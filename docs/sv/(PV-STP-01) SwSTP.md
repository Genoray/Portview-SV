# (PV-STP-01) SwSTP

Document ID: `PV-STP-01`  
Product: `Portview`  
Document Status: `Released`

## Document Overview

This document defines the unit-level software test procedure set for Portview.

Document notes:

- The current draft preserves the visible procedure grouping from the controlled test-procedure content.
- Execution details should remain aligned with `SV-04` and `SV-05`.

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
| `0.0` | `2024-01-17` | Initial procedure set prepared according to verification-item subdivision |
| `0.1` | `2025.07.24` | Added GUI translation test item |

## 1. Purpose

This document defines the software unit test procedures used to demonstrate that Portview software functions satisfy their verification criteria.

## 2. References

This procedure set is based primarily on:

- `SwSRS for Portview`
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

The current unit procedure set visibly covers the following items.

| Authored Procedure ID | Coverage |
| --- | --- |
| `UTP-001` | Acquire intraoral sensor image |
| `UTP-002` | Acquire image from file |
| `UTP-003` | Acquire image from TWAIN device |
| `UTP-004` | Show status of device |
| `UTP-005` | Select device |
| `UTP-006` | Main-window behavior |
| `UTP-007` | Tooth map window |
| `UTP-008` | Compare image display |
| `UTP-009` | Pan behavior |
| `UTP-010` | Zoom behavior |
| `UTP-011` | Rotate behavior |
| `UTP-012` | Thumbnail viewer |
| `UTP-013` | Print image |
| `UTP-014` | Transmit to DICOM printer |
| `UTP-015` | Export image to file |
| `UTP-016` | Export images to CD |
| `UTP-017` | Send image to DICOM server |
| `UTP-018` | FMX continuous acquisition |
| `UTP-019` | Multi-sensor selection |
| `UTP-020` | Sensor status |
| `UTP-021` | USB integrity check |
| `UTP-022` | Local-network connection check |
| `UTP-023` | Logging |
| `UTP-024` | Patient management |
| `UTP-025` | GUI translation |

### 4.1 Unit Procedure Groups

The current unit procedure coverage can be organized into stable test groups.

| Procedure Group | Included Procedures |
| --- | --- |
| Acquisition and device access | `UTP-001` to `UTP-005`, `UTP-018` to `UTP-022` |
| Viewer and image interaction | `UTP-006` to `UTP-012` |
| Output and communication | `UTP-013` to `UTP-017` |
| Administrative and support functions | `UTP-023` to `UTP-025` |

### 4.2 Relationship To Requirements

The unit procedures are expected to verify software requirements from `SwSRS for Portview`, especially:

- acquisition and source-control behavior
- viewer behavior and interaction tools
- output and communication features
- logging and localization features

### 4.3 Detailed Procedure Summaries

Each item below captures the authored procedure intent at issue level. These summaries are intended to be specific enough to support detailed procedure authoring without forcing the full step transcript into the document body.

#### 4.3.1 Acquisition And Device Access

| Authored Procedure ID | Setup | Core Procedure | Acceptance Criteria |
| --- | --- | --- | --- |
| `UTP-001` | Portview with intraoral sensor and selected patient | Select device, open patient context, acquire sensor image | Sensor image is acquired and displayed under the selected patient |
| `UTP-002` | Portview with supported image files | Invoke import, choose file, load image | Selected file is imported without issue and displayed correctly |
| `UTP-003` | Portview with TWAIN device | Invoke TWAIN acquisition, select TWAIN device, acquire image | TWAIN image is acquired and displayed correctly |
| `UTP-004` | Portview with connectable device | Observe status before and after device connection | Device status changes correctly between disconnected and connected states |
| `UTP-005` | Portview with selectable device list | Open device-selection UI and change device | Selected device becomes active and viewer state follows the selected device type |
| `UTP-018` | Portview with FMX-capable acquisition setup | Enable FMX continuous acquisition and acquire in sequence | Continuous-acquisition workflow proceeds according to the selected FMX mode |
| `UTP-019` | Portview with multiple supported sensors | Open sensor-selection control and select alternate sensor | Selected sensor becomes active and acquisition path follows the chosen device |
| `UTP-020` | Portview with supported device connection state changes | Trigger device-state transitions | Sensor or device status is shown consistently for the current connection state |
| `UTP-021` | Installation or delivery media in controlled setup | Perform integrity check on delivered USB or installation media | Integrity-check result is available and unexpected corruption is detected |
| `UTP-022` | Portview connected to local network path used by device workflow | Exercise network-dependent acquisition path | Network-based connectivity required for device workflow is available and stable |

#### 4.3.2 Viewer And Image Interaction

| Authored Procedure ID | Setup | Core Procedure | Acceptance Criteria |
| --- | --- | --- | --- |
| `UTP-006` | Portview with patient records | Open patient list, select patient, observe main viewer | Main viewer displays the selected patient mount or current image set |
| `UTP-007` | Portview with patient images and tooth-map layout | Select patient image and change location through tooth map | Display changes to the image associated with the selected tooth location |
| `UTP-008` | Portview with patient images suitable for comparison | Enable compare command, choose images, apply comparison option | Comparison view is presented for the selected images |
| `UTP-009` | Portview with displayed image | Enable panning and drag image | Image position changes according to pan interaction |
| `UTP-010` | Portview with displayed image | Enable zoom and apply drag or zoom gesture | Image zoom level changes in and out as commanded |
| `UTP-011` | Portview with displayed image | Select rotate control and apply rotation or flip option | Image rotates or flips according to selected option |
| `UTP-012` | Portview with patient image set | Open patient and observe thumbnail area | Thumbnail viewer shows available images and selection state correctly |

#### 4.3.3 Output And Communication

| Authored Procedure ID | Setup | Core Procedure | Acceptance Criteria |
| --- | --- | --- | --- |
| `UTP-013` | Portview with printable image | Invoke print command and complete print flow | Selected image is printed through the standard print path |
| `UTP-014` | Portview with configured DICOM printer | Invoke DICOM-print path and send selected image | Image is transmitted to DICOM printer without application error |
| `UTP-015` | Portview with exportable image | Choose export command, file format, and destination | Image export file is created successfully at target location |
| `UTP-016` | Portview with removable-media workflow | Invoke media export and complete target selection | Export to CD or equivalent media workflow completes successfully |
| `UTP-017` | Portview with reachable DICOM destination | Send selected image to DICOM server | DICOM transmission completes successfully or failure is detected and reported |

#### 4.3.4 Administrative And Support Functions

| Authored Procedure ID | Setup | Core Procedure | Acceptance Criteria |
| --- | --- | --- | --- |
| `UTP-023` | Portview with audit-relevant user activity | Perform representative activity and inspect log output | Activity log records expected operations without corruption |
| `UTP-024` | Portview with patient-management permissions | Add, modify, retrieve, and manage patient records | Patient-management actions succeed and data remains consistent |
| `UTP-025` | Portview with multiple enabled language resources | Change GUI language and inspect visible UI labels | GUI text changes to the selected language without layout or content corruption |

## 5. Procedure Structure

Each unit test procedure is expected to define:

- setup conditions
- ordered execution steps
- expected results
- pass or fail decision logic

### 5.1 Procedure Execution Model

Each unit procedure should be executable as a self-contained verification activity.

```mermaid
flowchart LR
    A["Setup"] --> B["Execute Procedure Steps"]
    B --> C["Observe Expected Results"]
    C --> D["Record Pass / Fail"]
    D --> E["Link To Requirement Coverage"]
```

### 5.2 Evidence Expectations

Each executed unit procedure should produce or support:

- procedure execution date
- executor identification
- configuration under test
- pass or fail status
- deviation note if expected behavior is not observed

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

- planning content in `SV-04`
- executed evidence summarized in `SV-05`
- requirement coverage linkage in the Portview traceability matrix

## 8. Open Items

- `Conditional:` Add direct links to execution records if a separate unit-level result record is maintained.
