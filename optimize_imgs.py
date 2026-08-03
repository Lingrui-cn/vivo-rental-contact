import os
from PIL import Image

Q = {
    "qr-full.webp":        (640, 95, None),
    "tutorial-guide.webp": (680, 85, 45),
    "bottom-hero.webp":    (840, 85, 45),
    "lens35mm-full.webp":  (840, 85, 45),
    "lens85mm-full.webp":  (840, 85, 45),
    "lens14mm-full.webp":  (840, 85, 45),
    "lens-group.avif":     (840, 85, 45),
}

def save_webp(im, path, q):
    im.save(path, "WEBP", quality=q, method=6)

def save_avif(im, path, q):
    im.save(path, "AVIF", quality=q)

for src, (w, wq, aq) in Q.items():
    if not os.path.exists(src):
        print("MISS", src); continue
    im = Image.open(src).convert("RGB")
    h = round(w * im.height / im.width)
    im = im.resize((w, h), Image.LANCZOS)
    base, ext = os.path.splitext(src)
    out = base + ".webp"
    save_webp(im, out, wq)
    print(f"{out:28} {w}x{h}  {os.path.getsize(out)/1024:7.1f}K  webp q{wq}")
    if aq:
        out = base + ".avif"
        save_avif(im, out, aq)
        print(f"{out:28} {w}x{h}  {os.path.getsize(out)/1024:7.1f}K  avif q{aq}")
