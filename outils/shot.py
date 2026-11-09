import sys
from playwright.sync_api import sync_playwright
src, out = sys.argv[1], sys.argv[2]
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
    pg = b.new_page(viewport={"width":390,"height":844}, device_scale_factor=2)
    pg.goto("file://"+src); pg.wait_for_timeout(500)
    h = pg.evaluate("document.body.scrollHeight"); print("hauteur", h)
    pg.screenshot(path=out, full_page=True)
    b.close()
