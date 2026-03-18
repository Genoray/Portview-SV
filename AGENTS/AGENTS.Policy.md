# AGENTS.Policy.md

General policy for creating and managing IEC 62304 certification document sets for medical device software. This policy is product-independent and can be applied to any software product requiring IEC 62304 Class A/B/C compliance.

## 1. Document Set Structure

### 1.1 Required Documents (IEC 62304)

| Document Type | IEC 62304 Clause | Content Focus |
| --- | --- | --- |
| Software Validation Report | 5.8 | Validation basis, lifecycle evidence, release conclusion |
| Software Development Planning | 5.1 | Lifecycle phases, roles, deliverables, configuration management, maintenance |
| Software High Level Design | 5.3 | Architecture, decomposition, safety classification, interfaces, SOUP |
| Software Verification Plan | 5.5, 5.6 | Verification strategy, levels, acceptance criteria, environment, schedule |
| Software Verification Report | 5.7 | Executed procedures, configuration under test, results, deviations, conclusion |
| Requirement Specification (RS) | 5.2 | System-level requirements with acceptance criteria |
| Software Requirement Specification (SwSRS) | 5.2 | Software-level requirements with acceptance criteria and design allocation |
| Software Design Specification (SwSDS) | 5.4 | Detailed design per unit with I/O, algorithms, flowcharts, interfaces |
| Traceability Matrix | 5.7, 7.3 | RS -> SRS -> SDS -> procedures -> results chain |
| Unit Test Procedures (SwSTP) | 5.5 | Per-requirement test setup, steps, acceptance criteria |
| Unit Test Results (SwSTR) | 5.5 | Mirror of SwSTP with execution status per procedure |
| Integration Test Procedures (SwTP) | 5.5 | Cross-module workflow verification |
| Integration Test Results (SwTR) | 5.5 | Mirror of SwTP with execution status |
| System Test Procedures (SystemTP) | 5.6 | Product-level end-to-end verification |
| System Test Results (SystemTR) | 5.6 | Mirror of SystemTP with execution status |

### 1.2 Risk And Cybersecurity Documents

| Document Type | Standard | Content Focus |
| --- | --- | --- |
| FMEA | ISO 14971, IEC 62304 7.1 | Hazard identification, severity/occurrence scoring, risk controls, verification |
| Cybersecurity Requirements | MDCG 2019-16, AAMI TIR 57 | Cybersecurity essentials checklist, risk evaluation, maintenance plan |
| Network Security Enclosure | IEC 62304 5.6, 7.1 | Security verification test cases and results |

## 2. Document Identifier Policy

### 2.1 Naming Convention

Use product-number-based identifiers: `{Type}-{ProductNo}` or `{Type}-{ProductNo}-{seq}`

Example for product number `603`:

```
SV-603-01    Software Validation Report
SV-603-05    Software Verification Report
RS-603       Requirement Specification
SRS-603      Software Requirement Specification
SDS-603      Software Design Specification
TM-603       Traceability Matrix
STP-603      Unit Test Procedures
STR-603      Unit Test Results
TP-603       Integration Test Procedures
TR-603       Integration Test Results
SystemTP-603 System Test Procedures
SystemTR-603 System Test Results
CSRS-603     Cybersecurity Requirements
FMEA-603     Risks FMEA
NSE-603      Network Security Enclosure
```

### 2.2 File Naming

Files follow the pattern: `({ID}) {Title}.md`

### 2.3 Internal Identifiers

| Level | Prefix | Example |
| --- | --- | --- |
| System requirements | `RS-xxx` | RS-001, RS-025 |
| Software requirements | `SRS-xxx` | SRS-001, SRS-037 |
| Design items | `SDS-xxx` | SDS-001, SDS-031 |
| Unit procedures | `UTP-xxx` | UTP-001, UTP-025 |
| Integration procedures | `ITP-xxx` | ITP-001, ITP-036 |
| System procedures | `SYSP-xxx` | SYSP-001, SYSP-009 |
| FMEA items | `FMEA-xxx` | FMEA-001, FMEA-021 |

Do not use legacy identifiers from source systems as primary IDs.

## 3. Document Lifecycle

### 3.1 Status Transitions

```
Draft -> Released
```

### 3.2 Release Checklist

- [ ] Document Approval signatures completed (Prepared / Reviewed / Approved)
- [ ] Revision History present with at least initial creation entry
- [ ] All cross-references use controlled document IDs
- [ ] No legacy identifiers or migration provenance in the document body
- [ ] Acceptance criteria present for all requirements
- [ ] Design allocation column present in SwSRS
- [ ] Flowcharts present for all design items in SwSDS
- [ ] Independent reviewer recorded in all result documents
- [ ] Evidence references point to QMS controlled archive

## 4. Traceability Requirements

### 4.1 Full Traceability Chain

```
RS -> SRS -> SDS -> UTP/ITP -> STR/TR -> SYSP -> SYSTR
```

### 4.2 Coverage Gaps

When a requirement is intentionally verified at only one level, document the design decision with justification in the traceability matrix coverage notes.

## 5. Design Specification Requirements

Each design item must include:

- Input/Output table
- Mermaid flowchart diagram with error handling paths
- Sub-process descriptions where applicable
- Inter-unit interface definitions (Source, Target, Data, Trigger, Failure Handling)
- State models for complex units

## 6. Risk Management Requirements

### 6.1 FMEA Structure

Split into two tables per functional group:

- **Risk Identification**: ID, Title, Harm, Risk Control (4 columns)
- **Risk Scoring**: ID, S, O(pre), RP(pre), O(post), RP(post), Acceptable, Verification (8 columns)

### 6.2 Cybersecurity Integration

Cross-reference cybersecurity controls to FMEA items. Map each checklist item to FMEA ID, risk category, and control integration description.

## 7. Verification Documents

### 7.1 Procedure-Result Pairing

Each procedure document has a paired result document mirroring its structure.

### 7.2 Independent Verification

Record an independent reviewer in execution information. Justify single-executor throughput if applicable.

### 7.3 Evidence References

Every result document must include an Evidence References section pointing to QMS controlled archive.

## 8. PDF Export Pipeline

### 8.1 Architecture

- Markdown source -> MkDocs Material (preview) -> Playwright (PDF export)
- Cover page, Revision History, TOC generated as separate HTML pages by the export script
- Body rendered from live MkDocs serve with Mermaid injection
- All pages merged into single PDF per document via pypdf

### 8.2 Cover Page

- Report no.: document ID
- Rev.: latest revision number from Revision History
- Approval table with signature images (base64 from `sign/` folder)
- GENORAY bar at bottom

### 8.3 Header/Footer

- Header: document ID + title (right-aligned)
- Footer: page number + company name, separator with left/right margins
- Applied uniformly via Playwright `headerTemplate`/`footerTemplate`

## 9. New Product Onboarding

1. **Define product number** (e.g., `603`)
2. **Create 18 document files** with `({Type}-{ProductNo}) Title.md` naming
3. **Populate requirements** with acceptance criteria
4. **Create design specification** with per-unit flowcharts and interfaces
5. **Define procedures** at unit, integration, and system levels
6. **Build traceability matrix** covering the full chain
7. **Perform FMEA** with risk controls and pre/post scoring
8. **Execute and record results** paired with procedures
9. **Complete SV core** documents referencing the full set
10. **Release**: complete signatures, transition to Released status

## 10. Compliance Verification Checklist

| IEC 62304 Clause | Check | Document |
| --- | --- | --- |
| 5.1 | Lifecycle planning with tool validation and maintenance | SV-{prod}-02 |
| 5.2 | Requirements with acceptance criteria and design allocation | RS, SwSRS |
| 5.3 | Architecture with safety classification per unit | SV-{prod}-03 |
| 5.4 | Per-unit design with flowcharts, error handling, interfaces | SwSDS |
| 5.5 | Unit and integration procedures with paired results | SwSTP/STR, SwTP/TR |
| 5.6 | System procedures formally adopted with paired results | SystemTP/TR |
| 5.7 | Full traceability chain, approval signatures completed | TM, SV-{prod}-05 |
| 5.8 | Validation report with release conclusion | SV-{prod}-01 |
| 7.1 | FMEA with pre/post risk scores, cybersecurity integration | FMEA, CSRS |
| 7.3 | All documents Released, configuration controlled | All |
