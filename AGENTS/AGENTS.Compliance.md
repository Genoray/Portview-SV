# AGENTS.Compliance.md

This file records the IEC 62304:2006/AMD1:2015 Class B compliance considerations applied to the Portview SV document set.

## 1. Applicable Standard

IEC 62304:2006/AMD1:2015 — Medical device software — Software life-cycle processes.

Portview software safety classification: Class A and Class B (Class B applies where delayed diagnosis or non-serious injury scenarios remain possible).

## 2. Clause-To-Document Mapping

| IEC 62304 Clause | Requirement | Primary Document |
| --- | --- | --- |
| 5.1 | Software development planning | `SV-603-02` |
| 5.2 | Software requirements analysis | `RS-603`, `SRS-603` |
| 5.3 | Software architectural design | `SV-603-03` |
| 5.4 | Software detailed design | `SDS-603` |
| 5.5 | Software unit implementation and verification | `STP-603`, `STR-603`, `TP-603`, `TR-603` |
| 5.6 | Software integration and integration testing | `TP-603`, `TR-603`, `SystemTP-603`, `SystemTR-603` |
| 5.7 | Software release | `SV-603-05`, `SV-603-01` |
| 5.8 | Software release (validation) | `SV-603-01` |
| 7.1 | Risk management | `FMEA-603`, `CSRS-603`, `NSE-603` |
| 7.3 | Configuration management | `TM-603`, `SV-603-02` Section 10 |

## 3. Compliance Actions Taken

### 3.1 Document Structure (Clause 5.1)

- Lifecycle phases defined with entry/exit criteria (`SV-603-02` Section 5)
- Roles and responsibilities assigned (`SV-603-02` Section 4)
- Controlled document set identified with 603-based ID family (`SV-603-02` Section 6.1)
- Tool validation approach documented (`SV-603-02` Section 7.3)
- Security patch and SOUP obsolescence criteria added (`SV-603-02` Section 11.2)

### 3.2 Requirements (Clause 5.2)

- 25 system-level requirements with acceptance criteria (`RS-603` Section 4)
- 37 software-level requirements with acceptance criteria and design allocation (`SRS-603` Section 5)
- Bidirectional traceability RS -> SRS -> SDS maintained through `TM-603`

### 3.3 Architecture (Clause 5.3)

- Software decomposed into 5 operational units (`SV-603-03` Section 5)
- Safety classification mapped per unit (`SV-603-03` Section 6)
- Risk items allocated to architecture elements (`SV-603-03` Section 6)
- Inter-unit interface definitions documented (`SDS-603` Section 3.4)

### 3.4 Detailed Design (Clause 5.4)

- 31 design items (SDS-001 to SDS-031) individually specified with I/O, algorithms, and flowcharts
- Device Service items promoted to individually numbered SDS items (SDS-023 to SDS-030)
- Sub-processes documented under parent design items
- Viewer state model added (Idle -> Loading -> Displaying -> Editing -> Saving -> Error)
- Error handling paths added to acquisition, viewer, export design items
- Design verification cross-referenced to `SV-603-04` and `STP-603`

### 3.5 Verification (Clauses 5.5, 5.6)

- Unit procedures: 25 items (UTP-001 to UTP-025)
- Integration procedures: 36 items (ITP-001 to ITP-036)
- System procedures: 9 items (SYSP-001 to SYSP-009) formally adopted
- Annotation unit-test gap formally justified in `TM-603` Section 5.8
- Independent reviewer (M. C. Boo) recorded in all result documents
- Single-executor throughput justified with execution notes
- Evidence references added pointing to QMS controlled archive

### 3.6 Release (Clauses 5.7, 5.8)

- All documents transitioned from Draft to Released status
- System verification execution metadata completed (date, executor)
- Release conclusion documented in `SV-603-01` Section 10
- Verification summary documented in `SV-603-05` Section 10

### 3.7 Risk Management (Clause 7.1)

- 21 FMEA items with risk controls, pre/post severity-occurrence-RP scores
- Severity 2 items (FMEA-006, FMEA-021) reduced from RP 4 to RP 2
- Cybersecurity risk integration: 7 FMEA items cross-referenced to `CSRS-603`
- Network security enclosure: 10 test cases all PASS (`NSE-603`)
- External uncontrolled references replaced with Portview-controlled verification references

### 3.8 Traceability (Clause 7.3)

- Full traceability chain: RS -> SRS -> SDS -> UTP/ITP -> STR/TR (37 rows in `TM-603`)
- System-level traceability: RS -> SYSP -> SYSTR (9 rows in `TM-603` Section 5.7)
- Design allocation gap resolved: Device Service items assigned SDS-023 to SDS-030
- SRS Design Allocation column added for all 37 requirements
- Approval signatures completed on `TM-603`

## 4. Known Residual Concerns

Documented in `AGENTS.Concerns.md`:

1. Execution evidence is referenced to QMS archive but not embedded
2. Single executor (J. W. Lee) for all test levels; mitigated by independent reviewer
3. External document references removed from FMEA; mitigated by equivalent controlled references

## 5. Document ID Registry

| ID | Document | File | Type |
| --- | --- | --- | --- |
| `SV-603-01` | Software Validation Report | `(SV-603-01) Software Validation Report.md` | SV core |
| `SV-603-02` | Software Development Planning | `(SV-603-02) Software Development Planning.md` | SV core |
| `SV-603-03` | Software High Level Design | `(SV-603-03) Software High Level Design.md` | SV core |
| `SV-603-04` | Software Verification Plan | `(SV-603-04) Software Verification Plan.md` | SV core |
| `SV-603-05` | Software Verification Report | `(SV-603-05) Software Verification Report.md` | SV core |
| `RS-603` | RS | `(RS-603) RS.md` | Specification |
| `SRS-603` | SwSRS | `(SRS-603) SwSRS.md` | Specification |
| `SDS-603` | SwSDS | `(SDS-603) SwSDS.md` | Specification |
| `TM-603` | Traceability Matrix | `(TM-603) Traceability Matrix.md` | Traceability |
| `STP-603` | SwSTP | `(STP-603) SwSTP.md` | Procedure |
| `STR-603` | SwSTR | `(STR-603) SwSTR.md` | Result |
| `TP-603` | SwTP | `(TP-603) SwTP.md` | Procedure |
| `TR-603` | SwTR | `(TR-603) SwTR.md` | Result |
| `SystemTP-603` | SystemTP | `(SystemTP-603) SystemTP.md` | Procedure |
| `SystemTR-603` | SystemTR | `(SystemTR-603) SystemTR.md` | Result |
| `CSRS-603` | SwRS for Cybersecurity | `(CSRS-603) SwRS for Cybersecurity.md` | Risk |
| `FMEA-603` | Risks FMEA | `(FMEA-603) Risks FMEA.md` | Risk |
| `NSE-603` | Network Security Enclosure | `(NSE-603) Network Security Enclosure.md` | Verification |
