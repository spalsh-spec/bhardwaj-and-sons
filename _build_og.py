"""Generate og-image.png for Bhardwaj & Sons social previews. 1200×630, Hermes-aesthetic."""
from PIL import Image, ImageDraw, ImageFont
import os, sys

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "og-image.png")
W, H = 1200, 630

PAPER = (243, 238, 229)
INK = (28, 22, 17)
INK_SOFT = (61, 52, 42)
INK_FAINT = (122, 111, 99)
ACCENT = (156, 74, 26)
GOLD = (157, 129, 71)
RULE = (203, 191, 168)

GARAMOND = "/System/Library/Fonts/Supplemental/Times New Roman.ttf"
GARAMOND_ITALIC = "/System/Library/Fonts/Supplemental/Times New Roman Italic.ttf"
GARAMOND_BOLD = "/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf"
SANS = "/System/Library/Fonts/Helvetica.ttc"
DEVA = "/System/Library/Fonts/Supplemental/Devanagari Sangam MN.ttc"

# Try to find a better Garamond if available
for cand in [
    "/Library/Fonts/EB Garamond/EBGaramond-Regular.ttf",
    "/System/Library/Fonts/Supplemental/Cochin.ttc",
    "/System/Library/Fonts/Supplemental/Charter.ttc",
]:
    if os.path.exists(cand):
        GARAMOND = cand
        break

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# Decorative top hairline
d.rectangle([(60, 60), (W - 60, 62)], fill=RULE)

# Top mark "Bhardwaj & Sons" small caps
mark_font = ImageFont.truetype(GARAMOND, 24)
ampersand_font = ImageFont.truetype(GARAMOND_ITALIC, 28)
mark_text = "BHARDWAJ"
amp = "&"
mark_text2 = "SONS"
# Compose the title bar
b1 = d.textbbox((0, 0), mark_text, font=mark_font)
ba = d.textbbox((0, 0), amp, font=ampersand_font)
b2 = d.textbbox((0, 0), mark_text2, font=mark_font)
total_w = (b1[2] - b1[0]) + 30 + (ba[2] - ba[0]) + 30 + (b2[2] - b2[0])
x = (W - total_w) // 2
d.text((x, 95), mark_text, font=mark_font, fill=INK)
d.text((x + (b1[2] - b1[0]) + 30, 92), amp, font=ampersand_font, fill=ACCENT)
d.text((x + (b1[2] - b1[0]) + 30 + (ba[2] - ba[0]) + 30, 95), mark_text2, font=mark_font, fill=INK)

# Hero headline
hero_font = ImageFont.truetype(GARAMOND, 96)
italic_font = ImageFont.truetype(GARAMOND_ITALIC, 96)
y = 215
line1 = "A house of"
line2 = "standards."
b = d.textbbox((0, 0), line1, font=hero_font)
d.text(((W - (b[2] - b[0])) // 2, y), line1, font=hero_font, fill=INK)
b = d.textbbox((0, 0), line2, font=italic_font)
d.text(((W - (b[2] - b[0])) // 2, y + 110), line2, font=italic_font, fill=ACCENT)

# Devanagari epigraph
deva_font = ImageFont.truetype(DEVA, 38)
deva = "सत्यमेव जयते"
b = d.textbbox((0, 0), deva, font=deva_font)
d.text(((W - (b[2] - b[0])) // 2, 460), deva, font=deva_font, fill=GOLD)

# Tagline
tag_font = ImageFont.truetype(GARAMOND_ITALIC, 22)
tag = "Methodologies, libraries, and audits for the next century of intelligent systems."
b = d.textbbox((0, 0), tag, font=tag_font)
d.text(((W - (b[2] - b[0])) // 2, 525), tag, font=tag_font, fill=INK_SOFT)

# Bottom est line
est_font = ImageFont.truetype(SANS, 14)
est = "MMXXVI · MELBOURNE · TRUST-OWNED"
b = d.textbbox((0, 0), est, font=est_font)
d.text(((W - (b[2] - b[0])) // 2, 580), est, font=est_font, fill=INK_FAINT)

img.save(OUT, "PNG", optimize=True)
print(f"wrote {OUT} ({os.path.getsize(OUT)/1024:.1f} KB)")
