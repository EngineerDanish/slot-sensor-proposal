#!/usr/bin/env python3
"""
Slot Sensor power budget (T-02).

Every output of this script is CALCULATED from the inputs below.
Inputs marked [DS] are datasheet typical values. Inputs marked [A] are our
assumptions and must be confirmed by measurement on a prototype.
Nothing here is MEASURED yet.

Run:  python3 analysis/power_budget.py
"""

import math

# ---------------------------------------------------------------------------
# Usage profile (Fixed Facts)
# ---------------------------------------------------------------------------
EVENTS_PER_DAY = 640          # F-5 upper bound, worst case
AWAKE_HOURS = 12              # F-9: sleeps at least 12 h, so at most 12 h awake
HEARTBEATS_PER_DAY = 24       # [A] one status uplink per hour for health checks

# ---------------------------------------------------------------------------
# LoRaWAN (SX1262)
# ---------------------------------------------------------------------------
BW_HZ = 125_000               # uplink bandwidth
CR = 1                        # coding rate 4/5
PREAMBLE = 8
LORAWAN_OVERHEAD_B = 13       # MHDR 1 + DevAddr 4 + FCtrl 1 + FCnt 2 + FPort 1 + MIC 4
PAYLOAD_EVENT_B = 8           # [A] slot bitmap 2, event 1, counter 2, battery 1, temp 1, flags 1
PAYLOAD_GROUP_B = 11          # [A] kept at 11 B so it fits US915 DR0 (SF10)

I_TX_MA = {22: 118.0, 14: 45.0}   # [DS] SX1262 TX current with DC-DC, +22 / +14 dBm
I_RX_MA = 4.6                      # [DS] SX1262 RX current, DC-DC, 125 kHz
RX_WINDOW_SYMBOLS = 8              # [A] preamble detect timeout per window
RX_WINDOW_MARGIN_S = 0.015         # [A] timing margin per window
RX2_SF = 12                        # [A] worst case RX2 data rate (SF12, 125 kHz)

UPLINK_OVERHEAD_UC = (             # [A] per uplink, outside TX and RX windows
    0.008 * 2.0e3                  # radio wake, TCXO start, calibration: 8 ms at 2.0 mA
    + 0.015 * 3.3e3                # MCU running the LoRaWAN stack: 15 ms at 3.3 mA [DS run current]
)                                  # in microcoulombs (s * uA)

# ---------------------------------------------------------------------------
# Bluetooth LE (nRF52840)
# ---------------------------------------------------------------------------
BLE_ADV_EVENT_UC = 12.0       # [A] one connectable advertising event, 3 channels, 0 dBm, 31 B
BLE_ADV_INTERVAL_S = 1.0      # [A] advertising only while awake
BLE_CONN_HOURS = 2.0          # [A] a phone connected 2 h per day
BLE_CONN_INTERVAL_S = 0.25    # [A]
BLE_CONN_EVENT_UC = 8.0       # [A] one connection event with a short notification

# ---------------------------------------------------------------------------
# Switch scanning (strobed pull-ups)
# ---------------------------------------------------------------------------
N_SWITCHES = 16
V_GPIO = 3.0                  # [A] GPIO supply, worst case (1.8 V would lower pull-up current)
R_PULLUP = 13_000             # [DS] nRF52840 internal pull-up, typical
PULLUP_ON_S = 20e-6           # [A] pull-ups enabled per scan, settle and read
SCAN_MCU_S = 60e-6            # [A] wake, read port, compare, back to sleep
I_MCU_RUN_MA = 3.3            # [DS] nRF52840 CPU running from flash, DC-DC
SCAN_HOURS = 24               # [A] worst case: scanning continues during sleep (P-2 open)
EVENT_MCU_S = 0.002           # [A] debounce confirm and queue per event

# ---------------------------------------------------------------------------
# Static floor (sleep) currents at 25 C
# ---------------------------------------------------------------------------
I_NRF_SLEEP_UA = 3.16         # [DS] nRF52840 System ON, full RAM retention, RTC running
I_SX_SLEEP_UA = 0.6           # [DS] SX1262 sleep, warm start
I_BOARD_LEAK_UA = 1.0         # [A] supervisor, ESD parts, switched divider off
I_BUFFER_LEAK_UA = 3.0        # [A] pulse buffer (HLC or low-leak supercap), primary cell only
I_PCM_LEAK_UA = 3.0           # [A] Li-ion protection circuit, Li-ion only
DESERT_LEAK_FACTOR = 2.5      # [A] day-averaged rise in silicon and capacitor leakage, enclosure 40 to 70 C


def lora_airtime_s(phy_payload_b, sf, bw=BW_HZ, cr=CR, preamble=PREAMBLE):
    """Semtech AN1200.13 time on air, explicit header, CRC on."""
    t_sym = (2 ** sf) / bw
    de = 1 if (sf >= 11 and bw == 125_000) else 0   # low data rate optimisation
    num = 8 * phy_payload_b - 4 * sf + 28 + 16
    n_payload = 8 + max(math.ceil(num / (4 * (sf - 2 * de))) * (cr + 4), 0)
    return (preamble + 4.25 + n_payload) * t_sym


def rx_window_s(sf):
    return RX_WINDOW_SYMBOLS * (2 ** sf) / BW_HZ + RX_WINDOW_MARGIN_S


def uplink_charge_uc(sf, tx_dbm, payload_b):
    t_tx = lora_airtime_s(payload_b + LORAWAN_OVERHEAD_B, sf)
    q_tx = t_tx * I_TX_MA[tx_dbm] * 1e3
    q_rx = (rx_window_s(sf) + rx_window_s(RX2_SF)) * I_RX_MA * 1e3
    return q_tx + q_rx + UPLINK_OVERHEAD_UC, t_tx


def grouped_messages_per_day(events, awake_h, model):
    minutes = awake_h * 60
    if model == "worst":            # events spread evenly, every event in its own minute
        return min(events, minutes)
    lam = events / minutes          # random (Poisson) arrivals
    return minutes * (1 - math.exp(-lam))


def floor_ua(cell_chem, desert):
    silicon = I_NRF_SLEEP_UA + I_SX_SLEEP_UA + I_BOARD_LEAK_UA
    extra = I_BUFFER_LEAK_UA if cell_chem == "LiSOCl2" else I_PCM_LEAK_UA
    f = DESERT_LEAK_FACTOR if desert else 1.0
    return (silicon + extra) * f


def scan_ua(period_s, all_closed=True):
    n = N_SWITCHES if all_closed else 0
    q_scan = n * (V_GPIO / R_PULLUP) * 1e6 * PULLUP_ON_S + I_MCU_RUN_MA * 1e3 * SCAN_MCU_S
    return q_scan / period_s * (SCAN_HOURS / 24)


def ble_ua():
    adv = BLE_ADV_EVENT_UC / BLE_ADV_INTERVAL_S * (AWAKE_HOURS / 24)
    conn = BLE_CONN_EVENT_UC / BLE_CONN_INTERVAL_S * (BLE_CONN_HOURS / 24)
    return adv, conn


def budget(sf, tx_dbm, mode, cell_chem="LiSOCl2", desert=True, scan_period=0.1):
    if mode == "event":
        msgs, payload = EVENTS_PER_DAY, PAYLOAD_EVENT_B
    else:
        msgs, payload = grouped_messages_per_day(EVENTS_PER_DAY, AWAKE_HOURS, mode), PAYLOAD_GROUP_B
    q_up, _ = uplink_charge_uc(sf, tx_dbm, payload)
    q_hb, _ = uplink_charge_uc(sf, tx_dbm, PAYLOAD_EVENT_B)
    lora = (msgs * q_up + HEARTBEATS_PER_DAY * q_hb) / 86400
    adv, conn = ble_ua()
    ev = EVENTS_PER_DAY * I_MCU_RUN_MA * 1e3 * EVENT_MCU_S / 86400
    parts = {
        "LoRaWAN": lora,
        "BLE adv": adv,
        "BLE conn": conn,
        "Switch scan": scan_ua(scan_period),
        "Event handling": ev,
        "Sleep floor": floor_ua(cell_chem, desert),
    }
    return sum(parts.values()), parts, msgs


# ---------------------------------------------------------------------------
# Cells
# ---------------------------------------------------------------------------
# name, chemistry, nominal Ah, usable fraction [A], self-discharge (25 C, desert), fade per year (25 C, desert)
# Li-SOCl2 self-discharge is % of nominal per year (linear). Li-ion self-discharge is % of remaining per month.
CELLS = [
    ("Li-ion 18650 x1 (3.0 Ah)",     "Liion",   3.0, 0.95, (0.02, 0.04), (0.05, 0.15)),
    ("Li-ion 18650 x2 (6.0 Ah)",     "Liion",   6.0, 0.95, (0.02, 0.04), (0.05, 0.15)),
    ("Li-SOCl2 A ER18505 x1 (4.0 Ah)", "LiSOCl2", 4.0, 0.85, (0.01, 0.03), (0.0, 0.0)),
    ("Li-SOCl2 A ER18505 x2 (8.0 Ah)", "LiSOCl2", 8.0, 0.85, (0.01, 0.03), (0.0, 0.0)),
    ("Li-SOCl2 C ER26500 x1 (8.5 Ah)", "LiSOCl2", 8.5, 0.85, (0.01, 0.03), (0.0, 0.0)),
    ("Li-SOCl2 D ER34615 x1 (19 Ah)",  "LiSOCl2", 19.0, 0.85, (0.01, 0.03), (0.0, 0.0)),
]


def life_years(cell, i_avg_ua, desert=True, cap_years=15):
    name, chem, ah, usable, sd, fade = cell
    sd = sd[1] if desert else sd[0]
    fade = fade[1] if desert else fade[0]
    q = ah * usable                         # Ah of charge we can draw
    load_per_day = i_avg_ua * 1e-6 * 24     # Ah per day
    for day in range(int(cap_years * 365)):
        t = day / 365
        if chem == "Liion":
            q -= q * (sd / 30)                              # % of remaining per month
            cap = ah * usable * max(1 - fade * t, 0)        # irreversible fade caps what is left
            q = min(q, cap)
        else:
            q -= ah * sd / 365                              # % of nominal per year
        q -= load_per_day
        if q <= 0:
            return day / 365
    return float(cap_years)


def fmt(x, nd=1):
    return f"{x:.{nd}f}"


def main():
    print("## Airtime and charge per uplink (calculated)\n")
    print("| SF | PHY bytes | Airtime ms | Charge per uplink at +22 dBm (mC) | at +14 dBm (mC) |")
    print("|---|---|---|---|---|")
    for sf in (7, 8, 9, 10, 12):
        q22, t = uplink_charge_uc(sf, 22, PAYLOAD_EVENT_B)
        q14, _ = uplink_charge_uc(sf, 14, PAYLOAD_EVENT_B)
        print(f"| SF{sf} | {PAYLOAD_EVENT_B + LORAWAN_OVERHEAD_B} | {fmt(t*1e3)} | {fmt(q22/1e3, 2)} | {fmt(q14/1e3, 2)} |")

    print("\n## Messages per day (calculated)\n")
    for m in ("event", "poisson", "worst"):
        n = EVENTS_PER_DAY if m == "event" else grouped_messages_per_day(EVENTS_PER_DAY, AWAKE_HOURS, m)
        print(f"- {m}: {fmt(n,0)} event uplinks + {HEARTBEATS_PER_DAY} heartbeats")

    print("\n## Switch scanning (calculated, all 16 switches closed)\n")
    print(f"- static pull-ups, always on: {fmt(N_SWITCHES * V_GPIO / R_PULLUP * 1e6, 0)} uA")
    for p in (0.05, 0.1, 0.25, 0.5):
        print(f"- strobed every {int(p*1000)} ms: {fmt(scan_ua(p), 2)} uA")

    adv, conn = ble_ua()
    print(f"\n## BLE (calculated)\n\n- advertising: {fmt(adv,2)} uA\n- connections: {fmt(conn,2)} uA")
    print(f"\n## Sleep floor (calculated)\n")
    for chem in ("LiSOCl2", "Liion"):
        print(f"- {chem}: 25 C {fmt(floor_ua(chem, False),2)} uA, desert {fmt(floor_ua(chem, True),2)} uA")

    for tx in (22, 14):
        print(f"\n## Average current, desert, Li-SOCl2 floor, +{tx} dBm (calculated, uA)\n")
        print("| Mode | SF7 | SF9 | SF10 |")
        print("|---|---|---|---|")
        for mode, label in (("event", "Per event"), ("poisson", "1 min grouping, random arrivals"), ("worst", "1 min grouping, evenly spread")):
            row = [fmt(budget(sf, tx, mode)[0], 0) for sf in (7, 9, 10)]
            print(f"| {label} | " + " | ".join(row) + " |")

    print("\n## Breakdown, per event, SF10, +22 dBm, desert, Li-SOCl2 (calculated, uA)\n")
    tot, parts, _ = budget(10, 22, "event")
    for k, v in parts.items():
        print(f"- {k}: {fmt(v, 1)} ({fmt(100*v/tot, 1)}%)")
    print(f"- Total: {fmt(tot, 1)}")
    print("\n## Breakdown, per event, SF7, +14 dBm, desert, Li-SOCl2 (calculated, uA)\n")
    tot, parts, _ = budget(7, 14, "event")
    for k, v in parts.items():
        print(f"- {k}: {fmt(v, 1)} ({fmt(100*v/tot, 1)}%)")
    print(f"- Total: {fmt(tot, 1)}")

    for tx in (22, 14):
        for mode, label in (("event", "per event"), ("poisson", "1 min grouping, random arrivals")):
            print(f"\n## Battery life, desert, +{tx} dBm, {label} (calculated, years)\n")
            print("| Cell | SF7 | SF9 | SF10 |")
            print("|---|---|---|---|")
            for cell in CELLS:
                row = []
                for sf in (7, 9, 10):
                    i_avg = budget(sf, tx, mode, cell_chem=cell[1])[0]
                    row.append(fmt(life_years(cell, i_avg), 1))
                print(f"| {cell[0]} | " + " | ".join(row) + " |")

    print("\n## Self-discharge only, no load, desert (calculated, % of usable charge lost in 2 years)\n")
    for cell in CELLS:
        name, chem, ah, usable, sd, fade = cell
        q = ah * usable
        q0 = q
        for day in range(730):
            t = day / 365
            if chem == "Liion":
                q -= q * (sd[1] / 30)
                q = min(q, ah * usable * max(1 - fade[1] * t, 0))
            else:
                q -= ah * sd[1] / 365
        print(f"- {name}: {fmt(100*(1-q/q0), 0)}%")


if __name__ == "__main__":
    main()
