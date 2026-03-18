# (PV-CSRS-01) SwRS for Cybersecurity

Document ID: `PV-CSRS-01`
Product: `Portview`
Document Status: `Released`

## Document Approval

### Prepared by

| Title | Name | Signature |
| --- | --- | --- |
| Manager | `S. R. Lim` |  |

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
| `0.0` | `2023-12-11` | Initial version based on requirements subdivision |
| `0.1` | `2025-07-24` | Revised in compliance with MDCG 2019-16 Rev.1 Guidance on Cybersecurity for medical devices |

## 1. Purpose

This document covers the cybersecurity risk assessment report of the intraoral imaging system named Portview in the software lifecycle process.

It contains:

- the risk analysis
- the risk assessment report
- the risk traceability matrix with testable requirements

## 2. Referenced Documents

| # | Standard No. | Standard Title |
| --- | --- | --- |
| 1 | EN ISO 13485:2016 | Medical devices - Quality management system - Requirements for regulatory purposes |
| 2 | EN ISO 14971:2019 | Medical devices - Application of risk management to medical devices |
| 3 | EN 62304:2006/A1:2015 | Medical device software - Software life-cycle processes |
| 4 | AAMI TIR 57:2016/(R)2019 | Principles for medical device security - Risk management |
| 5 | Medical Device Regulation (EU) 2017/745 | Medical Device Regulation |
| 6 | MDCG 2019-16 Rev.1 | Guidance on Cybersecurity for medical devices |

## 3. Device Description

### 3.1 Device Information

- **Product Name**: Intraoral imaging system
- **Software Name**: Portview
- **Manufacturer**: GENORAY Co., Ltd.

### 3.2 Intended Use

It is intended for use in dental applications for the scanning and processing of image data in an intraoral imaging system.

### 3.3 User Environment

It is to be used in health care facilities both inside and outside the operating room in a variety of procedures.

- Diagnosis and monitoring of dental health disease conditions

## 4. Basic Information

### 4.1 Health Data (PII)

- Patient digital image for diagnosis
- Patient ID (assigned by the program, not a social security number)
- Patient Name
- Patient Sex (optional)
- Patient Birth Date and Age (optional)

### 4.2 Functions

- **Transmission protocols**: TCP-based Private Network
- **Transport protocols**: TCP, NBT, NBF
- **Transmission data**: Structured Query Language Data, Medical Imaging Information and Related Data

### 4.3 Uses

Clinical application: Digital intraoral image acquisition workstation

### 4.4 Interchange Ways (System Requirements)

| Item | Specification |
| --- | --- |
| OS | Microsoft Windows 10 or higher (32-bit or 64-bit) |
| CPU | Core Duo / Core2 Processor |
| Memory | RAM 4 GB or more |
| VGA | Onboard chipset or more |
| Storage | 100 GB free hard disk space or more |
| Network | 100/1000 Mbps Ethernet |
| ODD | DVD-Multi |
| Graphic requirement | 32-bit color display |
| Monitor resolution | 1280 x 1024 or more |

### 4.5 Security Software

None

### 4.6 Off-The-Shelf Software

| Type | Model | Full Version | Supplier |
| --- | --- | --- | --- |
| Operating system | Microsoft Windows 10 IoT | 1809 | Microsoft Corporation |
| Toolkit | Windows SDK | 10.0.17763.0 | Microsoft Corporation |
| Toolkit | DCMTK | 3.6.7 | OFFIS |
| Development framework | Qt | 5.13 | The Qt Company |

## 5. Risk Management

### 5.1 Cybersecurity Essentials Checklist

#### Checklist Requirements

| No. | Classification | Risk Item | Requirement | Applicability |
| --- | --- | --- | --- | --- |
| 1 | Identify / Protect | Limit access to trusted users only | The software has account management system | Yes |
| 2 | Identify / Protect | Limit access to trusted users only | The software provides a means to block unauthorized network communication | Yes |
| 3 | Identify / Protect | Ensure trusted content | The system shall provide a means for users to obtain administrator approval to make software or firmware updates | Yes |
| 4 | Identify / Protect | Ensure trusted content | Use systematic procedures for authorized users to download version-identifiable software and firmware from the manufacturer | N/A |
| 5 | Identify / Protect | Ensure trusted content | The system shall ensure confidentiality and integrity by using appropriate encryption and decryption methods when exchanging medical device control information through the network | N/A |
| 6 | Identify / Protect | Ensure trusted content | It is recommended not to store personal medical information in measuring devices or gateways used outside of medical institutions | N/A |
| 7 | Detect / Respond / Recover | System logging for data auditing | The system shall provide a means to notify the user when a business process is interrupted or an error occurs | Yes |
| 8 | Detect / Respond / Recover | System logging for data auditing | The software shall provide a means to support the audit trail | Yes |
| 9 | Detect / Respond / Recover | Provide information | Manufacturers shall define countermeasures to be taken when detecting cybersecurity threats and provide relevant information to end users | N/A |
| 10 | Detect / Respond / Recover | Protect critical functionality | The systems shall implement functions that protect core information in the event of a cybersecurity breach | N/A |

#### Checklist Risk And Traceability

| No. | Risk | RS (`PV-SRS-01`) | SDS (`PV-SDS-01`) | V&V (`PV-TP-01`) |
| --- | --- | --- | --- | --- |
| 1 | PV-01, PV-02, PV-03, PV-04 | `SRS-001` to `SRS-005` | `SDS-001` | `ITP-002` to `ITP-005` |
| 2 | PV-50 | `SRS-034` | `SDS-020` | `ITP-034` |
| 3 | PV-51 | `SRS-001` | `SDS-001` | `ITP-036` |
| 4 | Remote installer download is not supported | — | — | — |
| 5 | P2P-only; secure transmission guaranteed | — | — | — |
| 6 | PV-50; private networks only | — | — | — |
| 7 | PV-01, PV-02, PV-03, PV-04 | `SRS-001` to `SRS-005` | `SDS-001` | `ITP-002` to `ITP-005` |
| 8 | PV-52 | `SRS-035` | `SDS-021` | `ITP-035` |
| 9 | P2P-only; secure transmission guaranteed | — | — | — |
| 10 | P2P-only; secure transmission guaranteed | — | — | — |

### 5.2 Identification Of Cybersecurity Risk

Refer to Clause 12, Risk Analysis Table (FMEA) in the Risk Management Report. See also `FMEA-Z01` Portview Risks FMEA.

### 5.3 Cybersecurity Risk Evaluation

Refer to Clause 12, Risk Analysis Table (FMEA) in the Risk Management Report. See also `FMEA-Z01` Portview Risks FMEA.

### 5.4 Cybersecurity Risk Control

Refer to Clause 12, Risk Analysis Table (FMEA) in the Risk Management Report. See also `FMEA-Z01` Portview Risks FMEA.

### 5.5 Risk Control Verification

See section 5.1 Cybersecurity Essentials Checklist in this document and Clause 12, Risk Analysis Table (FMEA) in the Risk Management Report. See also `FMEA-Z01` Portview Risks FMEA.

### 5.6 Risk/Benefit Analysis

Refer to Clause 12, Risk Analysis Table (FMEA) in the Risk Management Report. See also `FMEA-Z01` Portview Risks FMEA.

### 5.7 Overall Residual Risk Evaluation

Overall residual risk is re-evaluated after the cybersecurity risk controls have been applied.

Refer to Clause 12, Risk Analysis Table (FMEA) in the Risk Management Report. See also `FMEA-Z01` Portview Risks FMEA.

## 6. Maintenance Plan

Computer systems require regular maintenance in order to continue running smoothly and with proper security. Each vendor (or user) will be informed about maintenance and security via email.

A help desk team will start supporting users right away to take care of their immediate needs. The team will contact vendors (or users) for security patches if a critical threat to system operation is found.

The maintenance planning activities are performed in the software validation maintenance process in accordance with IEC 62304:2015. Refer to `PV-SV-02` Section 11 for the full maintenance and problem-resolution process.

### 6.1 Security Patch Priority And Deployment

| Priority | Criteria | Deployment Timeline |
| --- | --- | --- |
| Critical | Confirmed exploitable vulnerability affecting patient data, system availability, or regulatory compliance | Immediate; expedited change-control and verification |
| High | Confirmed vulnerability with limited exploit potential or indirect patient-safety impact | Within 30 days through expedited change-control |
| Normal | Advisory or preventive update without confirmed exploit | Next scheduled release cycle |

Security patches follow the change-control and verification process defined in `PV-SV-02` Section 11.2. SOUP components (Windows SDK, DCMTK, Qt) are monitored for end-of-life advisories and patched according to the same priority scheme.
