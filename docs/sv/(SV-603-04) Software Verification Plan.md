# (SV-603-04) Software Verification Plan

Document ID: `SV-603-04`  
Product: `Portview`  
Document Status: `Released`


## Document Approval

### Prepared by

| Title | Name | Signature |
| --- | --- | --- |
| Manager | `S. R. Lim` |  |
| Staff | `J. B. Kim` |  |
| General Manager | `S. I. Choi` |  |

### Reviewed by

| Title | Name | Signature |
| --- | --- | --- |
| Manager | `M. C. Boo` |  |

### Approved by

| Title | Name | Signature |
| --- | --- | --- |
| CTO (Director) | `K. Y. Ro` |  |

## Revision History

| Rev. | Date | Description |
| --- | --- | --- |
| `0.0` | `2012.03.07` | Initial Version |
| `0.1` | `2015.01.12` | User Interface Update |
| `0.2` | `2016.01.19` | New Function Implemented |
| `0.3` | `2017.01.13` | System Issue |
| `0.4` | `2018.01.12` | New Device Added |
| `0.5` | `2019.01.21` | Device Compatibility |
| `0.6` | `2020.01.30` | Device Compatibility |
| `0.7` | `2020.10.08` | GUI update |
| `0.8` | `2021.02.26` | Linkage usability improve |
| `0.9` | `2021.09.10` | Program Issue |
| `1.0` | `2021.10.08` | Device Compatibility |
| `1.1` | `2022.03.04` | Connection status improve |
| `1.2` | `2023.01.04` | Increasing image capacity |
| `1.3` | `2023.04.21` | Device Compatibility |
| `1.4` | `2024.01.08` | Device Compatibility |
| `1.5` | `2024.01.29` | Document number changed from 603 to Z01 according to OP-709 |
| `1.6` | `2025.07.24` | Revision numbers of related software validation documents updated |

## 1. Purpose

This document defines the software verification plan used to demonstrate that the applicable Portview software functions satisfy their verification and validation criteria.

The plan is intended to:

- define the verification approach for the covered product baseline
- identify the inputs, procedures, and environments used for verification
- define the acceptance logic for unit, integration, and system verification evidence

## 2. Scope

This plan covers the verification effort for the Portview software set.

In scope:

- software requirement verification for Portview
- interface and integration verification for the Portview software interfaces referenced in the RS inputs
- execution of the planned unit, integration, and system-level procedures

The current plan identifies software version `2.2.5.16` and the default Genoray testing platform as the principal baseline references. Software version `2.2.5.16` is associated with the `2024-10-02` release update for Windows 11 and GenX-CR compatibility.

## 3. Referenced Documents

The following references govern this plan for the current release baseline.

| Reference | Use |
| --- | --- |
| Medical Device Regulation (EU) 2017/745 | Regulatory framework |
| Quality management systems - Requirements | Quality-system reference |
| EN ISO 13485:2016 Medical devices Quality management systems | Governing quality management standard |
| ISO 12052:2006 DICOM including workflow and data management | Governing interoperability standard |
| IEC 62304:2006/AMD1:2015 Software lifecycle processes | Governing software lifecycle standard |
| Guidance for the Content of Premarket Submissions for Software Contained in Medical Devices | Regulatory guidance |
| General Principles of Software Validation Final Guidance for Industry and FDA Staff | Regulatory guidance |
| Software and Medical Devices (VdTUV, 2001) | External guidance reference |
| QM Quality System Documentation | Internal quality reference |
| QM Design Control Procedure | Internal process reference |
| QM Software Development Procedure | Internal process reference |
| QM Corrective and Preventive Actions | Internal process reference |
| QM Document Control | Internal process reference |
| `SV-603-01` Software Validation Report | Validation basis and release conclusion |
| `SV-603-02` Software Development Planning | Lifecycle and configuration-management context |
| `SV-603-03` Software High Level Design | Architecture and decomposition reference |
| `SV-603-05` Software Verification Report | Companion verification result report |
| `RS-603` RS for Portview | System-level requirement input |
| `SRS-603` SwSRS for Portview | Software requirement input |
| `SDS-603` SwSDS for Portview | Software design input |
| `TM-603` Traceability Matrix | Requirement and design traceability reference |
| `STP-603` SwSTP for Portview | Unit verification procedure |
| `TP-603` SwTP for Portview | Integration verification procedure |

## 4. Verification Objectives

The verification effort should demonstrate the following:

- the applicable Portview software requirements are verified by controlled procedures and recorded evidence
- the integrated behavior between Portview software components and interfaces is verified
- the planned verification procedures are defined clearly enough to support repeatable execution
- the final verification evidence can support a release or approval decision through an explicit pass or justified-fail logic

## 5. Verification Strategy

Verification is organized by level. The plan is structured around unit verification, integration testing, and system testing, with the procedure set serving as the primary evidence backbone.

### 5.1 Test Levels

The plan preserves the principal verification levels and document pairings.

| Level | Goal | Primary Inputs | Primary Outputs |
| --- | --- | --- | --- |
| Unit | Verify requirement-level behavior of Portview software units | `SRS-603` SwSRS for Portview | `STP-603` SwSTP for Portview |
| Integration | Verify integrated behavior against RS-level interface requirements | `RS-603` RS for Portview | `TP-603` SwTP for Portview |
| System | Verify system-level behavior on the controlled product baseline | System-level specifications and integrated configuration | `SystemTP-Z01` |

### 5.2 Verification Methods

Planned methods include:

- code review before unit-level verification
- execution of controlled unit-level procedures against the designated Portview requirement inputs
- integration testing against RS-derived interface requirements
- system testing using `SystemTP-Z01`
- review of execution results and final release decision through the verification report

### 5.3 Acceptance Criteria

All procedures referenced by this plan shall be executed, and the final status of each required result shall be either:

- `Passed`, or
- `Justified` when a failure or deviation is accepted through formal review and documented disposition

The final verification report should not claim successful completion unless this rule is met.

## 6. Verification Environment

The currently available information identifies assigned personnel and the core execution platform. Additional configuration detail can be appended if it is maintained as a separate controlled record.

### 6.1 Hardware And Devices

| Item | Identifier | Revision | Notes |
| --- | --- | --- | --- |
| Product under test | `Portview` | `Software baseline 2.2.5.16` | Release dated `2024-10-02`; Windows 11 and GenX-CR compatibility update |
| System test platform | `Genoray testing platform` | `Configuration: Default` | System procedure identifier is `SystemTP-Z01` |
| Integration interfaces | `Portview configuration` | `Serial/prototype number: -` | Hardware and network details remain to be expanded if controlled separately |

### 6.2 Software And Tools

| Tool | Version | Purpose | Validation Status |
| --- | --- | --- | --- |
| `SRS-603` SwSRS for Portview | `Rev 1.6` | Unit-level requirement input | `Released` |
| `STP-603` SwSTP for Portview | `Rev 0.1` | Unit-level test procedure | `Released` |
| `RS-603` RS for Portview | `Rev 0.1` | Integration requirement input | `Released` |
| `TP-603` SwTP for Portview | `Rev 0.1` | Integration test procedure | `Released` |
| `SystemTP-603` SystemTP-Z01 | `Rev 1.6` | System-level test procedure | `Released` |
| Microsoft Visual C++ 2017 | `Professional Edition` | Build environment | `Validated per SV-603-02 Section 7.3` |
| Genoray testing platform | `Default configuration` | Test execution environment | `Validated per SV-603-02 Section 7.3` |

### 6.3 Roles And Responsibilities

| Role | Responsibility | Owner |
| --- | --- | --- |
| Software Team Manager | Verification oversight for Portview software activities | `S.I. Choi` |
| Software Engineer | Execution and support for software verification tasks | `S.R. Lim` |
| Software Engineer | Execution and support for software verification tasks | `J.W. Lee` |

## 7. Verification Items

The verification items below follow the planning structure used in this document and keep the verification scope aligned with the defined procedure set.

| Item ID | Description | Source Requirement / Design Input | Verification Level |
| --- | --- | --- | --- |
| `UNIT-PORTVIEW` | Portview unit verification | `SRS-603` SwSRS for Portview / All Sections | `Unit` |
| `INT-PORTVIEW` | Portview integration verification | `RS-603` RS for Portview / Section 2.1 Software Requirements | `Integration` |
| `SYS-PORTVIEW` | Portview system verification | `System-level integrated baseline` | `System` |

The verification items above are tied to the following planned procedure set:

| Verification Item | Planned Procedure | Notes |
| --- | --- | --- |
| Portview unit verification | `STP-603` SwSTP for Portview / All Sections | Code review is completed before this verification |
| Portview integration verification | `TP-603` SwTP for Portview / All Sections | `RS-603` RS for Portview Section 2.1 Software Requirements is used as the input |
| Portview system verification | `SystemTP-603` [SystemTP-Z01]((SystemTP-603) SystemTP.md) | System testing is conducted with `SystemTP-Z01` |

If finer-grained requirement grouping is needed, it should be maintained in a separate traceability annex instead of replacing the planning structure in this section.

## 8. Procedures And Evidence

The following procedure set forms the execution baseline for this plan.

| Procedure ID | Title | Evidence Output | Owner |
| --- | --- | --- | --- |
| `STP-603` | SwSTP for Portview | Unit-level Portview execution records | `Software team` |
| `TP-603` | SwTP for Portview | Integration execution records for Portview interfaces | `Software team` |
| `SystemTP-603` | [SystemTP-Z01]((SystemTP-603) SystemTP.md) | System-level execution records | `System verification owner` |

## 9. Schedule And Entry/Exit Criteria

This repository does not yet contain an active execution schedule. Until that information is added, the following gate logic should apply:

- entry: approved baseline, approved procedures, available test environment, assigned personnel
- exit: required procedures executed, deviations dispositioned, verification report updated, release decision prepared

## 10. Deviations And Risk Handling

Any failed, blocked, or partially executed procedure shall be recorded with:

- the affected item or procedure identifier
- the observed problem
- the impact on safety, effectiveness, or release confidence
- the disposition owner
- the justification or remediation plan

Deviations should not be embedded solely in narrative text. The report set should maintain them in a dedicated table.

## 11. Traceability Strategy

Traceability will be maintained from requirement inputs to procedures, and from procedures to execution evidence and final summary claims.

```mermaid
flowchart LR
    R["Requirements"] --> P["Verification procedures"]
    P --> E["Execution evidence"]
    E --> S["Verification summary"]
```

Traceability rules:

- each procedure should name its controlling requirement or document section
- each executed record should reference the procedure identifier and baseline
- the verification report should summarize status by verification level and unresolved deviation status
