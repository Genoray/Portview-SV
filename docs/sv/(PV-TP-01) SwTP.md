# (PV-TP-01) SwTP

Document ID: `PV-TP-01`  
Product: `Portview`  
Document Status: `Released`

## Document Overview

This document defines the integration-level software test procedures for Portview.

Document notes:

- The current procedure grouping reflects the integration-oriented workflow visible in the existing Portview test procedure content.
- The integration procedure is treated as `SwTP for Portview`, while the integration result record is treated as `SwTR-Z01 for Portview` in the current authored set.

## Document Approval

### Prepared by

| Title | Name | Signature |
| --- | --- | --- |
| Manager | `J. W. Lee` |  |

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
| `0.0` | `2024-01-22` | Initial procedure set prepared according to verification-item subdivision |
| `0.1` | `2025-07-24` | Added translation test plan |

## 1. Purpose

This document defines the integration test procedures used to verify Portview behavior across interacting software functions and interfaces.

## 2. References

This procedure set is based primarily on:

- `RS for Portview`
- `SV-04` Software Verification Plan

## 3. Test Information

| Field | Value |
| --- | --- |
| Tester name | `J. W. Lee` |
| Tests performed date | `2025.07.24` |
| System location | `Genoray testing platform` |
| Configuration | `Default` |
| Software baseline | `Portview 2.2.5.16` |

## 4. Procedure Coverage

The current integration procedure set visibly covers the following items.

| Authored Procedure ID | Coverage |
| --- | --- |
| `ITP-001` | System instability check |
| `ITP-002` | Patient registration |
| `ITP-003` | Modify patient information |
| `ITP-004` | Patient search |
| `ITP-005` | Delete patient information |
| `ITP-006` | Export patient information |
| `ITP-007` | Select device |
| `ITP-008` | Acquire intraoral sensor image |
| `ITP-009` | Acquire image from digital camera |
| `ITP-010` | Acquire image from file |
| `ITP-011` | Acquire image from TWAIN device |
| `ITP-012` | Show status of device |
| `ITP-013` | Main viewer |
| `ITP-014` | Thumbnail viewer |
| `ITP-015` | Compare viewer |
| `ITP-016` | Tooth map window |
| `ITP-017` | Pan behavior |
| `ITP-018` | Zoom behavior |
| `ITP-019` | Reset |
| `ITP-020` | Delete |
| `ITP-021` | Rotate |
| `ITP-022` | Text |
| `ITP-023` | Arrow |
| `ITP-024` | Pencil |
| `ITP-025` | Angle |
| `ITP-026` | Length |
| `ITP-027` | Print image |
| `ITP-028` | Print to DICOM printer |
| `ITP-029` | CD burning |
| `ITP-030` | Send image to DICOM server |
| `ITP-031` | Multi-sensor selection |
| `ITP-032` | Intraoral sensor FMX layout |
| `ITP-033` | USB integrity |
| `ITP-034` | Local-network connection check |
| `ITP-035` | Activity logging |
| `ITP-036` | GUI translation |

### 4.1 Integration Procedure Groups

The current integration procedure coverage can be organized into stable test groups.

| Procedure Group | Included Procedures |
| --- | --- |
| Patient and data workflow | `ITP-002` to `ITP-006` |
| Device acquisition workflow | `ITP-007` to `ITP-012`, `ITP-031` to `ITP-034` |
| Viewer and annotation workflow | `ITP-013` to `ITP-026` |
| Output and exchange workflow | `ITP-027` to `ITP-030` |
| Stability and support workflow | `ITP-001`, `ITP-035`, `ITP-036` |

### 4.2 Relationship To Requirements

The integration procedures are expected to verify requirement interactions that originate from `RS for Portview` and flow into the software requirement set.

The current integration set especially supports:

- end-to-end patient and image workflow
- device-to-viewer and import-to-viewer transitions
- viewer-to-output and viewer-to-communication transitions
- integrity, logging, and localization behavior across user workflow states

### 4.3 Detailed Procedure Summaries

Each item below captures the authored integration-procedure intent at issue level. The summaries focus on cross-module workflow behavior, exception handling, and end-to-end acceptance outcomes.

#### 4.3.1 Stability And Patient Workflow

| Authored Procedure ID | Setup | Core Procedure | Acceptance Criteria |
| --- | --- | --- | --- |
| `ITP-001` | Portview with representative device and patient workflow | Exercise main workflow steps, induce documented error conditions where applicable, review manual guidance and logs | Errors are detectable, diagnosable, and aligned with documented recovery guidance |
| `ITP-002` | Portview in patient-list context | Register new patient data and exercise exception cases | Valid patient data is registered successfully and invalid inputs raise the expected message |
| `ITP-003` | Portview with existing patient record | Modify patient information and exercise exception cases | Modified patient data is saved correctly and invalid operations return the expected error handling |
| `ITP-004` | Portview with searchable patient data | Search by patient identifiers and exercise search exception case | Matching patient data is retrieved correctly and failure conditions are reported properly |
| `ITP-005` | Portview with deletable patient record | Select and delete patient while avoiding active-record conflicts | Patient record is removed correctly and exception handling preserves data integrity |
| `ITP-006` | Portview with patient image data | Export patient-associated information or image data and exercise export exception | Export succeeds to selected destination and export errors are reported with the expected message |

#### 4.3.2 Device Acquisition And Source Integration

| Authored Procedure ID | Setup | Core Procedure | Acceptance Criteria |
| --- | --- | --- | --- |
| `ITP-007` | Portview with one or more supported devices | Select device from device UI | Correct acquisition window or device path becomes active |
| `ITP-008` | Portview with intraoral sensor and selected patient | Select device, open patient, acquire image | Acquired sensor image is associated with the selected patient and displayed |
| `ITP-009` | Portview with digital camera and selected patient | Select camera source and acquire image | Camera image is acquired and displayed under the active patient context |
| `ITP-010` | Portview with supported file types | Import image file into active workflow | Imported image is loaded into the integrated viewer workflow |
| `ITP-011` | Portview with TWAIN device | Invoke TWAIN import and acquire image | TWAIN image is acquired and integrated into the current workflow |
| `ITP-012` | Portview with connectable device state changes | Observe status handling before and after connection changes | Device status is reflected correctly in the integrated workflow state |
| `ITP-031` | Portview with multiple sensor options | Switch among sensors during workflow | Selected sensor is used consistently by subsequent acquisition actions |
| `ITP-032` | Portview with FMX layout workflow | Use FMX layout during acquisition sequence | FMX-related image placement and layout workflow behaves correctly |
| `ITP-033` | Installation or delivery media in integrated environment | Perform USB integrity verification before dependent workflow | Integrity issues are detected before they affect downstream workflow |
| `ITP-034` | Portview with network-dependent device path | Exercise local-network connection used by the device workflow | Network dependency is available and integrated acquisition path remains functional |

#### 4.3.3 Viewer And Annotation Workflow

| Authored Procedure ID | Setup | Core Procedure | Acceptance Criteria |
| --- | --- | --- | --- |
| `ITP-013` | Portview with patient image set | Open patient and review main viewer state | Main viewer displays correct patient image context |
| `ITP-014` | Portview with multiple patient images | Observe thumbnail area after patient selection | Thumbnail viewer remains synchronized with active image set |
| `ITP-015` | Portview with comparable images | Open comparison workflow and apply comparison options | Comparison view is shown correctly for selected images |
| `ITP-016` | Portview with tooth-map workflow | Navigate by tooth map and review image changes | Image selection follows tooth-map interaction correctly |
| `ITP-017` | Portview with displayed image | Pan displayed image | Image moves correctly while preserving workflow state |
| `ITP-018` | Portview with displayed image | Zoom in and out during active workflow | Zoom behavior is correct and image remains usable |
| `ITP-019` | Portview with modified viewer state | Use reset action after viewer manipulations | Viewer state returns to expected baseline presentation |
| `ITP-020` | Portview with deletable image or annotation context | Use delete action in permitted workflow | Target object is deleted without corrupting surrounding workflow state |
| `ITP-021` | Portview with displayed image | Rotate or flip image | Rotation or flip is correctly reflected in viewer state |
| `ITP-022` | Portview with annotation-enabled image | Add text annotation | Text annotation is created, displayed, and retained correctly |
| `ITP-023` | Portview with annotation-enabled image | Add arrow annotation | Arrow annotation is created, displayed, and retained correctly |
| `ITP-024` | Portview with annotation-enabled image | Add pencil annotation | Pencil annotation is created, displayed, and retained correctly |
| `ITP-025` | Portview with annotation-enabled image | Add angle measurement | Angle measurement is created and displayed correctly |
| `ITP-026` | Portview with annotation-enabled image | Add length measurement | Length measurement is created and displayed correctly |

#### 4.3.4 Output And Exchange Workflow

| Authored Procedure ID | Setup | Core Procedure | Acceptance Criteria |
| --- | --- | --- | --- |
| `ITP-027` | Portview with printable image | Execute standard print flow | Printed output matches selected image and no application error occurs |
| `ITP-028` | Portview with configured DICOM printer | Execute DICOM-print flow | DICOM-print request is issued correctly and printer path completes or reports failure cleanly |
| `ITP-029` | Portview with media-export destination | Execute CD or media-burning export | Output media workflow completes and selected data is exported correctly |
| `ITP-030` | Portview with reachable DICOM server | Send image through DICOM transmission path | Transmission completes or returns controlled failure handling without data mismatch |

#### 4.3.5 Logging And Localization

| Authored Procedure ID | Setup | Core Procedure | Acceptance Criteria |
| --- | --- | --- | --- |
| `ITP-035` | Portview with representative user operations | Perform integrated workflow and review logs | Log records reflect the executed workflow consistently |
| `ITP-036` | Portview with enabled language resources | Change GUI language during active workflow | Localized GUI remains coherent across integrated workflow screens |

## 5. Integration Focus

The integration procedures are intended to demonstrate that:

- patient, study, and image data remain consistent across interacting software functions
- acquisition, display, annotation, and export flows operate together as intended
- device-state and communication functions behave correctly across workflow transitions

### 5.1 Procedure Execution Model

Each integration procedure should verify behavior across at least one multi-step workflow.

```mermaid
flowchart LR
    A["Initial Configuration"] --> B["Trigger User Or Device Workflow"]
    B --> C["Observe Cross-Module Behavior"]
    C --> D["Confirm Expected Integrated Result"]
    D --> E["Record Pass / Fail And Deviations"]
```

### 5.2 Evidence Expectations

Each executed integration procedure should produce or support:

- procedure execution date
- executor identification
- configuration under test
- observed integrated behavior
- pass or fail status
- deviation note where applicable

## 6. Current Test Environment Basis

The currently visible controlled procedure content identifies:

| Environment Element | Current Basis |
| --- | --- |
| Test performer | `J. W. Lee` |
| Test date | `2025.07.24` |
| Test location | `Genoray testing platform` |
| Configuration | `Default` |
| Software under test | `Portview 2.2.5.16` |

## 7. Relationship To The SV Set

This procedure set supports:

- integration planning in `SV-04`
- integration result summarization in `SV-05`
- traceability linkage between requirements and verification evidence
