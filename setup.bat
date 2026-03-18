@echo off
echo Installing dependencies...
py -3.11 -m pip install -r requirements.txt
py -3.11 -m playwright install chromium
echo.
echo Setup complete. Run:
echo   py -3.11 -m mkdocs serve        (preview)
echo   py -3.11 scripts\export-pdf.py  (PDF export, requires serve running)
