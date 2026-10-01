#!/usr/bin/env python3
# usage: zoom.py <id> <page> <x0> <y0> <x1> <y1> [scale] -> writes render/zoom-<id>-p<page>-<x0>-<y0>.png (coords in 150-dpi pixels)
import sys, os
from PIL import Image
SP = "/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad/gisement/9eme-sciences-vie-terre"
id_, page = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0
im = Image.open(f"{SP}/render/{id_}-{page}.png").convert("RGB")
box = (max(0, x0), max(0, y0), min(im.width, x1), min(im.height, y1))
c = im.crop(box)
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
out = f"{SP}/render/zoom-{id_}-p{page}-{x0}-{y0}.png"
c.save(out)
print(out, c.size)
