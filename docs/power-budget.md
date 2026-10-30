# Power budget and battery feasibility

Ticket T-02. Every number in this document is calculated by `analysis/power_budget.py` from the inputs listed below. Nothing is measured yet. Inputs marked [DS] are datasheet typical values, inputs marked [A] are our assumptions. Battery life figures are estimates and must be confirmed by measurement on a prototype.

## Summary

The LoRaWAN spreading factor decides almost everything. At SF10 and +22 dBm, sending on every event averages about 380 uA (calculated), which is roughly 3.3 Ah a year. No 18650 option, Li-ion or otherwise, reaches 2 years at that point.

At SF7 the same unit averages about 93 uA (calculated) and most options reach 2 years.

Grouping events into one message per minute saves nothing in the worst case (events spread evenly) and about 30% with random arrivals. It helps, but it does not rescue the SF10 case on a small cell.

Li-ion is the weaker chemistry here. In desert heat a single 18650 loses an estimated 62% of its charge in 2 years to self-discharge and ageing alone, before the device draws anything.

Recommendation: a single D-size Li-SOCl2 cell (ER34615, 19 Ah) with a pulse buffer. It gives an estimated 4.1 years at the worst case (SF10, +22 dBm, per event, desert), so the 2 year target holds even if the hotspot forces SF10. If the client prefers to keep the 18650 size, 2 years is only realistic when the link runs at SF7 to SF8, which a site test can show.

---

## Assumptions

### Usage (from Fixed Facts)

| Input | Value | Source |
|---|---|---|
| Events per day | 640 | F-5, upper bound |
| Awake hours per day | 12 | F-9, least sleep is the worst case |
| Heartbeat uplinks | 24 per day | [A] one per hour for health checks |
| Switch scanning during sleep | yes, 24 h | [A] worst case, P-2 open |

### LoRaWAN (SX1262)

| Input | Value | Source |
|---|---|---|
| Event payload | 8 bytes (21 bytes on air with 13 bytes LoRaWAN overhead) | [A] |
| Grouped payload | 11 bytes, fits US915 DR0 at SF10 | [A] |
| Bandwidth, coding rate, preamble | 125 kHz, 4/5, 8 symbols | [A] standard uplink |
| TX current +22 dBm | 118 mA | [DS] SX1262, DC-DC |
| TX current +14 dBm | 45 mA | [DS] SX1262, DC-DC |
| RX current | 4.6 mA | [DS] SX1262, DC-DC |
| RX windows | RX1 at uplink SF, RX2 at SF12, each 8 symbols plus 15 ms | [A] worst case RX2 |
| Overhead per uplink | radio wake and TCXO 8 ms at 2 mA, MCU stack 15 ms at 3.3 mA | [A] |
| Uplink type | unconfirmed, no downlink expected | [A] |

### Bluetooth LE (nRF52840)

| Input | Value | Source |
|---|---|---|
| Advertising | connectable, 0 dBm, 1 s interval, awake hours only | [A] |
| Charge per advertising event | 12 uC | [A] three channels, 31 bytes |
| Phone connected | 2 h a day, 250 ms interval, 8 uC per connection event | [A] |

### Switch scanning

| Input | Value | Source |
|---|---|---|
| Switches | 16, all closed | F-1, worst case |
| Pull-up | 13 kOhm internal, 3.0 V | [DS] nRF52840 typical, [A] voltage |
| Pull-up on time per scan | 20 us | [A] |
| MCU time per scan | 60 us at 3.3 mA | [A] |
| Scan period | 100 ms | [A] |

### Sleep floor at 25 C

| Part | Current | Source |
|---|---|---|
| nRF52840 System ON, full RAM, RTC | 3.16 uA | [DS] |
| SX1262 sleep, warm start | 0.6 uA | [DS] |
| Board leakage (supervisor, ESD, divider off) | 1.0 uA | [A] |
| Pulse buffer leakage (primary cell only) | 3.0 uA | [A] |
| Li-ion protection circuit (Li-ion only) | 3.0 uA | [A] |
| Desert factor on the floor | x2.5 | [A] day average, enclosure 40 to 70 C |

### Cells

| Cell | Nominal | Usable fraction | Self-discharge, desert | Ageing, desert | Source |
|---|---|---|---|---|---|
| Li-ion 18650 | 3.0 Ah | 0.95 | 4% of remaining per month | 15% capacity per year | [A] |
| Li-SOCl2 A, ER18505 | 4.0 Ah | 0.85 | 3% of nominal per year | none modelled | [A] |
| Li-SOCl2 C, ER26500 | 8.5 Ah | 0.85 | 3% of nominal per year | none modelled | [A] |
| Li-SOCl2 D, ER34615 | 19 Ah | 0.85 | 3% of nominal per year | none modelled | [A] |

The usable fraction for Li-SOCl2 allows for cut-off under pulse load and heat. Battery current is taken as equal to chip current (direct supply or LDO).

---

## 1. Uplink airtime and charge

Airtime uses the Semtech time-on-air formula. Charge includes TX, both RX windows and the fixed overhead.

| SF | Airtime (21 bytes) | Charge at +22 dBm | Charge at +14 dBm |
|---|---|---|---|
| SF7 | 56.6 ms | 8.1 mC | 4.0 mC |
| SF8 | 102.9 ms | 13.6 mC | 6.1 mC |
| SF9 | 185.3 ms | 23.4 mC | 9.9 mC |
| SF10 | 370.7 ms | 45.5 mC | 18.4 mC |
| SF12 | 1482.8 ms | 177.6 mC | 69.3 mC |

All calculated. Each step up in SF roughly doubles the charge per message.

## 2. Per event sending vs 1-minute grouping

With grouping, the number of messages equals the number of minutes that contain at least one event.

| Mode | Event uplinks per day | Notes |
|---|---|---|
| Per event | 640 | F-5 upper bound |
| 1 min grouping, events evenly spread | 640 | worst case, every event in its own minute |
| 1 min grouping, random arrivals | 424 | Poisson, 640 events over 720 awake minutes |

All calculated, plus 24 heartbeats a day in every mode. If events come in bursts the saving is larger than 34%, but we cannot count on that without client data.

The 11 byte grouped payload carries the current state of all 16 slots and which slots changed. It does not carry a timestamp for every event. If per-event timestamps are needed, the grouped message gets longer and, in US915 at SF10, may not fit one uplink.

## 3. Switch scanning with strobed pull-ups

A closed switch with a permanent pull-up draws current all the time. With all 16 slots occupied that is 3692 uA (calculated), ten times the whole worst-case budget. So the pull-ups are switched on only for a short read.

| Scan period | Average current, all 16 closed |
|---|---|
| Static pull-ups | 3692 uA |
| 50 ms | 5.4 uA |
| 100 ms (chosen) | 2.7 uA |
| 250 ms | 1.1 uA |
| 500 ms | 0.5 uA |

All calculated. At 100 ms a place or remove is seen within 0.1 s and confirmed on the next read. Running the GPIO at 1.8 V instead of 3.0 V lowers the 100 ms figure to 2.4 uA (calculated). The MCU wake-up, not the pull-ups, is most of this current.

## 4. Bluetooth LE

| Item | Average current |
|---|---|
| Advertising, 1 s, awake hours | 6.0 uA |
| Phone connection, 2 h a day | 2.7 uA |

All calculated. BLE is small next to LoRaWAN at SF9 and above. It matters at SF7, where it is about 14% of the total.

## 5. Sleep floor

| Case | 25 C | Desert |
|---|---|---|
| Either chemistry | 7.8 uA | 19.4 uA |

All calculated. The desert figure is the weakest number in this document because silicon and capacitor leakage rise steeply with heat. It needs a measurement at 60 to 70 C.

## 6. Average current, desert

At +22 dBm (worst case TX power):

| Mode | SF7 | SF9 | SF10 |
|---|---|---|---|
| Per event | 93 uA | 211 uA | 380 uA |
| 1 min grouping, random arrivals | 76 uA | 164 uA | 267 uA |
| 1 min grouping, evenly spread | 98 uA | 229 uA | 380 uA |

At +14 dBm:

| Mode | SF7 | SF9 | SF10 |
|---|---|---|---|
| Per event | 62 uA | 107 uA | 172 uA |
| 1 min grouping, random arrivals | 53 uA | 87 uA | 126 uA |
| 1 min grouping, evenly spread | 63 uA | 114 uA | 172 uA |

All calculated. Evenly spread grouping is slightly above per event at SF7 and SF9 because the grouped payload is 3 bytes longer.

Where the current goes, per event, desert, Li-SOCl2:

| Part | SF10, +22 dBm | SF7, +14 dBm |
|---|---|---|
| LoRaWAN | 349 uA (92%) | 31 uA (50%) |
| Sleep floor | 19 uA (5%) | 19 uA (32%) |
| BLE advertising and connection | 9 uA (2%) | 9 uA (14%) |
| Switch scanning | 3 uA (1%) | 3 uA (4%) |

All calculated.

## 7. Battery comparison

### Chemistry at desert temperatures

| Point | Li-ion 18650 | Li-SOCl2 (bobbin) |
|---|---|---|
| Nominal voltage | 3.6 to 3.7 V, 4.2 V full | 3.6 V, flat |
| Self-discharge, desert | about 4% a month [A] | about 3% a year [A] |
| Charge lost in 2 years with no load, desert | 62% (calculated) | 7% (calculated) |
| Operating temperature | usually up to 60 C on discharge | typically up to 85 C |
| Heat and full charge | fast ageing, swelling risk in a sealed box | not an issue |
| Pulse current for the radio | handles it directly | needs a buffer (hybrid capacitor or supercap) or a spiral cell |
| Supply to SX1262 (max 3.7 V) | needs a regulator at 4.2 V | can feed it directly |
| Protection circuit | needed, adds leakage | not needed |

Even at a milder 2% a month, a Li-ion cell loses about 39% (calculated) of its charge in 2 years from self-discharge alone, before ageing.

### Battery life, desert, +22 dBm (years, calculated)

Per event:

| Cell | SF7 | SF9 | SF10 |
|---|---|---|---|
| Li-ion 18650 x1 (3.0 Ah) | 2.0 | 1.1 | 0.7 |
| Li-ion 18650 x2 (6.0 Ah) | 3.0 | 1.9 | 1.2 |
| Li-SOCl2 A x1 (4.0 Ah) | 3.6 | 1.7 | 1.0 |
| Li-SOCl2 A x2 (8.0 Ah) | 6.4 | 3.3 | 1.9 |
| Li-SOCl2 C x1 (8.5 Ah) | 6.7 | 3.4 | 2.0 |
| Li-SOCl2 D x1 (19 Ah) | 11.6 | 6.7 | 4.1 |

1 min grouping, random arrivals:

| Cell | SF7 | SF9 | SF10 |
|---|---|---|---|
| Li-ion 18650 x1 (3.0 Ah) | 2.3 | 1.4 | 1.0 |
| Li-ion 18650 x2 (6.0 Ah) | 3.4 | 2.2 | 1.6 |
| Li-SOCl2 A x1 (4.0 Ah) | 4.3 | 2.2 | 1.4 |
| Li-SOCl2 A x2 (8.0 Ah) | 7.5 | 4.0 | 2.6 |
| Li-SOCl2 C x1 (8.5 Ah) | 7.9 | 4.3 | 2.8 |
| Li-SOCl2 D x1 (19 Ah) | 13.1 | 8.0 | 5.6 |

### Battery life, desert, +14 dBm (years, calculated)

Per event:

| Cell | SF7 | SF9 | SF10 |
|---|---|---|---|
| Li-ion 18650 x1 (3.0 Ah) | 2.6 | 1.9 | 1.3 |
| Li-ion 18650 x2 (6.0 Ah) | 3.7 | 2.8 | 2.1 |
| Li-SOCl2 A x1 (4.0 Ah) | 5.2 | 3.2 | 2.1 |
| Li-SOCl2 A x2 (8.0 Ah) | 8.7 | 5.8 | 3.9 |
| Li-SOCl2 C x1 (8.5 Ah) | 9.1 | 6.1 | 4.1 |
| Li-SOCl2 D x1 (19 Ah) | 14.6 | 10.7 | 7.8 |

1 min grouping, random arrivals:

| Cell | SF7 | SF9 | SF10 |
|---|---|---|---|
| Li-ion 18650 x1 (3.0 Ah) | 2.8 | 2.1 | 1.7 |
| Li-ion 18650 x2 (6.0 Ah) | 4.0 | 3.2 | 2.6 |
| Li-SOCl2 A x1 (4.0 Ah) | 5.8 | 3.9 | 2.8 |
| Li-SOCl2 A x2 (8.0 Ah) | 9.7 | 6.8 | 5.1 |
| Li-SOCl2 C x1 (8.5 Ah) | 10.1 | 7.1 | 5.3 |
| Li-SOCl2 D x1 (19 Ah) | 15.0 | 12.1 | 9.6 |

Lives above about 10 years are arithmetic only. Real cells, seals and electronics will not be trusted that long.

## 8. Airtime limits that affect per event sending

These come from LoRaWAN regional rules, not from the battery, but they decide whether per event sending is possible at all.

| Region | Limit | Effect (calculated) |
|---|---|---|
| EU868 | 1% duty cycle per sub-band, 36 s of airtime an hour | SF10 allows 97 uplinks an hour, SF12 allows 24. The awake average is 53 events an hour, so per event works at SF10 but bursts can be delayed, and SF12 needs grouping |
| US915 | 400 ms dwell time, SF10 is the slowest uplink rate | 21 bytes at SF10 is 370.7 ms, it fits. Payload at SF10 is limited to 11 bytes |

The LoRaWAN region of the site is not in the Fixed Facts. It also sets the real worst-case TX power: EU868 effectively caps at +14 to +16 dBm, US915 allows +22 dBm.

## 9. Recommendation

Use a single D-size Li-SOCl2 cell (ER34615, 19 Ah) with a low-leakage pulse buffer, and support both per event sending and 1-minute grouping in firmware.

- At the worst case (SF10, +22 dBm, per event, desert) the estimated life is 4.1 years, about twice the 2 year target. This margin covers the uncertain desert sleep floor and an SF we cannot know until a site test.

- Li-ion 18650 is not recommended. Self-discharge and ageing in heat take most of its charge in 2 years, it needs a protection circuit and a regulator, and it is a heat risk in a sealed box. This supports working assumption A-6.

- If the client wants to keep the 18650 size, the honest position is that 2 years holds only when the link runs at SF7 to SF8. A single A-size Li-SOCl2 (the closest primary cell to 18650, 18.5 x 50.5 mm) then gives an estimated 3.6 years at SF7. At SF9 and above it falls short.

- 1-minute grouping (P-1) is worth having as a setting. It gives about 30% more life with random event timing, and it is required in EU868 if the link drops to SF11 or SF12.

All of these are estimates from the power budget, to be confirmed by measurement.

## 10. To be measured on the prototype

- Sleep floor at 25 C and at 60 to 70 C, the largest unknown at low SF.

- Charge per uplink at the SF and TX power the site actually gives.

- Cell voltage under the TX pulse at high temperature, with the chosen buffer.

- Charge per BLE advertising event and per connection event.

- Switch scan current with all 16 slots occupied.
