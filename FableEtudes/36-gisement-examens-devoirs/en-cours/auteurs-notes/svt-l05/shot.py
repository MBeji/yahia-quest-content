import sys
from playwright.sync_api import sync_playwright
src,dst=sys.argv[1:3]
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':760,'height':700},device_scale_factor=2)
    pg.goto('file://'+src); pg.screenshot(path=dst,full_page=True); b.close()
