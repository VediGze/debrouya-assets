"""Aperçu PDF d'une édition : python3 apercu.py NNN-LearnyBox.html NNN-apercu.pdf (une seule longue page, largeur téléphone)."""
import sys, os
from playwright.sync_api import sync_playwright
src, out = os.path.abspath(sys.argv[1]), sys.argv[2]
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": 430, "height": 900})
    pg.emulate_media(media="screen"); pg.goto("file://" + src); pg.wait_for_load_state("networkidle"); pg.wait_for_timeout(500)
    h = pg.evaluate("document.body.scrollHeight")
    pg.pdf(path=out, width="430px", height=f"{h+60}px", print_background=True, margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
    b.close()
print("ok", h)
