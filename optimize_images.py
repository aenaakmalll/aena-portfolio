from pathlib import Path
from PIL import Image

ROOT = Path(__file__).parent
OUTPUT = ROOT / "optimized"

# Formats we are optimizing for now
EXTENSIONS = {".jpg", ".jpeg", ".png"}

# High quality. We are NOT aggressively compressing.
QUALITY = 95

OUTPUT.mkdir(exist_ok=True)

for file in ROOT.rglob("*"):

    if file.suffix.lower() not in EXTENSIONS:
        continue

    # Don't process the optimized folder
    if OUTPUT in file.parents:
        continue

    try:
        image = Image.open(file)

        # Preserve transparency when the image has it
        if image.mode in ("RGBA", "LA"):
            image = image.convert("RGBA")
        else:
            image = image.convert("RGB")

        # Keep the same folder structure
        relative = file.relative_to(ROOT)
        output_file = OUTPUT / relative.with_suffix(".webp")

        output_file.parent.mkdir(parents=True, exist_ok=True)

        image.save(
            output_file,
            "WEBP",
            quality=QUALITY,
            method=6
        )

        old_size = file.stat().st_size / (1024 * 1024)
        new_size = output_file.stat().st_size / (1024 * 1024)

        reduction = (1 - new_size / old_size) * 100

        print(
            f"{file.name}\n"
            f"  {old_size:.2f} MB → {new_size:.2f} MB "
            f"({reduction:.1f}% smaller)\n"
        )

    except Exception as e:
        print(f"ERROR: {file}: {e}")

print("========================================")
print("DONE")
print(f"Optimized files are in: {OUTPUT}")
print("========================================")