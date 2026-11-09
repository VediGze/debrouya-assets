import sys
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
    pg=b.new_page(viewport={"width":320,"height":700},device_scale_factor=2)
    pg.goto("file://"+sys.argv[1]); pg.wait_for_timeout(400)
    pg.screenshot(path=sys.argv[2],full_page=True); b.close()
