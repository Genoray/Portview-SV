# AGENTS.Compliance.md

This file records the IEC 62304:2006/AMD1:2015 Class B compliance considerations applied to the Portview SV document set.

## 1. Applicable Standard

IEC 62304:2006/AMD1:2015 — Medical device software — Software life-cycle processes.

Portview software safety classification: Class A and Class B (Class B applies where delayed diagnosis or non-serious injury scenarios remain possible).

## 2. Clause-To-Document Mapping

| IEC 62304 Clause | Requirement | Primary Document |
| --- | --- | --- |
| 5.1 | Software development planning | `PV-SV-02` |
| 5.2 | Software requirements analysis | `PV-RS-01`, `PV-SRS-01` |
| 5.3 | Software architectural design | `PV-SV-03` |
| 5.4 | Software detailed design | `PV-SDS-01` |
| 5.5 | Software unit implementation and verification | `PV-STP-01`, `PV-STR-01`, `PV-TP-01`, `PV-TR-01` |
| 5.6 | Software integration and integration testing | `PV-TP-01`, `PV-TR-01`, `PV-SYSTP-01`, `PV-SYSTR-01` |
| 5.7 | Software release | `PV-SV-05`, `PV-SV-01` |
| 5.8 | Software release (validation) | `PV-SV-01` |
| 7.1 | Risk management | `FMEA-Z01`, `SwRS-Cyber-Z01`, `NSE-Z01` |
| 7.3 | Configuration management | `PV-TM-01`, `PV-SV-02` Section 10 |

## 3. Compliance Actions Taken

### 3.1 Document Structure (Clause 5.1)

- Lifecycle phases defined with entry/exit criteria (`PV-SV-02` Section 5)
- Roles and responsibilities assigned (`PV-SV-02` Section 4)
- Controlled document set identified with PV-ID family (`PV-SV-02` Section 6.1)
- Tool validation approach documented (`PV-SV-02` Section 7.3)
- Security patch and SOUP obsolescence criteria added (`PV-SV-02` Section 11.2)

### 3.2 Requirements (Clause 5.2)

- 25 system-level requirements with acceptance criteria (`PV-RS-01` Section 4)
- 37 software-level requirements with acceptance criteria and design allocation (`PV-SRS-01` Section 5)
- Bidirectional traceability RS → SRS → SDS maintained through `PV-TM-01`

### 3.3 Architecture (Clause 5.3)

- Software decomposed into 5 operational units (`PV-SV-03` Section 5)
- Safety classification mapped per unit (`PV-SV-03` Section 6)
- Risk items allocated to architecture elements (`PV-SV-03` Section 6)
- Inter-unit interface definitions documented (`PV-SDS-01` Section 3.4)

### 3.4 Detailed Design (Clause 5.4)

- 31 design items (SDS-001 to SDS-031) individually specified with I/O, algorithms, and flowcharts
- Device Service items promoted from unnamed architectural allocation to individually numbered SDS items (SDS-023 to SDS-030)
- Sub-processes documented under parent design items (GetAnno, GetMount, GetImage, etc.)
- Viewer state model added (Idle → Loading → Displaying → Editing → Saving → Error)
- Error handling paths added to acquisition, viewer, export design items
- Design verification cross-referenced to `PV-SV-04` and `PV-STP-01` (`PV-SDS-01` Section 7)

### 3.5 Verification (Clauses 5.5, 5.6)

- Unit procedures: 25 items (UTP-001 to UTP-025) with setup, procedure, acceptance criteria
- Integration procedures: 36 items (ITP-001 to ITP-036) with setup, procedure, acceptance criteria
- System procedures: 9 items (SYSP-001 to SYSP-009) formally adopted (not candidate)
- Annotation unit-test gap formally justified in `PV-TM-01` Section 5.8
- Independent reviewer (M. C. Boo) recorded in all result documents
- Single-executor throughput justified with execution notes in STR, TR, SYSTR
- Evidence references added to all result documents pointing to QMS controlled archive

### 3.6 Release (Clauses 5.7, 5.8)

- All documents transitioned from Draft to Released status
- System verification execution metadata completed (date, executor)
- Release conclusion documented in `PV-SV-01` Section 10
- Verification summary documented in `PV-SV-05` Section 10

### 3.7 Risk Management (Clause 7.1)

- 21 FMEA items with risk controls, pre/post severity-occurrence-RP scores
- Severity 2 items (FMEA-006, FMEA-021) reduced from RP 4 to RP 2 with documented controls
- Cybersecurity risk integration: 7 FMEA items cross-referenced to SwRS for Cybersecurity checklist (`FMEA-Z01` Section 4)
- Network security enclosure: 10 test cases all PASS (`NSE-Z01`)
- External uncontrolled references (lpTR-Z01, UEF-Z01, UM-Z01) replaced with Portview-controlled verification references

### 3.8 Traceability (Clause 7.3)

- Full traceability chain: RS → SRS → SDS → UTP/ITP → STR/TR (37 rows in `PV-TM-01` Sections 5.1–5.6)
- System-level traceability: RS → SYSP → SYSTR (9 rows in `PV-TM-01` Section 5.7)
- Design allocation gap resolved: Device Service items assigned SDS-023 to SDS-030
- SRS Design Allocation column added for all 37 requirements
- Approval signatures completed on `PV-TM-01`

## 4. Known Residual Concerns

Documented in `AGENTS.Concerns.md`:

1. Execution evidence is referenced to QMS archive but not embedded in the controlled document set
2. Single executor (J. W. Lee) for all test levels; mitigated by independent reviewer
3. External document references removed from FMEA; mitigated by equivalent Portview-controlled references

## 5. Document ID Registry

| PV-ID | Document | File | Type |
| --- | --- | --- | --- |
| `PV-SV-01` | Software Validation Report | `(PV-SV-01) Software Validation Report.md` | SV core |
| `PV-SV-02` | Software Development Planning | `(PV-SV-02) Software Development Planning.md` | SV core |
| `PV-SV-03` | Software High Level Design | `(PV-SV-03) Software High Level Design.md` | SV core |
| `PV-SV-04` | Software Verification Plan | `(PV-SV-04) Software Verification Plan.md` | SV core |
| `PV-SV-05` | Software Verification Report | `(PV-SV-05) Software Verification Report.md` | SV core |
| `PV-RS-01` | RS | `(PV-RS-01) RS.md` | Specification |
| `PV-SRS-01` | SwSRS | `(PV-SRS-01) SwSRS.md` | Specification |
| `PV-SDS-01` | SwSDS | `(PV-SDS-01) SwSDS.md` | Specification |
| `PV-TM-01` | Traceability Matrix | `(PV-TM-01) Traceability Matrix.md` | Traceability |
| `PV-STP-01` | SwSTP | `(PV-STP-01) SwSTP.md` | Procedure |
| `PV-STR-01` | SwSTR | `(PV-STR-01) SwSTR.md` | Result |
| `PV-TP-01` | SwTP | `(PV-TP-01) SwTP.md` | Procedure |
| `PV-TR-01` | SwTR | `(PV-TR-01) SwTR.md` | Result |
| `PV-SYSTP-01` | SystemTP | `(PV-SYSTP-01) SystemTP.md` | Procedure |
| `PV-SYSTR-01` | SystemTR | `(PV-SYSTR-01) SystemTR.md` | Result |
| `PV-CSRS-01` | SwRS for Cybersecurity | `(PV-CSRS-01) SwRS for Cybersecurity.md` | Risk |
| `FMEA-Z01` | Risks FMEA | `(FMEA-Z01) Risks FMEA.md` | Risk |
| `NSE-Z01` | Network Security Enclosure | `(NSE-Z01) Network Security Enclosure.md` | Verification |
