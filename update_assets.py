from pathlib import Path

ROOT = Path(__file__).parent

# --------------------------------------------------
# EXACT GIF REPLACEMENTS USED BY YOUR WEBSITE
# --------------------------------------------------

replacements = {

    # index.html
    "1Churri.gif": "optimized/1Churri.webm",
    "Bahar.gif": "optimized/Bahar.webm",

    # shehnoor.html
    "Made in pakistan.gif": "optimized/Made in pakistan.webm",

    # meraki.html
    "./meraki-graphics/meraki eid newsletter.gif":
        "optimized/meraki-graphics/meraki eid newsletter.webm",

    "./meraki-graphics/Newsletter compressed.gif":
        "optimized/meraki-graphics/Newsletter compressed.webm",

    "meraki-graphics/gif1.gif":
        "optimized/meraki-graphics/gif1.webm",

    "meraki-graphics/gif2.gif":
        "optimized/meraki-graphics/gif2.webm",
}


# --------------------------------------------------
# 1. INDEX.HTML
# --------------------------------------------------

file = ROOT / "index.html"

text = file.read_text(encoding="utf-8")

text = text.replace(
    '<img src="1Churri.gif" alt="ShehNoor newsletter 1">',
    '<video src="optimized/1Churri.webm" alt="ShehNoor newsletter 1" autoplay muted loop playsinline></video>'
)

text = text.replace(
    '<img src="Bahar.gif" alt="ShehNoor newsletter 3">',
    '<video src="optimized/Bahar.webm" alt="ShehNoor newsletter 3" autoplay muted loop playsinline></video>'
)

file.write_text(text, encoding="utf-8")

print("Updated index.html")


# --------------------------------------------------
# 2. SHEHNOOR.HTML
# --------------------------------------------------

file = ROOT / "shehnoor.html"

text = file.read_text(encoding="utf-8")

text = text.replace(
    '<img src="Bahar.gif" alt="ShehNoor newsletter 1">',
    '<video src="optimized/Bahar.webm" autoplay muted loop playsinline></video>'
)

text = text.replace(
    '<img src="Made in pakistan.gif" alt="ShehNoor newsletter 3">',
    '<video src="optimized/Made in pakistan.webm" autoplay muted loop playsinline></video>'
)

file.write_text(text, encoding="utf-8")

print("Updated shehnoor.html")


# --------------------------------------------------
# 3. MERAKI.HTML
# --------------------------------------------------

file = ROOT / "meraki.html"

text = file.read_text(encoding="utf-8")

text = text.replace(
    '<img src="./meraki-graphics/meraki eid newsletter.gif" alt="Newsletter 1">',
    '<video src="optimized/meraki-graphics/meraki eid newsletter.webm" autoplay muted loop playsinline></video>'
)

text = text.replace(
    '<img src="./meraki-graphics/Newsletter compressed.gif" alt="Newsletter 2">',
    '<video src="optimized/meraki-graphics/Newsletter compressed.webm" autoplay muted loop playsinline></video>'
)

text = text.replace(
    '<img src="meraki-graphics/gif1.gif" alt="GIF 1">',
    '<video src="optimized/meraki-graphics/gif1.webm" autoplay muted loop playsinline></video>'
)

text = text.replace(
    '<img src="meraki-graphics/gif2.gif" alt="GIF 2">',
    '<video src="optimized/meraki-graphics/gif2.webm" autoplay muted loop playsinline></video>'
)

# Change the existing GIF image CSS to video CSS
text = text.replace(
    ".gif-item img { width: 100%; height: auto; display: block; }",
    ".gif-item img, .gif-item video { width: 100%; height: auto; display: block; }"
)

file.write_text(text, encoding="utf-8")

print("Updated meraki.html")


# --------------------------------------------------
# DONE
# --------------------------------------------------

print()
print("=" * 50)
print("GIF OPTIMIZATION REFERENCES UPDATED")
print("=" * 50)
print()
print("Original GIF files were NOT deleted.")
print("Optimized files are being loaded from /optimized/")
print()