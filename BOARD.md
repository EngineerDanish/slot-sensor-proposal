# Slot Sensor: Board

Single source of truth for the Slot Sensor brigade. Only the MANAGER chat edits Fixed Facts, Working Assumptions, Parked Questions and ticket statuses (except a station setting its own ticket to IN REVIEW).

Status values: READY, BLOCKED, IN PROGRESS, IN REVIEW, DONE, REOPENED, PARKED

---

## Fixed Facts

Stated by the client (through Uzair). Do not ask about these again.

| ID | Fact |
|---|---|
| F-1 | 16 slots, one mechanical switch per slot |
| F-2 | 24 inches long, in four 6 inch sections with 4 slots each (16 slots, about 1.5 in / 38 mm apart). Corrected 2026-10-31 from the client's own words; the discussion document wrongly said a slot every 6 inches, so the proposal states the layout for the client to confirm |
| F-3 | Object weight approx. 200 to 210 g (assumed by the client for now) |
| F-4 | No lid or cover over the slots |
| F-5 | Approx. 30 to 40 place/remove events per slot per day (about 480 to 640 per unit) |
| F-6 | Data sent to the internet and to a mobile phone every time an object is placed or removed |
| F-7 | Power: one 18650 cell, maximum two. Battery only, no charging system |
| F-8 | Battery life target: 2 to 3 years (at least 2) |
| F-9 | Sleeps at least 12 hours a day, sometimes up to 16 |
| F-10 | Internet over Helium LoRaWAN; coverage confirmed at site |
| F-11 | Bluetooth receiver is a mobile phone |
| F-12 | Site is a desert; unit must resist UV, water and dirt |
| F-13 | Priorities: minimal cost, long life, high reliability |
| F-14 | Client will sign an NDA once the project moves forward, i.e. after they accept our proposal, not before it |
| F-15 | Uzair has done two PCB projects for this client; no budget shared, asked us to suggest one |
| F-16 | Danish handles the project start to end, hardware included; Uzair confirmed he will not take any part (busy with other projects) and asked for our final quotation to discuss with the client |
| F-17 | A delay of up to 1 minute is acceptable, so close events can go in one message (answer to P-1, 2026-10-31) |
| F-18 | Daily sleep starts after 10 pm, following several hours of inactivity (answer to P-2, first half only) |
| F-19 | Highest expected site temperature: 100 F (about 38 C). Read as ambient air; solar heating inside the enclosure is on top of this (answer to P-3) |
| F-20 | After 2 years the battery is replaced on site, not the whole unit (answer to P-4) |
| F-21 | Bluetooth data readable by any nearby phone that has the specific app (answer to P-5) |
| F-22 | Client wants the dashboard (answer to P-6) |
| F-23 | Client wants the mobile application (answer to P-7) |
| F-24 | Client wants the 3D model and enclosure design (answer to P-8) |

## Working Assumptions

Ours, not the client's. Change only with Danish's agreement.

| ID | Assumption |
|---|---|
| A-1 | No LED, button or buzzer (power and sealing) |
| A-2 | We select the switch; dimensions needed only if the client supplies the enclosure |
| A-3 | Battery life is an estimate, never a guarantee |
| A-4 | Dashboard, mobile app and 3D/enclosure were requested by the client (F-22 to F-24); priced as separate items, not awarded until the quotation is accepted |
| A-5 | We send an initial proposal with an estimate for a basic version only (minimum features in device, dashboard and app), to open the discussion (promised to Uzair for tonight, 2026-10-31), stated as expected to change. After the NDA, a detailed discussion with the client, then the final quotation |
| A-6 | Primary lithium (Li-SOCl2) is the likely cell given no charging and desert heat; to be confirmed by T-02 |
| A-7 | Every uplink carries the full 16-slot state plus a counter, so a lost packet is corrected by the next one; uplinks unconfirmed, plus a daily heartbeat (battery voltage, temperature) |
| A-8 | BLE is advertising-only, slot data encrypted with an app key so only the client's app can read it (follows F-21) |
| A-9 | Enclosure internal temperature in sun is assumed 20 to 30 C above ambient, so up to about 70 C (follows F-19) |

## Team and Commercial Decisions

Danish's decisions for the proposal. Internal only; names never appear in client-facing text.

| ID | Decision |
|---|---|
| D-1 | Dashboard: Noman. Mobile app: a developer Noman arranges. Both priced as separate items |
| D-2 | 3D model and enclosure: Abdullah |
| D-3 | PCB layout: Abdullah |
| D-4 | Danish deals with the client directly and pays Uzair a 10% commission out of the price (changed 2026-10-31; previously Uzair was to add his share on top). Client price must include Uzair's share. Terms with Uzair (percentage, base, payment timing, future work) to be agreed in writing |
| D-5 | The proposal carries no company or personal name for now (we speak as "we") |
| D-6 | Prototype is delivered in running form (units, dashboard and app working end to end). The dashboard and app are also handed over as a setup package the client installs on their own accounts. Live services (hosting, monitoring, ongoing operation) are not included; if the client wants them, they are priced separately. Running costs during the prototype are paid by the client |

Still to decide: battery offer (D-size recommended, 18650 as option), prototype count, site signal test as first step, support period, prices per phase, advance and milestones, timeline, defaults for site region, quantity, app platforms, sleep-time events.

## Parked Questions

Sent to the client in drafts/Project_Discussion_16-Slot_Sensing_Unit.docx. Answers received 2026-10-31 (annotated PDF via Uzair).

| ID | Question | Status |
|---|---|---|
| P-1 | Is a delay of up to 1 minute acceptable, so close events can go in one message? | CLOSED, see F-17 |
| P-2 | What starts the daily sleep, and are events during sleep reported on wake? | PARTIAL: sleep trigger answered (F-18); reporting of events during sleep not answered |
| P-3 | Highest temperature expected at the site? | CLOSED, see F-19 |
| P-4 | After 2 years, battery replaced on site or whole unit swapped? | CLOSED, see F-20 |
| P-5 | Bluetooth data readable by any nearby phone, or only authorised phones? | CLOSED, see F-21 |
| P-6 | Dashboard required? | CLOSED, see F-22 |
| P-7 | Mobile application required? | CLOSED, see F-23 |
| P-8 | 3D model and enclosure design required? | CLOSED, see F-24 |
| P-9 | Country or region of the site (sets the LoRaWAN frequency plan, power and duty limits) | OPEN |
| P-10 | Quantity: prototypes and expected production | OPEN |
| P-11 | Where the data lands besides our dashboard, and who owns the Helium network account | OPEN |
| P-12 | Certification needed (FCC, CE) or own use only | OPEN |
| P-13 | Mobile app platforms: Android, iPhone or both | OPEN |
| P-14 | Dashboard hosting (who hosts and pays) and number of users | OPEN |

## Asked Log

Questions already sent to the client, so stations never repeat them: installation site and Helium coverage, object type, lid, events per day, Bluetooth receiver, switch arrangement, budget, NDA, plus P-1 to P-8.

---

## Tickets

### T-01 Send the discussion document
- Status: DONE
- Owner: Danish (manual)
- Depends: none
- Inputs: drafts/Project_Discussion_16-Slot_Sensing_Unit.docx
- Deliverable: document sent to Uzair for the client
- Done means: sent, with the date recorded in the handoff
- Handoff: Sent to Uzair on WhatsApp, 2026-10-31 at 02:46 PKT, as "Project Discussion_ 16-Slot Sensing Unit.docx" (10 kB). Delivered. P-1 to P-8 now wait on the client's reply through Uzair.

### T-02 Power budget and battery feasibility
- Status: REOPENED. Missing after scope update 2026-10-31: (1) standing current of the switch-sensing method T-03 chose (I2C expander with interrupt) next to strobed pull-ups and SPDT, and which one the budget uses; (2) sleep window per F-18 (after 10 pm, after several hours idle) and how sleep scanning is treated until the client answers.
- Depends: none
- Inputs: Fixed Facts, Working Assumptions
- Deliverable: docs/power-budget.md (and analysis/power_budget.py if calculations are scripted)
- Done means: average current and battery life for per-event sending vs 1-minute grouping (grouping is the design case per F-17), with events spread evenly vs in bursts, at SF7, SF9 and SF10 and at 14 and 20 dBm transmit power; standing current of each switch-sensing method (internal pull-up, strobed pull-up, SPDT switch to VDD/GND); sleep schedule per F-18; switch scanning current with strobed pull-ups; sleep current; Li-ion 18650 vs Li-SOCl2 compared at enclosure temperatures up to 70 C (A-9) including self-discharge and capacity loss, and the buffer (supercap or hybrid capacitor) a primary cell needs for TX pulses; one clear recommendation; every number marked calculated, with assumptions listed
- Handoff: 2026-10-31. Committed docs/power-budget.md and analysis/power_budget.py (all figures come from the script; nothing measured). Findings: SF decides the design. Per event at SF10 +22 dBm averages 380 uA (about 3.3 Ah a year); at SF7 93 uA. 1-minute grouping saves 0% in the worst case and about 34% fewer messages with random arrivals. Strobed scanning at 100 ms is 2.7 uA vs 3692 uA with static pull-ups. Sleep floor 7.8 uA at 25 C, 19.4 uA desert (assumed x2.5, weakest number). Li-ion 18650 loses about 62% of its charge in 2 years in desert heat with no load. Recommendation: one D-size Li-SOCl2 (ER34615, 19 Ah) with a pulse buffer, replaced on site at 2 years (F-20), 1-minute grouping as default (F-17); 4.1 years estimated at the worst case. A-6 is supported by the numbers. F-17 to F-24 arrived mid-ticket; the doc now reflects F-17, F-19 and F-20, and the desert profile (enclosure 60 to 70 C) stays as a conservative margin over the 38 C ambient in F-19. Blockers and notes for the manager: (1) The recommendation departs from F-7 (18650, max two); no 18650 option reaches 2 years at SF10, so this belongs in T-04 as a recommendation with reasons. (2) LoRaWAN region of the site is not in Fixed Facts; it sets worst-case TX power (EU868 about +14 dBm, US915 +22 dBm) and duty-cycle limits. Check whether the client already gave the site country before asking anything. (3) For T-03: a primary cell needs a pulse buffer or a spiral cell; the D cell changes enclosure size. (4) For T-05: Helium data credits at 664 uplinks a day are about USD 2.4 per unit per year (calculated, 1 DC per uplink at USD 0.00001).

### T-03 Architecture and part shortlist
- Status: REOPENED. Missing after scope update 2026-10-31: (1) the expander interrupt scheme vs T-02's strobed scanning: standing current with all 16 slots closed, and one agreed method; (2) BLE advertising with app-key encryption so only the client's app reads it (A-8, F-21); (3) Helium network server options and who owns the account and data credits.
- Depends: none
- Inputs: Fixed Facts, Working Assumptions
- Deliverable: docs/architecture.md
- Done means: block diagram; module choice (nRF52840 + SX1262 module vs alternatives) with reasons; sealed switch shortlist with actuation force suited to 200 g, comparing SPDT (no standing current) with SPST plus strobed pull-up; main board plus harness vs one long strip board for the 24 inch span; battery and holder; supercap or buffer if a primary cell is used; enclosure sealing and breather needs, including a sealed battery door and holder the client can open on site (F-20); BLE advertising with app-key encryption (A-8); Helium network server options and who would own the account; indicative BOM cost per unit with sources
- Handoff: docs/architecture.md committed 2026-10-31. Covers every "Done means" item.
  - Result: RAK4630 module; Omron D2HW pin plunger switches (0.75 N, about 2.6x margin on 200 g, calculated); SPDT wiring into a TCA6416A expander so static switch current is zero by design and no strobing is needed (strobed pull-ups kept as fallback for T-02); TPS62840 buck because the module's 3.6 V limit is below a fresh cell; D-size ER34615 + hybrid layer capacitor in a field-replaceable holder, aligned with the T-02 handoff; IP67 polycarbonate box with membrane vent; indicative BOM USD 96.07 per unit (62.07 sourced, 34.00 estimated), slot body excluded.
  - For T-02 review: SPDT wiring removes even the 2.7 uA strobed scanning current. The expander adds about 3 uA standby (TI figure), so the net change is small; worth a line in the power budget. Read only the T-02 handoff on the board, not docs/power-budget.md, to stay within inputs.
  - Blockers:
    - F-7: the D cell departs from "18650" as the client wrote it. Same point as T-02 blocker (1); one item for T-04, framed as a recommendation with reasons.
    - Helium region and so the RAK4630 variant (8XX or 9XX) is not in Fixed Facts. Same as T-02 blocker (2). "Installation site" is in the Asked Log, so check the client's earlier answer before raising anything.
    - F-2 geometry: 24 inches at a slot every 6 inches gives 4 positions along the length, while F-1 says 16 slots. Likely a 4 x 4 layout or similar. Switch arrangement is already in the Asked Log, so do not re-ask; confirm from the earlier answer. Affects harness length only, not the parts.
    - Client answers (F-17 to F-24) landed while this ticket was open; docs/architecture.md was updated to match. F-19 (38 C) drops the high-temperature cell; F-20 (on-site replacement) sets a field-replaceable cell in a gasketed battery bay; F-24 makes the slot body, actuator boots and harness route ours, to be designed after award.
    - A-2 reads "dimensions needed only if the client supplies the enclosure". With F-24 we design the enclosure, so A-2 may need rewording. Not changed here.
    - Estimated BOM lines (expander, buck, buffer, BLE antenna, vent, PCBs, misc) need quotes after award. Switch mechanical life (43,800 operations over 3 years, calculated) to be checked against the Omron datasheet.

### T-08 Service scope sheet
- Status: IN REVIEW
- Depends: none
- Inputs: Fixed Facts F-21 to F-24, Working Assumptions, Parked Questions P-13 and P-14
- Deliverable: drafts/Scope_Brief_Dashboard_and_App.docx and drafts/Scope_Brief_PCB_and_Enclosure.docx (partner briefs, replacing docs/service-scope.md)
- Done means: for dashboard, mobile app and 3D model and enclosure, each: proposed features (minimum and nice to have), platforms and hosting options with running costs, what the client must supply, what is excluded, and the open points that change the price; written so T-05 can put a fixed price on each
- Handoff: Written by the manager on Danish's direct request (2026-10-31) to get partner prices the same day. Dashboard and app brief goes to Noman; PCB and enclosure brief goes to Abdullah. Each asks for fixed prices per item, working days, assumptions and exclusions. Open items carried as assumptions: object size, site region, quantity, app platforms, user count. Prices come back to Danish, then feed T-05.

### T-09 System architecture diagram
- Status: DONE (reviewed 2026-10-31: all Done-means points met; use the PNG in the proposal)
- Depends: none
- Inputs: docs/architecture.md, docs/power-budget.md (summary and recommendation), Fixed Facts, Working Assumptions A-7 and A-8, Team decision D-6
- Deliverable: docs/diagrams/system-architecture.svg and .png (source file alongside), one picture usable in the client proposal
- Done means: shows the whole system end to end. Unit side: slot body (24 in, four 6 in sections, 4 switches each), sealed electronics bay with radio module (Bluetooth + LoRaWAN), switch reader, regulator, replaceable lithium battery with pulse buffer (cell type not fixed: two 18650-class or one D-size primary cell). Data side: LoRaWAN uplink to Helium hotspot, network server, backend and database, web dashboard; Bluetooth broadcast (encrypted, readable only by the client's app) to the mobile app. Optional items drawn dashed and labelled optional: client-owned gateway, firmware update over Bluetooth from the app, live hosting service. Labels in plain words a non-engineer can follow; no internal IDs, no people's or partner names, no prices, no long dashes; readable at A4 width and in print; PNG checked visually
- Handoff: 2026-10-31. Committed docs/diagrams/system-architecture.svg, system-architecture.png (2000 x 1443 px) and the source system-architecture.py (hand-placed SVG written by Python, PNG rendered with Playwright/Chromium; rerun the script to regenerate). Greyscale-safe (solid = included, dashed = optional, plus "(optional)" text), no part numbers, IDs, names or prices; PNG checked visually. Assumptions: the "Backend and database" and "Web dashboard" boxes are drawn as included and only the live hosting around them as optional (per D-6); the pulse buffer is shown for both cell options because the brief asked for it, though a Li-ion pair would not strictly need one. Font is Inter with Arial fallback, so the SVG may reflow slightly on machines without Inter; use the PNG in the proposal. No blockers.

### T-04 Discussion agenda
- Status: PARKED (superseded 2026-10-31: the client wants a proposal first; open points go into the proposal)
- Depends: T-01, T-02, T-03, T-08
- Inputs: client answers, docs/power-budget.md, docs/architecture.md
- Deliverable: drafts/discussion-agenda.md
- Done means: one page, at most 6 points, each tied to a parked question or a design choice; no repeated questions
- Handoff:

### T-05 Initial proposal with tentative estimate (due tonight, 2026-10-31)
- Status: BLOCKED (partner prices from Noman and Abdullah, Danish's own price and terms). Manager decision 2026-10-31 17:20: the reopened points in T-02 and T-03 are design detail and do not change a basic-version estimate, so the proposal does not wait for them
- Depends: T-08, partner prices, Danish's commercial decisions. Uses T-02 and T-03 as they stand
- Inputs: docs/power-budget.md, docs/architecture.md, docs/service-scope.md, Fixed Facts, Working Assumptions, open Parked Questions
- Deliverable: drafts/proposal.docx
- Done means: our understanding (layout per F-2 for the client to confirm); recommended design in plain terms; battery life as an estimate with its assumptions; fixed price per phase (architecture, hardware, firmware, testing) and for dashboard, mobile app and enclosure as separate items; timeline; advance plus milestones; prototype parts at actual cost; open points stated as assumptions with short questions; NDA at award; no hours times rate shown
- Handoff:

### T-06 NDA review
- Status: PARKED (client signs after accepting the proposal)
- Depends: client
- Inputs: the NDA document
- Deliverable: short review note for Danish (term, scope, IP, jurisdiction, anything unusual)
- Done means: Danish can sign or ask for changes knowing what each clause means
- Handoff:
