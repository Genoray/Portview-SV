# AGENTS.md

## Scope

This workspace is the standalone IEC 62304 software verification document set for `Portview`.
All controlled documents are in `docs/sv/` as the single source of truth.

## Product

- Product name: `Portview`
- Product number: `603`
- Manufacturer: `GENORAY Co., Ltd.`

## Document Identity

- Treat each document as a standalone controlled document.
- Do not include provenance-style wording in the document body.
- Do not place repository rules or drafting-process guidance in the controlled document body.
- Exclude `GIX`, `IP System`, and `ImageProcess` content.

## Document Set

All documents are in `docs/sv/`. File naming: `(ID) Title.md`

| ID | File | Type |
| --- | --- | --- |
| `SV-603-01` | `(SV-603-01) Software Validation Report.md` | SV core |
| `SV-603-02` | `(SV-603-02) Software Development Planning.md` | SV core |
| `SV-603-03` | `(SV-603-03) Software High Level Design.md` | SV core |
| `SV-603-04` | `(SV-603-04) Software Verification Plan.md` | SV core |
| `SV-603-05` | `(SV-603-05) Software Verification Report.md` | SV core |
| `RS-603` | `(RS-603) RS.md` | Specification |
| `SRS-603` | `(SRS-603) SwSRS.md` | Specification |
| `SDS-603` | `(SDS-603) SwSDS.md` | Specification |
| `TM-603` | `(TM-603) Traceability Matrix.md` | Traceability |
| `STP-603` | `(STP-603) SwSTP.md` | Procedure |
| `STR-603` | `(STR-603) SwSTR.md` | Result |
| `TP-603` | `(TP-603) SwTP.md` | Procedure |
| `TR-603` | `(TR-603) SwTR.md` | Result |
| `SystemTP-603` | `(SystemTP-603) SystemTP.md` | Procedure |
| `SystemTR-603` | `(SystemTR-603) SystemTR.md` | Result |
| `CSRS-603` | `(CSRS-603) SwRS for Cybersecurity.md` | Risk |
| `FMEA-603` | `(FMEA-603) Risks FMEA.md` | Risk |
| `NSE-603` | `(NSE-603) Network Security Enclosure.md` | Verification |

## Document ID Convention

- Product number `603` is embedded in every document ID.
- SV documents with sequence: `SV-603-{seq}`
- Single documents: `{Type}-603`

## Document Header Pattern

```
# (ID) Title

Document ID: `ID`
Product: `Portview`
Document Status: `Released`
```

Followed by Document Approval (Prepared by / Reviewed by / Approved by) and Revision History.

## Internal Identifiers

| Level | Prefix |
| --- | --- |
| System requirements | `RS-xxx` |
| Software requirements | `SRS-xxx` |
| Design items | `SDS-xxx` (SDS-001 to SDS-031) |
| Unit procedures | `UTP-xxx` |
| Integration procedures | `ITP-xxx` |
| System procedures | `SYSP-xxx` |
| FMEA items | `FMEA-xxx` |

## Verification-Level Separation

- `SwSTP` (unit), `SwTP` (integration), `SystemTP` (system) are separate.
- Result documents mirror their paired procedure.

## Result Document Pairing

- `STP-603` -> `STR-603`
- `TP-603` -> `TR-603`
- `SystemTP-603` -> `SystemTR-603`

## Table Conventions

- Document Approval: Prepared by / Reviewed by / Approved by (Title, Name, Signature)
- Revision History: Rev., Date, Description (no Author column)
- Wide tables (7+ columns): split into two related tables linked by ID column.
- FMEA: Risk Identification (4 cols) + Risk Scoring (8 cols, short values)

## Markdown Rules

- Pure Markdown over embedded HTML.
- GitHub/VS Code/MkDocs compatible.
- Mermaid flowcharts for all design items, center-aligned via CSS.

## PDF Export

- Script: `py -3.11 scripts/export-pdf.py` (requires `mkdocs serve` running)
- Must run from `C:\Portview-SV` directory
- Playwright-based with Mermaid batch injection
- Cover page: title, product, Report no. (document ID), Rev. (version), approval table with signature images, GENORAY bar
- Revision History: separate page, Rev#/Description/Date/Remark (4 cols, centered headers)
- Table of Contents: separate page with dot leaders and calculated page numbers
- Header/footer on all pages via Playwright templates (separator with left/right margins)
- Signature images from `sign/` folder (11 signatories, base64 embedded)

## Signature Files

11 signature images in `sign/`:
C. H. Lee, H. J. Cho, H. S. Park, J. B. Kim, J. W. Lee, K. Y. Ro, M. C. Boo, N. Y. Choi, S. I. Choi, S. R. Lim, Y. Jeon

## Companion Files

- `AGENTS.Compliance.md` — IEC 62304 compliance actions and clause-to-document mapping
- `AGENTS.Concerns.md` — Known residual compliance concerns
- `AGENTS.Policy.md` — General certification document policy (product-independent)
