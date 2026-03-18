# (PV-SYSTP-01) SystemTP

Document ID: `PV-SYSTP-01`  
Product: `Portview`  
Document Status: `Released`


## Document Overview

This document defines the system-level verification procedures for Portview.

## Document Approval

### Prepared by

| Title | Name | Signature |
| --- | --- | --- |
| Manager | `S. R. Lim` |  |
| Staff | `J. B. Kim` |  |

### Reviewed by

| Title | Name | Signature |
| --- | --- | --- |
| General Manager | `S. I. Choi` |  |

### Approved by

| Title | Name | Signature |
| --- | --- | --- |
| CTO (Director) | `K. Y. Ro` |  |

## Revision History

| Rev. | Date | Description |
| --- | --- | --- |
| `1.5` | `2024.01.29` | Controlled system-level procedure baseline maintained with the Portview verification plan set |
| `1.6` | `2025.07.24` | Related verification-document revisions updated for the current Portview baseline |

## 1. Purpose

This document defines the system-level verification procedures used to demonstrate that the integrated Portview product baseline satisfies the applicable system-level expectations.

## 2. References

This system procedure is governed primarily by:

- `PV-SV-04` [Software Verification Plan](../sv/(PV-SV-04) Software Verification Plan.md)
- `PV-RS-01` [RS for Portview]((PV-RS-01) RS.md)
- `PV-TM-01` [Traceability Matrix]((PV-TM-01) Traceability Matrix.md)

## 3. Execution Basis

| Field | Value |
| --- | --- |
| Product under test | `Portview` |
| Software baseline | `Portview 2.2.5.16` |
| Test platform | `Genoray testing platform` |
| Configuration | `Default` |
| Verification level | `System` |

## 4. System-Level Coverage Model

The system-level procedure baseline covers verification of the integrated Portview product configuration rather than isolated software functions.

### 4.1 Scope Boundaries

| Scope Area | Coverage Intent |
| --- | --- |
| Product-baseline verification | Confirm the integrated Portview baseline behaves as intended on the controlled platform |
| System-level functional support | Confirm the supporting system-level functions are properly available |
| End-to-end behavior | Confirm the complete user-facing workflow remains acceptable at integrated system level |

### 4.2 What Stays At System Level

System-level verification should stay focused on behaviors that need the released baseline, configured environment, and full user-facing workflow.

- startup, launch, and baseline availability on the designated workstation configuration
- end-to-end patient and image workflow across multiple integrated functions
- integrated viewer behavior under representative clinical workflow sequences
- output and communication behavior in the complete product configuration
- user-visible recovery, logging, and localized interaction at product level

### 4.3 What Does Not Belong Here

The following should remain in unit or integration procedure sets and should not be repeated here as isolated low-level checks.

- single-tool annotation behavior already covered by `PV-TP-01`
- isolated import or export edge cases already covered by `PV-TP-01`
- unit-level module behavior already covered by `PV-STP-01`
- design-allocation confirmation that belongs to `PV-SDS-01` or `PV-TM-01`

## 5. System Procedure Set

The authored system procedure set should use a small number of release-oriented procedure items instead of reproducing every lower-level check.

### 5.1 Approved System Procedures

| System Procedure ID | Title | System-Level Intent |
| --- | --- | --- |
| `SYSP-001` | Product baseline startup and availability | Confirm the released Portview baseline launches and presents the expected operational context on the controlled platform |
| `SYSP-002` | End-to-end patient and acquisition workflow | Confirm patient selection, source selection, acquisition, and image presentation operate as one product workflow |
| `SYSP-003` | End-to-end viewer and diagnostic workflow | Confirm mounted-view, compare-view, tooth-map, navigation, and representative annotation workflow remain coherent at product level |
| `SYSP-004` | End-to-end output and communication workflow | Confirm print, export, media, and DICOM paths operate correctly in the full integrated baseline |
| `SYSP-005` | Device integrity and recovery workflow | Confirm device status, sensor connectivity, USB integrity, network dependence, and recovery guidance are acceptable at product level |
| `SYSP-006` | Logging and localization workflow | Confirm activity logging and multilingual GUI behavior remain acceptable in the released product workflow |
| `SYSP-007` | Installation and authorized-version acceptance | Confirm the released product baseline is installed on an acceptable workstation configuration and unsupported or unauthorized installation states are detected |
| `SYSP-008` | Operational audit and log-review workflow | Confirm representative product operations produce audit-relevant logs that support troubleshooting and review |
| `SYSP-009` | Data persistence and reopen workflow | Confirm patient and image data remain attributable, recoverable, and reusable after save, close, and reopen workflow transitions |

### 5.2 Requirement Mapping

| System Procedure ID | Primary RS Coverage |
| --- | --- |
| `SYSP-001` | `RS-001`, `RS-002` |
| `SYSP-002` | `RS-003` to `RS-009`, `RS-024` |
| `SYSP-003` | `RS-010` to `RS-014` |
| `SYSP-004` | `RS-015` to `RS-018` |
| `SYSP-005` | `RS-019`, `RS-020`, `RS-022`, `RS-023` |
| `SYSP-006` | `RS-021`, `RS-025` |
| `SYSP-007` | `RS-001`, `RS-019`, `RS-020`, `RS-023` |
| `SYSP-008` | `RS-021`, `RS-023` |
| `SYSP-009` | `RS-003`, `RS-010`, `RS-016`, `RS-024` |

### 5.3 Procedure Intent

| System Procedure ID | Setup | Core Procedure | Acceptance Criteria |
| --- | --- | --- | --- |
| `SYSP-001` | Released Portview baseline on controlled workstation configuration | Launch product, confirm baseline availability, review startup and operational context | Product launches correctly and the expected operational context is available without blocking issue |
| `SYSP-002` | Controlled patient dataset, configured device source, released baseline | Select patient, acquire image from representative source, and confirm image presentation in the integrated workflow | End-to-end acquisition workflow completes and the resulting image is associated with the correct patient context |
| `SYSP-003` | Released baseline with representative patient image set | Perform mounted-view, compare-view, tooth-map, and representative annotation workflow | Viewer workflow remains coherent and representative diagnostic actions are usable at product level |
| `SYSP-004` | Released baseline with output destinations configured | Execute representative print, export, media, and DICOM-send actions | Output and communication paths complete successfully or fail with controlled user-visible handling |
| `SYSP-005` | Released baseline with representative device and connection state transitions | Review connectivity, integrity, and recovery behavior under representative operational changes | Device-related issues are detected, communicated, and recoverable without uncontrolled behavior |
| `SYSP-006` | Released baseline with enabled logging and language resources | Execute representative workflow while reviewing logging and localized user interaction | Product logs the expected workflow activity and localized GUI behavior remains coherent |
| `SYSP-007` | Released installation package and supported workstation configuration | Install or verify the released baseline, confirm displayed version, and review unsupported or unauthorized installation conditions | The released version is identifiable, acceptable workstation conditions are met, and unsupported or unauthorized installation states are detected with controlled handling |
| `SYSP-008` | Released baseline with representative workflow activity | Execute representative clinical workflow, then review the produced operational logs for completeness and troubleshooting value | Audit-relevant workflow actions are reflected in the log set with sufficient detail to support review and problem analysis |
| `SYSP-009` | Released baseline with representative patient and image dataset | Create or open patient data, acquire or load images, save results, close the workflow, and reopen the data set | Patient and image data remain associated, recoverable, and reusable after the full save-close-reopen sequence |

## 6. Procedure Summary

The system-level verification procedure set should:

- execute the controlled integrated Portview configuration
- confirm the complete product baseline on the designated test platform
- verify representative end-to-end workflows rather than isolated low-level checks
- confirm installation, auditability, and persistence expectations that are only meaningful at released product level
- record pass, fail, or justified outcomes for the integrated system-level behavior

```mermaid
flowchart LR
    A["Controlled Portview Baseline"] --> B["System-Level Procedure Execution"]
    B --> C["Integrated Product Observation"]
    C --> D["System Result Record"]
```

## 7. Planned Evidence Output

| Procedure | Expected Output |
| --- | --- |
| `SYSP-001` to `SYSP-009` | `PV-SYSTR-01` system-level result record |
| `PV-SYSTP-01` | Controlled system procedure baseline governing `SYSP-001` to `SYSP-009` |

## 8. Traceability Use

This procedure document is intended to support:

- system-level planning references in `PV-SV-04` [Software Verification Plan](../sv/(PV-SV-04) Software Verification Plan.md)
- system-level execution summaries in `PV-SV-05` [Software Verification Report](../sv/(PV-SV-05) Software Verification Report.md)
- system-level traceability rows in `PV-TM-01` [Traceability Matrix]((PV-TM-01) Traceability Matrix.md)
