# Slot Sensor: Board

Single source of truth for the Slot Sensor brigade. Only the MANAGER chat edits Fixed Facts, Working Assumptions, Parked Questions and ticket statuses (except a station setting its own ticket to IN REVIEW).

Status values: READY, BLOCKED, IN PROGRESS, IN REVIEW, DONE, REOPENED, PARKED

---

## Fixed Facts

Stated by the client (through Uzair). Do not ask about these again.

| ID | Fact |
|---|---|
| F-1 | 16 slots, one mechanical switch per slot |
| F-2 | 24 inches long, a slot every 6 inches |
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
| F-14 | Client will sign an NDA once the project moves forward |
| F-15 | Uzair has done two PCB projects for this client; no budget shared, asked us to suggest one |
| F-16 | Danish handles hardware and firmware end to end; Uzair is not on the hardware side |
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
| A-5 | No price is quoted until after the NDA and scope discussion |
| A-6 | Primary lithium (Li-SOCl2) is the likely cell given no charging and desert heat; to be confirmed by T-02 |

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
- Status: IN REVIEW
- Depends: none
- Inputs: Fixed Facts, Working Assumptions
- Deliverable: docs/power-budget.md (and analysis/power_budget.py if calculations are scripted)
- Done means: average current and battery life for per-event sending vs 1-minute grouping, at SF7, SF9 and SF10; switch scanning current with strobed pull-ups; sleep current; Li-ion 18650 vs Li-SOCl2 compared at desert temperatures including self-discharge; one clear recommendation; every number marked calculated, with assumptions listed
- Handoff: 2026-10-31. Committed docs/power-budget.md and analysis/power_budget.py (all figures come from the script; nothing measured). Findings: SF decides the design. Per event at SF10 +22 dBm averages 380 uA (about 3.3 Ah a year); at SF7 93 uA. 1-minute grouping saves 0% in the worst case and about 34% fewer messages with random arrivals. Strobed scanning at 100 ms is 2.7 uA vs 3692 uA with static pull-ups. Sleep floor 7.8 uA at 25 C, 19.4 uA desert (assumed x2.5, weakest number). Li-ion 18650 loses about 62% of its charge in 2 years in desert heat with no load. Recommendation: one D-size Li-SOCl2 (ER34615, 19 Ah) with a pulse buffer, 4.1 years estimated at the worst case. A-6 is supported by the numbers. Blockers and notes for the manager: (1) The recommendation departs from F-7 (18650, max two); no 18650 option reaches 2 years at SF10, so this belongs in T-04 as a recommendation with reasons. (2) LoRaWAN region of the site is not in Fixed Facts; it sets worst-case TX power (EU868 about +14 dBm, US915 +22 dBm) and duty-cycle limits. Check whether the client already gave the site country before asking anything. (3) For T-03: a primary cell needs a pulse buffer or a spiral cell; the D cell changes enclosure size. (4) For T-05: Helium data credits at 664 uplinks a day are about USD 2.4 per unit per year (calculated, 1 DC per uplink at USD 0.00001).

### T-03 Architecture and part shortlist
- Status: READY
- Depends: none
- Inputs: Fixed Facts, Working Assumptions
- Deliverable: docs/architecture.md
- Done means: block diagram; module choice (nRF52840 + SX1262 module vs alternatives) with reasons; sealed switch shortlist with actuation force suited to 200 g; battery and holder; supercap or buffer if a primary cell is used; enclosure sealing and breather needs; indicative BOM cost per unit with sources
- Handoff:

### T-04 Discussion agenda
- Status: BLOCKED (T-02, T-03)
- Depends: T-01, T-02, T-03
- Inputs: client answers, docs/power-budget.md, docs/architecture.md
- Deliverable: drafts/discussion-agenda.md
- Done means: one page, at most 6 points, each tied to a parked question or a design choice; no repeated questions
- Handoff:

### T-05 Quotation
- Status: BLOCKED
- Depends: T-04 (discussion held)
- Inputs: all docs, Fixed Facts, answered Parked Questions
- Deliverable: drafts/quotation.docx
- Done means: fixed price per phase (architecture, hardware, firmware, testing) and for each optional service the client selected; timeline; advance plus milestone payments; assumptions and exclusions; prototype parts at actual cost; no hours times rate shown
- Handoff:

### T-06 NDA review
- Status: PARKED (waiting for the client's NDA)
- Depends: client
- Inputs: the NDA document
- Deliverable: short review note for Danish (term, scope, IP, jurisdiction, anything unusual)
- Done means: Danish can sign or ask for changes knowing what each clause means
- Handoff:
