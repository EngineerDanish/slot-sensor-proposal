# Hardware and firmware milestone plan

Ticket T-10. Internal planning document for the basic version of the 16-slot unit: requirements, hardware, prototype build, firmware, testing, documentation, plus client communication and project management. It covers 3 prototype units. Dashboard, mobile app and enclosure work are separate items and appear here only as handover points.

Every hours figure in this document is an estimate. The same data is in `analysis/milestones-hw-fw.csv`. PCB layout is done by a partner, so those rows show the owner as partner and carry no hours here. All other rows are Danish's hours.

Totals: basic 280 h, buffer 42 h (15 percent), 322 h with buffer. Optional items add 44 h if taken. At 15 to 20 hours a week the basic plan runs 18 weeks, about 20 to 21 weeks with the buffer used.

## Requirements and architecture

| Milestone | Week | Subtask | Owner | Hours | Output |
|---|---|---|---|---|---|
| M1.1 Requirements freeze | 1 | Kickoff with the client to confirm open points (site region, quantity, slot layout, app platforms, events during sleep) | Danish | 3 | Meeting notes |
| M1.1 Requirements freeze | 1 | Write the requirements specification for the basic version | Danish | 5 | docs/requirements.md |
| M1.2 Architecture freeze | 1 to 2 | Finalise architecture and part choices from client answers (radio variant, cell type, harness route) | Danish | 4 | docs/architecture.md (final) |
| M1.2 Architecture freeze | 1 to 2 | Update the power budget for the final choices | Danish | 3 | docs/power-budget.md (final) |
| M1.2 Architecture freeze | 1 to 2 | Define interfaces with partners: board outline, connector and harness for enclosure, data fields for dashboard and app | Danish | 3 | docs/interfaces.md |

Milestone subtotals:

| Milestone | Hours |
|---|---|
| M1.1 Requirements freeze | 8 |
| M1.2 Architecture freeze | 10 |
| **Requirements and architecture total** | **18** |

## Hardware design

| Milestone | Week | Subtask | Owner | Hours | Output |
|---|---|---|---|---|---|
| M2.1 Schematic | 2 to 3 | Power section: cell holder, pulse buffer, buck regulator, reverse polarity, switched battery divider | Danish | 6 | Schematic sheet: power |
| M2.1 Schematic | 2 to 3 | Radio module section: RAK4630, LoRa and BLE antenna feeds, SWD, decoupling, test and current measurement points | Danish | 5 | Schematic sheet: radio |
| M2.1 Schematic | 2 to 3 | Switch interface: TCA6416A, series resistors, ESD clamps, switched NC rail, harness connector | Danish | 5 | Schematic sheet: switch interface |
| M2.1 Schematic | 2 to 3 | Switch section board schematic (4 switches per 6 inch section) | Danish | 3 | Schematic: switch section board |
| M2.1 Schematic | 2 to 3 | Electrical rules check, netlist and schematic PDF | Danish | 2 | Schematic PDF and netlist |
| M2.2 Part selection | 3 to 4 | Datasheet checks: switch mechanical life, expander inputs without pull-ups, buffer replacement rules, temperature ratings | Danish | 4 | Part selection notes |
| M2.2 Part selection | 3 to 4 | BOM with sources, alternates and quantities for 3 prototypes plus spares | Danish | 3 | BOM spreadsheet |
| M2.2 Part selection | 3 to 4 | Footprint and library check for every part | Danish | 3 | Checked part library |
| M2.3 Design review | 4 | Internal schematic review against a checklist | Danish | 3 | Review checklist |
| M2.3 Design review | 4 | Design review summary for the client and answers to their comments | Danish | 2 | Design review note |
| M2.3 Design review | 4 | Schematic fixes after review, release to layout | Danish | 2 | Released schematic rev A |
| M2.4 PCB layout | 5 to 6 | Main board layout | partner |  | Main board layout files |
| M2.4 PCB layout | 5 to 6 | Switch section board layout | partner |  | Section board layout files |
| M2.4 PCB layout | 5 to 6 | Gerbers, drill, pick and place and assembly drawings | partner |  | Fabrication package |
| M2.4 PCB layout | 5 to 6 | Layout review: antenna keep-out, power paths, test points, fit with enclosure | Danish | 4 | Layout review comments |

Milestone subtotals:

| Milestone | Hours |
|---|---|
| M2.1 Schematic | 21 |
| M2.2 Part selection | 10 |
| M2.3 Design review | 7 |
| M2.4 PCB layout | 4 |
| **Hardware design total** | **42** |

## Prototype build and bring-up

| Milestone | Week | Subtask | Owner | Hours | Output |
|---|---|---|---|---|---|
| M3.1 Fabrication and parts | 7 to 11 | Place PCB fabrication and parts orders, track deliveries | Danish | 3 | Purchase orders |
| M3.1 Fabrication and parts | 7 to 11 | Incoming inspection of boards and parts | Danish | 2 | Inspection checklist |
| M3.2 Assembly | 11 to 12 | Assemble 3 units: remaining parts, switches, harnesses | Danish | 10 | 3 assembled prototype boards |
| M3.2 Assembly | 11 to 12 | Fit check with the slot body and enclosure supplied by the partner | Danish | 3 | Fit check notes |
| M3.3 Bring-up | 12 | Power-up, rail checks and first current check on each unit | Danish | 3 | Bring-up log |
| M3.3 Bring-up | 12 | Programming, module check and radio sanity test on each unit | Danish | 2 | Bring-up log |
| M3.3 Bring-up | 12 | Rework and hardware errata list | Danish | 3 | Errata list |

Milestone subtotals:

| Milestone | Hours |
|---|---|
| M3.1 Fabrication and parts | 5 |
| M3.2 Assembly | 13 |
| M3.3 Bring-up | 8 |
| **Prototype build and bring-up total** | **26** |

## Firmware

| Milestone | Week | Subtask | Owner | Hours | Output |
|---|---|---|---|---|---|
| M4.1 Board bring-up on Zephyr | 5 and 13 | Zephyr project, custom board definition and devicetree, build setup (first on the module dev kit) | Danish | 6 | Firmware repo, board files |
| M4.1 Board bring-up on Zephyr | 5 and 13 | Move firmware to the prototype boards and fix pin and power differences | Danish | 4 | Firmware running on prototype |
| M4.2 Switch reading and debounce | 5 to 6 | Expander driver setup and interrupt wake from sleep | Danish | 5 | Switch input module |
| M4.2 Switch reading and debounce | 5 to 6 | Debounce, 16-slot state and event counter | Danish | 5 | Slot state module |
| M4.2 Switch reading and debounce | 5 to 6 | Unit tests for debounce and state logic | Danish | 3 | Test results |
| M4.3 LoRaWAN on Helium | 6 to 8 | LoRaWAN stack setup, region settings, OTAA join on Helium | Danish | 8 | Joined device on Helium console |
| M4.3 LoRaWAN on Helium | 6 to 8 | 1-minute grouping with full 16-slot state and counter in each unconfirmed uplink | Danish | 6 | Uplink module |
| M4.3 LoRaWAN on Helium | 6 to 8 | Join retry, link check, data rate policy and duty cycle handling | Danish | 6 | Link handling module |
| M4.4 Encrypted BLE advertising | 9 | Advertising payload with slot state, encrypted with the app key, with replay counter | Danish | 8 | BLE module |
| M4.4 Encrypted BLE advertising | 9 | Per-unit key provisioning and reference decoder for the app team | Danish | 4 | Key tool and reference decoder |
| M4.5 Sleep schedule | 9 to 10 | Inactivity detection, nightly sleep after 10 pm, time sync over LoRaWAN, wake | Danish | 6 | Sleep schedule module |
| M4.5 Sleep schedule | 9 to 10 | Handling of events during sleep per the client's answer | Danish | 2 | Sleep event handling |
| M4.6 Battery and heartbeat | 10 to 11 | Battery voltage under load, temperature reading, daily heartbeat uplink | Danish | 4 | Heartbeat module |
| M4.6 Battery and heartbeat | 10 to 11 | Low power tuning: peripherals off, lowest sleep current | Danish | 6 | Power tuned build |
| M4.7 Reliability and settings | 11 | Watchdog, brownout and fault recovery | Danish | 4 | Reliability module |
| M4.7 Reliability and settings | 11 | Settings in flash: LoRaWAN keys, BLE key, grouping and sleep settings | Danish | 3 | Settings module |
| M4.8 Payload spec and decoder | 8 | Payload specification for uplink, heartbeat and BLE | Danish | 3 | docs/payload-spec.md |
| M4.8 Payload spec and decoder | 8 | Helium decoder function with test vectors | Danish | 4 | decoder.js and test vectors |
| M4.8 Payload spec and decoder | 8 | Handover session with the dashboard and app team | Danish | 2 | Handover notes |
| M4.9 Integration | 13 | Integration on prototype boards and bug fixing | Danish | 8 | Firmware release v0.9 |

Milestone subtotals:

| Milestone | Hours |
|---|---|
| M4.1 Board bring-up on Zephyr | 10 |
| M4.2 Switch reading and debounce | 13 |
| M4.3 LoRaWAN on Helium | 20 |
| M4.4 Encrypted BLE advertising | 12 |
| M4.5 Sleep schedule | 8 |
| M4.6 Battery and heartbeat | 10 |
| M4.7 Reliability and settings | 7 |
| M4.8 Payload spec and decoder | 9 |
| M4.9 Integration | 8 |
| **Firmware total** | **97** |

## Testing

| Milestone | Week | Subtask | Owner | Hours | Output |
|---|---|---|---|---|---|
| M5.1 Current measurement | 13 to 14 | Bench setup and measurement at room temperature: sleep floor, charge per uplink, BLE events, switch reading | Danish | 6 | Current test report (room) |
| M5.1 Current measurement | 13 to 14 | Measurement at 60 to 70 C: sleep floor and cell voltage under transmit pulse with buffer | Danish | 6 | Current test report (high temperature) |
| M5.1 Current measurement | 13 to 14 | Update the power budget with measured values | Danish | 3 | docs/power-budget.md (measured) |
| M5.2 Signal test | 15 | Signal test to the Helium hotspot: RSSI, SNR, spreading factor and packet loss log | Danish | 5 | Signal test report |
| M5.3 Functional and endurance test | 15 to 16 | Test plan and 16-slot functional test on all 3 units, both radios | Danish | 6 | Functional test report |
| M5.3 Functional and endurance test | 15 to 16 | Endurance run: repeated place and remove cycles, message loss count over at least one week | Danish | 8 | Endurance test report |
| M5.4 Field trial support | 17 to 18 | Installation support and remote log review during the field trial | Danish | 8 | Field trial log |
| M5.4 Field trial support | 17 to 18 | Fixes from the field trial and firmware release | Danish | 6 | Firmware release v1.0 |

Milestone subtotals:

| Milestone | Hours |
|---|---|
| M5.1 Current measurement | 15 |
| M5.2 Signal test | 5 |
| M5.3 Functional and endurance test | 14 |
| M5.4 Field trial support | 14 |
| **Testing total** | **48** |

## Documentation and handover

| Milestone | Week | Subtask | Owner | Hours | Output |
|---|---|---|---|---|---|
| M6.1 Documentation | 16 to 18 | Firmware source handover with build and flash guide | Danish | 4 | Firmware guide |
| M6.1 Documentation | 16 to 18 | Hardware design package: schematic, BOM, layout files, assembly notes | Danish | 3 | Hardware package |
| M6.1 Documentation | 16 to 18 | Compiled test reports | Danish | 3 | Test report set |
| M6.1 Documentation | 16 to 18 | Installation and battery replacement guide | Danish | 3 | Field guide |
| M6.2 Handover | 18 | Handover meeting and close-out | Danish | 2 | Signed handover note |

Milestone subtotals:

| Milestone | Hours |
|---|---|
| M6.1 Documentation | 13 |
| M6.2 Handover | 2 |
| **Documentation and handover total** | **15** |

## Client communication and project management

| Milestone | Week | Subtask | Owner | Hours | Output |
|---|---|---|---|---|---|
| M7.1 Client communication | 1 to 18 | Weekly progress update to the client | Danish | 16 | Weekly updates |
| M7.1 Client communication | 1 to 18 | Milestone demos and sign-off (4 milestones) | Danish | 6 | Sign-off notes |
| M7.2 Project management | 1 to 18 | Partner coordination for layout, enclosure, dashboard and app | Danish | 8 | Coordination notes |
| M7.2 Project management | 1 to 18 | Plan, risk and issue tracking | Danish | 4 | Project board |

Milestone subtotals:

| Milestone | Hours |
|---|---|
| M7.1 Client communication | 22 |
| M7.2 Project management | 12 |
| **Client communication and project management total** | **34** |

## Optional

| Milestone | Week | Subtask | Owner | Hours | Output |
|---|---|---|---|---|---|
| O1 Firmware update over Bluetooth | Adds about 1.5 weeks after M4.7 | Secure bootloader with signed images and dual slot | Danish | 8 | Bootloader build |
| O1 Firmware update over Bluetooth | Adds about 1.5 weeks after M4.7 | Bluetooth update service and support to the app team | Danish | 8 | Update service |
| O1 Firmware update over Bluetooth | Adds about 1.5 weeks after M4.7 | Update testing including power loss during update | Danish | 6 | Update test report |
| O2 Site signal survey before design | Adds about 1 week before week 1 | Prepare a test node from a dev kit with logging | Danish | 4 | Test node |
| O2 Site signal survey before design | Adds about 1 week before week 1 | Survey support and data review | Danish | 5 | Survey log |
| O2 Site signal survey before design | Adds about 1 week before week 1 | Survey report with spreading factor and power budget impact | Danish | 3 | Signal survey report |
| O3 Client-owned gateway setup | Adds about 0.5 week before M5.2 | Gateway selection and configuration | Danish | 4 | Gateway config |
| O3 Client-owned gateway setup | Adds about 0.5 week before M5.2 | Network server routing and device registration | Danish | 4 | Network setup notes |
| O3 Client-owned gateway setup | Adds about 0.5 week before M5.2 | End to end test through the client gateway | Danish | 2 | Gateway test note |

Milestone subtotals:

| Milestone | Hours |
|---|---|
| O1 Firmware update over Bluetooth | 22 |
| O2 Site signal survey before design | 12 |
| O3 Client-owned gateway setup | 10 |
| **Optional total** | **44** |

## Module summary

| Module | Hours |
|---|---|
| Requirements and architecture | 18 |
| Hardware design | 42 |
| Prototype build and bring-up | 26 |
| Firmware | 97 |
| Testing | 48 |
| Documentation and handover | 15 |
| Client communication and project management | 34 |
| **Basic total** | **280** |
| Buffer (15 percent) | 42 |
| **Total with buffer** | **322** |
| Optional total (not in the basic total) | 44 |

## Week by week plan

Assumption: Danish works about 15 to 20 hours a week on this project, since he is also studying full time. Week 1 starts when the project is awarded and the advance is received. The buffer is not placed in a given week; if it is used it adds about 2 to 3 weeks at the same pace.

| Week | Milestones running (Danish hours) | Danish hours | Partner work and lead times |
|---|---|---|---|
| 1 | M1.1 Requirements freeze (8); M1.2 Architecture freeze (6); M7 Communication and management (2) | 16 |  |
| 2 | M1.2 Architecture freeze (4); M2.1 Schematic (10); M7 Communication and management (2) | 16 |  |
| 3 | M2.1 Schematic (11); M2.2 Part selection (4); M7 Communication and management (2) | 17 |  |
| 4 | M2.2 Part selection (6); M2.3 Design review (7); M7 Communication and management (2) | 15 |  |
| 5 | M4.1 Board bring-up on Zephyr (6); M4.2 Switch reading and debounce (8); M7 Communication and management (2) | 16 | Partner starts PCB layout |
| 6 | M2.4 PCB layout (4); M4.2 Switch reading and debounce (5); M4.3 LoRaWAN on Helium (5); M7 Communication and management (2) | 16 | Partner finishes layout; fabrication package released |
| 7 | M3.1 Fabrication and parts (3); M4.3 LoRaWAN on Helium (11); M7 Communication and management (2) | 16 | PCB fabrication and shipping (about 3 to 4 weeks, lead time only) |
| 8 | M4.3 LoRaWAN on Helium (4); M4.8 Payload spec and decoder (9); M7 Communication and management (2) | 15 | Fabrication and shipping continue |
| 9 | M4.4 Encrypted BLE advertising (12); M4.5 Sleep schedule (2); M7 Communication and management (2) | 16 | Fabrication and shipping continue |
| 10 | M4.5 Sleep schedule (6); M4.6 Battery and heartbeat (8); M7 Communication and management (2) | 16 | Fabrication and shipping continue |
| 11 | M4.6 Battery and heartbeat (2); M4.7 Reliability and settings (7); M3.1 Fabrication and parts (2); M3.2 Assembly (5); M7 Communication and management (2) | 18 | Boards and parts arrive; enclosure and slot body from partner |
| 12 | M3.2 Assembly (8); M3.3 Bring-up (8); M7 Communication and management (2) | 18 |  |
| 13 | M4.1 Board bring-up on Zephyr (4); M4.9 Integration (8); M5.1 Current measurement (2); M7 Communication and management (2) | 16 |  |
| 14 | M5.1 Current measurement (13); M7 Communication and management (2) | 15 |  |
| 15 | M5.2 Signal test (5); M5.3 Functional and endurance test (9); M7 Communication and management (2) | 16 | Endurance run starts and runs unattended |
| 16 | M5.3 Functional and endurance test (5); M6.1 Documentation (7); M7 Communication and management (2) | 14 | Endurance run continues |
| 17 | M5.4 Field trial support (8); M6.1 Documentation (3); M7 Communication and management (1) | 12 | Field trial on site |
| 18 | M5.4 Field trial support (6); M6.1 Documentation (3); M6.2 Handover (2); M7 Communication and management (1) | 12 |  |
| **Total** | | **280** | |

Firmware starts on the radio module's dev kit in week 5, so the PCB layout and fabrication weeks are used for firmware rather than waiting.

## Assumptions behind the hours

- Engineer with 5 years of nRF52840, Zephyr and LoRaWAN work, so no learning time for the toolchain, the radio stacks or Helium onboarding.
- Architecture and power budget already drafted (T-02, T-03); M1 only finalises them with the client's answers.
- Design as in docs/architecture.md: RAK4630, TCA6416A with interrupt, SPDT D2HW switches, TPS62840, replaceable lithium primary cell with pulse buffer. A change of platform or cell type after M1.2 needs a re-estimate.
- One main board and one switch section board design, one board revision. A second spin would add schematic, review, bring-up and lead time.
- PCB layout, 3D model, slot body and enclosure come from a partner on time for week 11; Danish's time covers interfaces, layout review and fit check only.
- PCB fabrication and shipping take about 3 to 4 weeks (weeks 7 to 10). Danish hand-assembles the remaining parts and the harnesses for 3 units.
- Firmware uses Zephyr's LoRaWAN and Bluetooth stacks as they are. One region plan only, set by the site region still to be confirmed.
- Uplinks are unconfirmed and carry the full 16-slot state plus a counter (A-7), with 1-minute grouping (F-17). BLE is advertising only, encrypted with an app key (A-8).
- Handling of events during sleep is 2 hours, assuming a simple rule (queue and send on wake, or ignore); a complex rule needs more.
- The payload spec and decoder are the only firmware deliverables to the dashboard and app team; their own work is not in these hours.
- Testing uses bench gear Danish already has (current profiler, temperature oven or chamber). The endurance run is mostly unattended; only setup and review are counted.
- Field trial is supported remotely with installation guidance; site travel, if needed, is not in these hours.
- Client communication assumes one written update a week plus 4 milestone demos, through text and short calls.
- No certification work (FCC or CE) is included; that waits on the client's answer.
- Optional items: firmware update over Bluetooth also needs the app team's work; the site signal survey assumes someone on site places the test node; the client gateway setup assumes the client buys the gateway.
