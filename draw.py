#!/usr/bin/env python3
"""Draw the news-image-20261126 entry: a newspaper front page summing up
Thursday 26 November 2026 world news. Output: entry.png (1024x1024, <1 MiB).
All facts verified 26 Nov 2026 from AP, Reuters, Investopedia, FIDE/ChessBase.
Run: python3 draw.py  (writes entry.png next to this file)"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
NAVY = (11, 31, 58)
GOLD = (232, 184, 75)
RED = (178, 34, 34)
INK = (20, 20, 20)
GREY = (90, 90, 90)
CARD = (255, 255, 255)
LINE = (200, 192, 175)

FD = "/usr/share/fonts/truetype/dejavu/"
def font(name, size):
    return ImageFont.truetype(FD + name, size)

SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

def wrap(text, fnt, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if fnt.getlength(t) <= maxw:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def text_block(x, y, lines, fnt, color, leading=None):
    lh = leading or int(fnt.size * 1.18)
    for ln in lines:
        d.text((x, y), ln, font=fnt, fill=color)
        y += lh
    return y

# ---------- masthead ----------
d.rectangle([0, 0, W, 118], fill=NAVY)
d.text((W // 2, 14), "THE WORLD IN ONE DAY", font=SERIF_B(52), fill=(255, 255, 255), anchor="ma")
d.text((W // 2, 76), "THURSDAY  26  NOVEMBER  2026", font=SANS_B(28), fill=GOLD, anchor="ma")
d.rectangle([0, 118, W, 124], fill=GOLD)

# ---------- lead story: USA / Macy's parade ----------
d.rectangle([24, 140, W - 24, 428], fill=CARD, outline=LINE, width=2)
# balloon icon (right side of lead card)
bx, by = 800, 170
d.ellipse([bx, by, bx + 150, by + 130], fill=(178, 34, 34), outline=(120, 20, 20), width=3)
d.ellipse([bx + 45, by, bx + 105, by + 130], fill=(210, 60, 60))
d.ellipse([bx + 62, by, bx + 88, by + 130], fill=(178, 34, 34))
d.line([bx + 30, by + 128, bx + 55, by + 178], fill=(90, 60, 30), width=3)
d.line([bx + 120, by + 128, bx + 95, by + 178], fill=(90, 60, 30), width=3)
d.rectangle([bx + 55, by + 178, bx + 95, by + 206], fill=(120, 85, 50), outline=(70, 45, 20), width=2)
d.text((bx + 75, 384), "100th", font=SANS_B(24), fill=NAVY, anchor="ma")

x = 48
y = 158
d.text((x, y), "UNITED STATES  ·  THANKSGIVING", font=SANS_B(22), fill=RED)
y = 192
y = text_block(x, y, wrap("Storm grounds Macy's 100th parade — first postponement ever", SERIF_B(38), 720), SERIF_B(38), INK)
y += 8
text_block(x, y, wrap("The Thanksgiving Day parade moves to Saturday as a nor'easter slams New York; the giant balloons cannot fly in the winds.", SANS(23), 720), SANS(23), GREY)

# ---------- 2x2 grid ----------
cards = [
    ("EGYPT", "Tanker fire kills at least 31 on Cairo's Ring Road",
     "A fuel truck overturns and explodes; dozens of cars charred.", "flame"),
    ("TAIWAN", "Taipei confident of keeping 15% US tariff rate",
     "After Trump's new salvo at 14 trading partners.", "bars"),
    ("MARKETS", "Nasdaq falls 2.5% as AI stocks slide",
     "Nvidia down 5%; investors flee the AI trade.", "chart"),
    ("SPORT  ·  CHESS", "Title match tied 1–1 as Game 3 begins",
     "Gukesh v Sindarov in Geneva; two draws so far.", "chess"),
]
gx, gy, cw, ch, gap = 24, 446, 478, 238, 20
for i, (kick, head, sub, icon) in enumerate(cards):
    cx = gx + (i % 2) * (cw + gap)
    cy = gy + (i // 2) * (ch + gap)
    d.rectangle([cx, cy, cx + cw, cy + ch], fill=CARD, outline=LINE, width=2)
    # icon box
    ix, iy, iw, ih = cx + 14, cy + 14, 92, 92
    d.rectangle([ix, iy, ix + iw, iy + ih], fill=(235, 230, 218), outline=LINE, width=1)
    if icon == "flame":
        d.polygon([(ix + 46, iy + 12), (ix + 78, iy + 52), (ix + 66, iy + 80), (ix + 26, iy + 80), (ix + 14, iy + 52)], fill=(230, 90, 20))
        d.polygon([(ix + 46, iy + 40), (ix + 62, iy + 62), (ix + 56, iy + 80), (ix + 36, iy + 80), (ix + 30, iy + 62)], fill=(245, 200, 40))
    elif icon == "bars":
        d.rectangle([ix + 16, iy + 52, ix + 34, iy + 80], fill=NAVY)
        d.rectangle([ix + 40, iy + 38, ix + 58, iy + 80], fill=NAVY)
        d.rectangle([ix + 64, iy + 22, ix + 82, iy + 80], fill=GOLD)
        d.text((ix + 46, iy + 2), "15%", font=SANS_B(20), fill=RED, anchor="ma")
    elif icon == "chart":
        pts = [(ix + 10, iy + 22), (ix + 30, iy + 30), (ix + 48, iy + 46), (ix + 66, iy + 56), (ix + 84, iy + 78)]
        d.line(pts, fill=RED, width=5)
        d.polygon([(ix + 84, iy + 78), (ix + 72, iy + 74), (ix + 80, iy + 64)], fill=RED)
    elif icon == "chess":
        for r in range(4):
            for c in range(4):
                col = (250, 250, 250) if (r + c) % 2 == 0 else NAVY
                d.rectangle([ix + 8 + c * 19, iy + 8 + r * 19, ix + 8 + (c + 1) * 19, iy + 8 + (r + 1) * 19], fill=col)
        d.ellipse([ix + 14, iy + 14, ix + 30, iy + 30], fill=(255, 255, 255), outline=INK, width=2)
        d.ellipse([ix + 56, iy + 56, ix + 72, iy + 72], fill=(30, 30, 30), outline=INK, width=2)
    tx = cx + 120
    d.text((tx, cy + 16), kick, font=SANS_B(19), fill=RED)
    text_block(tx, cy + 44, wrap(head, SERIF_B(27), cw - 134), SERIF_B(27), INK)
    # sub at bottom of card
    text_block(tx, cy + 168, wrap(sub, SANS(19), cw - 134), SANS(19), GREY)

# ---------- footer ----------
d.rectangle([0, 950, W, H], fill=NAVY)
d.text((W // 2, 962), "India marks Constitution Day  ·  Sources: AP · Reuters · Investopedia · FIDE",
       font=SANS(19), fill=(220, 220, 220), anchor="ma")
d.text((W // 2, 990), "make.fun — one day's news in one image",
       font=SANS(17), fill=GOLD, anchor="ma")

img.save("entry.png", "PNG", optimize=True)
print("saved entry.png", img.size)
import os
print("bytes:", os.path.getsize("entry.png"))
