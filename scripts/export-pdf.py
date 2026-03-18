"""
Export MkDocs pages to PDF with cover, revision history, TOC (with page numbers), and body.
All pages include header (document name) and footer (page number + company name).
Requires: mkdocs serve running on localhost:8000
Usage: py -3.11 scripts/export-pdf.py
"""

import asyncio
import base64
import re
import sys
import tempfile
from pathlib import Path
from urllib.parse import quote

from pypdf import PdfReader, PdfWriter

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "output" / "pdf-export"
DOCS_DIR = PROJECT_ROOT / "docs" / "sv"
BASE_URL = "http://127.0.0.1:8000"

PAGES = [
    "(SV-603-01) Software Validation Report",
    "(SV-603-02) Software Development Planning",
    "(SV-603-03) Software High Level Design",
    "(SV-603-04) Software Verification Plan",
    "(SV-603-05) Software Verification Report",
    "(RS-603) RS",
    "(SRS-603) SwSRS",
    "(SDS-603) SwSDS",
    "(TM-603) Traceability Matrix",
    "(STP-603) SwSTP",
    "(STR-603) SwSTR",
    "(TP-603) SwTP",
    "(TR-603) SwTR",
    "(SystemTP-603) SystemTP",
    "(SystemTR-603) SystemTR",
    "(CSRS-603) SwRS for Cybersecurity",
    "(FMEA-603) Risks FMEA",
    "(NSE-603) Network Security Enclosure",
]

BODY_MARGIN = {"top": "18mm", "right": "10mm", "bottom": "20mm", "left": "10mm"}
PAGE_HEIGHT_PX = 1016
FRONT_PAGES = 3

SIGN_DIR = PROJECT_ROOT / "sign"
FRONT_MARGIN = {"top": "18mm", "right": "10mm", "bottom": "20mm", "left": "10mm"}


def load_sign_base64(name):
    """Load a signature image as base64 data URI. Returns empty string if not found."""
    path = SIGN_DIR / f"{name}.png"
    if path.exists():
        b64 = base64.b64encode(path.read_bytes()).decode()
        return f'<img src="data:image/png;base64,{b64}" style="height:28px;max-width:90px;object-fit:contain">'
    return ""

COMMON_STYLE = """
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: 'Segoe UI', Arial, sans-serif; margin: 0; padding: 10px 20px 10px 20px; color: #222; }
"""


def make_header_template(header_text):
    """Playwright headerTemplate for body pages."""
    return f'''<div style="width:100%;font-size:9px;color:#888;text-align:right;padding-right:20px;padding-top:4px">
        {header_text}
    </div>'''


def make_footer_template():
    """Playwright footerTemplate for body pages."""
    return '''<div style="width:100%;font-size:8px;color:#888;padding:0 40px">
        <div style="border-top:1px solid #ccc;padding-top:4px;display:flex;justify-content:space-between">
            <span><span class="pageNumber"></span> | Page</span>
            <span>GENORAY Co., Ltd.</span>
        </div>
    </div>'''


# ── Metadata parsing ──

def parse_metadata(name):
    md_path = DOCS_DIR / f"{name}.md"
    if not md_path.exists():
        return None
    text = md_path.read_text(encoding="utf-8")

    doc_id = (re.search(r"Document ID: `(.+?)`", text) or type('', (), {'group': lambda s, n: name})()).group(1)
    title = (re.search(r"^# \(.+?\) (.+)$", text, re.MULTILINE) or type('', (), {'group': lambda s, n: name})()).group(1)
    product = (re.search(r"Product: `(.+?)`", text) or type('', (), {'group': lambda s, n: "Portview"})()).group(1)
    status = (re.search(r"Document Status: `(.+?)`", text) or type('', (), {'group': lambda s, n: "Released"})()).group(1)
    # Extract version from Revision History section only
    rev_section = re.search(r"## Revision History\n\n\|.*?\n\|.*?\n((?:\|.*?\n)*)", text)
    if rev_section:
        rev_rows = re.findall(r"\| `(.+?)` \| `(.+?)` \|", rev_section.group(1))
        version = rev_rows[-1][0] if rev_rows else "0.0"
    else:
        version = "0.0"

    return {
        "doc_id": doc_id, "title": title, "product": product,
        "status": status, "version": version,
        "approval_rows": extract_approval_rows(text),
        "revision_rows": extract_revision_rows(text),
        "toc_entries": extract_toc_entries(text),
        "mermaid_blocks": re.findall(r"```mermaid\s*\n(.*?)```", text, re.DOTALL),
    }


def extract_approval_rows(text):
    rows = []
    for role in ["Prepared by", "Reviewed by", "Approved by"]:
        label = role.replace(" by", "")
        m = re.search(rf"### {role}\n\n\|.*?\n\|.*?\n((?:\|.*?\n)*)", text)
        if m:
            first = True
            for line in m.group(1).strip().split("\n"):
                cells = [c.strip().replace("`", "") for c in line.split("|")[1:-1]]
                if len(cells) >= 2:
                    rows.append({"by": label if first else "", "title": cells[0], "name": cells[1]})
                    first = False
    return rows


def extract_revision_rows(text):
    m = re.search(r"## Revision History\n\n\|.*?\n\|.*?\n((?:\|.*?\n)*)", text)
    if not m:
        return []
    rows = []
    for line in m.group(1).strip().split("\n"):
        cells = [c.strip().replace("`", "") for c in line.split("|")[1:-1]]
        if len(cells) >= 3:
            rows.append({"rev": cells[0], "desc": cells[2], "date": cells[1]})
    return rows


def extract_toc_entries(text):
    entries = []
    for m in re.finditer(r"^(#{2,4}) (\d.*)$", text, re.MULTILINE):
        level = len(m.group(1))
        title = m.group(2).strip()
        if "Document" in title or "Revision" in title or "Open Items" in title:
            continue
        anchor = re.sub(r"[^\w\s-]", "", title.lower())
        anchor = re.sub(r"[\s]+", "-", anchor).strip("-")
        entries.append({"level": level, "title": title, "anchor": anchor, "page": 0})
    return entries


# ── HTML generators ──

def make_cover_html(meta, header_text):
    approval_html = build_approval_table(meta["approval_rows"])
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
    {COMMON_STYLE}
    .doc-title {{ font-size: 18px; font-weight: bold; border-bottom: 2px solid #222; padding-bottom: 8px; margin-top: 20px; }}
    .product {{ font-size: 32px; font-weight: bold; text-align: center; margin-top: 80px; }}
    .subtitle {{ font-size: 20px; font-weight: normal; text-align: center; margin-top: 8px; color: #444; }}
    .report-info {{ text-align: center; font-size: 12px; margin-top: 20px; color: #444; line-height: 1.8; }}
    .approval {{ margin-top: 50px; }}
    .approval table {{ width: 80%; margin: 0 auto; border-collapse: collapse; }}
    .approval th {{ padding: 6px 12px; border: 1px solid #ccc; background: #f5f5f5; font-size: 11px; text-align: center; }}
    .genoray-bar {{ position: absolute; bottom: 60px; left: 40px; right: 40px;
                    background: #e8e8e8; text-align: center; padding: 8px; font-size: 13px; font-weight: bold; color: #333; }}
    </style></head><body>
    <div class="doc-title">{meta['doc_id']} {meta['title']}</div>
    <div class="product">{meta['product']}</div>
    <div class="subtitle">{meta['title']}</div>
    <div class="report-info">Report no. : {meta['doc_id']}<br>Rev. : {meta['version']}</div>
    <div class="approval"><table>
    <tr><th>By</th><th>Title</th><th>Name</th><th>Sign</th></tr>
    {approval_html}</table></div>
    <div class="genoray-bar">GENORAY Co., Ltd.</div>
    </body></html>"""


def build_approval_table(rows):
    role_counts = {}
    for r in rows:
        if r["by"]:
            role_counts[r["by"]] = role_counts.get(r["by"], 0)
        last_role = r["by"] if r["by"] else list(role_counts.keys())[-1] if role_counts else ""
        role_counts[last_role] = role_counts.get(last_role, 0) + 1

    html = ""
    used = set()
    for r in rows:
        by_td = ""
        if r["by"] and r["by"] not in used:
            cnt = role_counts.get(r["by"], 1)
            by_td = f'<td rowspan="{cnt}" style="padding:8px 12px;border:1px solid #ccc;text-align:center;vertical-align:middle;font-size:11px">{r["by"]}</td>'
            used.add(r["by"])
        sign_img = load_sign_base64(r["name"])
        html += f'<tr>{by_td}<td style="padding:8px 12px;border:1px solid #ccc;text-align:center;font-size:11px">{r["title"]}</td><td style="padding:8px 12px;border:1px solid #ccc;text-align:center;font-size:11px">{r["name"]}</td><td style="padding:8px 12px;border:1px solid #ccc;width:100px;text-align:center">{sign_img}</td></tr>'
    return html


def make_revision_html(meta, header_text):
    rows = "".join(
        f'<tr><td style="padding:5px 8px;border:1px solid #ccc;text-align:center;font-size:11px">{r["rev"]}</td>'
        f'<td style="padding:5px 8px;border:1px solid #ccc;font-size:11px">{r["desc"]}</td>'
        f'<td style="padding:5px 8px;border:1px solid #ccc;text-align:center;font-size:11px">{r["date"]}</td>'
        f'<td style="padding:5px 8px;border:1px solid #ccc;font-size:11px"></td></tr>'
        for r in meta["revision_rows"]
    )
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
    {COMMON_STYLE}
    h2 {{ text-align: center; font-size: 18px; margin: 30px 0 20px; }}
    table {{ width: 100%; border-collapse: collapse; }}
    th {{ padding: 6px 8px; border: 1px solid #ccc; background: #f5f5f5; font-size: 11px; text-align: center; }}
    </style></head><body>
    <h2>Revision History</h2>
    <table><tr><th>Rev#</th><th>Description</th><th>Date</th><th>Remark</th></tr>{rows}</table>
    </body></html>"""


def make_toc_html(meta, header_text):
    entries = "".join(
        f'<div style="display:flex;align-items:baseline;margin-left:{({2:0,3:30,4:60}).get(e["level"],0)}px;padding:3px 0;font-size:12px">'
        f'<span>{e["title"]}</span>'
        f'<span style="flex:1;border-bottom:1px dotted #aaa;margin:0 8px;min-width:20px"></span>'
        f'<span style="min-width:20px;text-align:right">{e["page"] if e["page"]>0 else ""}</span></div>'
        for e in meta["toc_entries"]
    )
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
    {COMMON_STYLE}
    h2 {{ text-align: center; font-size: 20px; font-weight: bold; margin: 30px 0 20px; }}
    </style></head><body>
    <h2>Table of Contents</h2>
    {entries}
    </body></html>"""


# ── Rendering ──

async def render_html_to_pdf(page, html, path, header_text=""):
    await page.set_content(html, wait_until="networkidle")
    await page.pdf(
        path=str(path), format="A4",
        margin=FRONT_MARGIN,
        print_background=True,
        display_header_footer=True,
        header_template=make_header_template(header_text),
        footer_template=make_footer_template(),
    )


async def prepare_body_page(page, url, mermaid_blocks):
    await page.goto(url, wait_until="networkidle", timeout=30000)
    await asyncio.sleep(1)

    if mermaid_blocks:
        for start in range(0, min(len(mermaid_blocks), 100), 10):
            batch = mermaid_blocks[start:start+10]
            await page.evaluate("""
                async ([blocks, startIdx]) => {
                    const divs = document.querySelectorAll('.mermaid');
                    for (let i = 0; i < blocks.length; i++) {
                        const idx = startIdx + i;
                        if (idx < divs.length && !divs[idx].querySelector('svg'))
                            divs[idx].textContent = blocks[i];
                    }
                    if (typeof mermaid !== 'undefined')
                        try { await mermaid.run({ querySelector: '.mermaid' }); } catch (e) {}
                }
            """, [batch, start])
            await asyncio.sleep(1)
        await asyncio.sleep(1)

    await page.evaluate("""
        () => {
            // Hide all MkDocs chrome
            ['.md-header','.md-tabs','.md-sidebar','.md-sidebar--primary',
             '.md-sidebar--secondary','.md-search','.md-footer','.md-top',
             '.md-source','.md-nav'].forEach(s => {
                document.querySelectorAll(s).forEach(el => el.style.display = 'none');
            });

            // Hide Document Approval / Revision History sections
            document.querySelectorAll('h2').forEach(h => {
                const t = h.textContent.trim();
                if (t.includes('Document Approval') || t.includes('Revision History')) {
                    let el = h;
                    while (el) {
                        el.style.display = 'none';
                        el = el.nextElementSibling;
                        if (el && el.tagName === 'H2' && !el.textContent.includes('Document Approval') && !el.textContent.includes('Revision History')) break;
                    }
                    h.style.display = 'none';
                }
            });

            // Hide Document ID / Product / Status meta block
            document.querySelectorAll('.md-content__inner > p').forEach(p => {
                const t = p.textContent;
                if (t.includes('Document ID:') || t.includes('Product:') || t.includes('GENORAY'))
                    p.style.display = 'none';
            });

            // Hide h1 title (on cover page)
            const h1 = document.querySelector('.md-content__inner h1');
            if (h1) h1.style.display = 'none';

            // Clean up content styling
            const c = document.querySelector('.md-content__inner');
            if (c) { c.style.maxWidth='none'; c.style.boxShadow='none'; c.style.background='#fff'; c.style.borderRadius='0'; c.style.padding='0 10px'; }
            const main = document.querySelector('.md-main__inner');
            if (main) { main.style.marginTop='0'; main.style.padding='0'; }
            document.querySelectorAll('.md-grid').forEach(g => g.style.maxWidth='none');
        }
    """)


async def get_heading_pages(page, toc_entries):
    anchors = [e["anchor"] for e in toc_entries]
    positions = await page.evaluate("""
        (anchors) => anchors.map(a => {
            const el = document.getElementById(a);
            return el ? el.getBoundingClientRect().top + window.scrollY : -1;
        })
    """, anchors)
    for i, pos in enumerate(positions):
        toc_entries[i]["page"] = (FRONT_PAGES + 1 + int(pos / PAGE_HEIGHT_PX)) if pos >= 0 else 0
    return toc_entries


async def export_page(browser, name, tmp_dir):
    meta = parse_metadata(name)
    if not meta:
        print(f"  FAIL: {name}", file=sys.stderr)
        return

    header_text = f"{meta['doc_id']} {meta['title']}"
    url = f"{BASE_URL}/sv/{quote(name, safe='()')}/"

    cover_path = tmp_dir / f"{name}_cover.pdf"
    revision_path = tmp_dir / f"{name}_revision.pdf"
    toc_path = tmp_dir / f"{name}_toc.pdf"
    body_path = tmp_dir / f"{name}_body.pdf"
    final_path = OUTPUT_DIR / f"{name}.pdf"

    # 1. Cover + Revision
    p = await browser.new_page()
    try:
        await render_html_to_pdf(p, make_cover_html(meta, header_text), cover_path, header_text)
        await render_html_to_pdf(p, make_revision_html(meta, header_text), revision_path, header_text)
    finally:
        await p.close()

    # 2. Body (render first to get heading positions)
    bp = await browser.new_page()
    try:
        await prepare_body_page(bp, url, meta["mermaid_blocks"])
        if meta["toc_entries"]:
            meta["toc_entries"] = await get_heading_pages(bp, meta["toc_entries"])
        svg_count = await bp.evaluate("document.querySelectorAll('.mermaid svg').length")

        # Body PDF with header/footer on every page
        await bp.pdf(
            path=str(body_path),
            format="A4",
            margin=BODY_MARGIN,
            print_background=True,
            display_header_footer=True,
            header_template=make_header_template(header_text),
            footer_template=make_footer_template(),
        )
    finally:
        await bp.close()

    # 3. TOC (after body, so page numbers are known)
    if meta["toc_entries"]:
        tp = await browser.new_page()
        try:
            await render_html_to_pdf(tp, make_toc_html(meta, header_text), toc_path, header_text)
        finally:
            await tp.close()

    # 4. Merge
    parts = [cover_path, revision_path]
    if meta["toc_entries"] and toc_path.exists():
        parts.append(toc_path)
    parts.append(body_path)
    merge_pdfs(parts, final_path)
    print(f"  OK: {name}.pdf ({svg_count} diagrams)")


def merge_pdfs(parts, output_path):
    writer = PdfWriter()
    for part in parts:
        if part.exists():
            for p in PdfReader(str(part)).pages:
                writer.add_page(p)
    with open(output_path, "wb") as f:
        writer.write(f)


async def main():
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        print("Run: pip install playwright pypdf && py -3.11 -m playwright install chromium")
        sys.exit(1)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Exporting {len(PAGES)} documents to {OUTPUT_DIR}/\n")
    tmp_dir = Path(tempfile.mkdtemp())

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        for name in PAGES:
            await export_page(browser, name, tmp_dir)
        await browser.close()

    print(f"\nDone. {len(list(OUTPUT_DIR.glob('*.pdf')))} PDFs in {OUTPUT_DIR}/")


if __name__ == "__main__":
    asyncio.run(main())
