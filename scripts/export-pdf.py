"""
Export MkDocs pages to PDF via Playwright.
Requires: mkdocs serve running on localhost:8000
Usage: py -3.11 scripts/export-pdf.py
"""

import asyncio
import re
import sys
from pathlib import Path
from urllib.parse import quote

OUTPUT_DIR = Path("output/pdf-export")
BASE_URL = "http://127.0.0.1:8000"
DOCS_DIR = Path("docs/sv")

PAGES = [
    "(PV-SV-01) Software Validation Report",
    "(PV-SV-02) Software Development Planning",
    "(PV-SV-03) Software High Level Design",
    "(PV-SV-04) Software Verification Plan",
    "(PV-SV-05) Software Verification Report",
    "(PV-RS-01) RS",
    "(PV-SRS-01) SwSRS",
    "(PV-SDS-01) SwSDS",
    "(PV-TM-01) Traceability Matrix",
    "(PV-STP-01) SwSTP",
    "(PV-STR-01) SwSTR",
    "(PV-TP-01) SwTP",
    "(PV-TR-01) SwTR",
    "(PV-SYSTP-01) SystemTP",
    "(PV-SYSTR-01) SystemTR",
    "(PV-CSRS-01) SwRS for Cybersecurity",
    "(FMEA-Z01) Risks FMEA",
    "(NSE-Z01) Network Security Enclosure",
]


def extract_mermaid_blocks(name):
    """Extract mermaid code blocks from the source markdown."""
    md_path = DOCS_DIR / f"{name}.md"
    if not md_path.exists():
        return []
    text = md_path.read_text(encoding="utf-8")
    return re.findall(r"```mermaid\s*\n(.*?)```", text, re.DOTALL)


async def export_page(browser, name):
    """Navigate to a page, inject mermaid, and print to PDF."""
    url_path = f"sv/{quote(name, safe='()')}/"
    url = f"{BASE_URL}/{url_path}"
    mermaid_blocks = extract_mermaid_blocks(name)

    page = await browser.new_page()
    try:
        await page.goto(url, wait_until="networkidle", timeout=30000)
        await asyncio.sleep(1)

        if mermaid_blocks:
            # Inject mermaid source and render in batches to avoid overload
            batch_size = 10
            total = min(len(mermaid_blocks), 100)
            for start in range(0, total, batch_size):
                end = min(start + batch_size, total)
                batch = mermaid_blocks[start:end]
                await page.evaluate("""
                    async ([blocks, startIdx]) => {
                        const divs = document.querySelectorAll('.mermaid');
                        for (let i = 0; i < blocks.length; i++) {
                            const idx = startIdx + i;
                            if (idx < divs.length && !divs[idx].querySelector('svg')) {
                                divs[idx].textContent = blocks[i];
                            }
                        }
                        if (typeof mermaid !== 'undefined') {
                            try {
                                await mermaid.run({ querySelector: '.mermaid' });
                            } catch (e) {}
                        }
                    }
                """, [batch, start])
                await asyncio.sleep(1)
            await asyncio.sleep(1)

        # Hide nav elements for clean PDF
        await page.evaluate("""
            () => {
                ['.md-header', '.md-tabs', '.md-sidebar', '.md-search',
                 '.md-footer', '.md-top', '.md-source'].forEach(s => {
                    document.querySelectorAll(s).forEach(el => el.style.display = 'none');
                });
                const c = document.querySelector('.md-content__inner');
                if (c) {
                    c.style.maxWidth = 'none';
                    c.style.boxShadow = 'none';
                    c.style.background = '#fff';
                    c.style.borderRadius = '0';
                }
                const main = document.querySelector('.md-main__inner');
                if (main) main.style.marginTop = '0';
            }
        """)

        pdf_path = OUTPUT_DIR / f"{name}.pdf"
        await page.pdf(
            path=str(pdf_path),
            format="A4",
            margin={"top": "10mm", "right": "10mm", "bottom": "10mm", "left": "10mm"},
            print_background=True,
        )
        svg_count = await page.evaluate("document.querySelectorAll('.mermaid svg').length")
        print(f"  OK: {name}.pdf ({svg_count} diagrams)")

    except Exception as e:
        print(f"  FAIL: {name} - {e}", file=sys.stderr)
    finally:
        await page.close()


async def main():
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        print("Run: pip install playwright && py -3.11 -m playwright install chromium")
        sys.exit(1)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Exporting {len(PAGES)} documents to {OUTPUT_DIR}/\n")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        for name in PAGES:
            await export_page(browser, name)
        await browser.close()

    count = len(list(OUTPUT_DIR.glob("*.pdf")))
    print(f"\nDone. {count} PDFs in {OUTPUT_DIR}/")


if __name__ == "__main__":
    asyncio.run(main())
