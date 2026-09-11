from pathlib import Path
from PIL import Image, ImageSequence

ROOT = Path(__file__).parent
OUTPUT = ROOT / "optimized"

OUTPUT.mkdir(exist_ok=True)

gif_files = list(ROOT.rglob("*.gif"))

for file in gif_files:

    # Don't process GIFs that are already inside optimized/
    if OUTPUT in file.parents:
        continue

    try:
        image = Image.open(file)

        frames = []
        durations = []

        for frame in ImageSequence.Iterator(image):
            frames.append(frame.copy())
            durations.append(frame.info.get("duration", 100))

        relative = file.relative_to(ROOT)
        output_file = OUTPUT / relative

        # Recreate the exact same folder structure
        output_file.parent.mkdir(parents=True, exist_ok=True)

        frames[0].save(
            output_file,
            save_all=True,
            append_images=frames[1:],
            duration=durations,
            loop=image.info.get("loop", 0),
            optimize=True
        )

        old_size = file.stat().st_size / (1024 * 1024)
        new_size = output_file.stat().st_size / (1024 * 1024)

        reduction = (1 - new_size / old_size) * 100

        print(
            f"{file.name}\n"
            f"  {old_size:.2f} MB → {new_size:.2f} MB "
            f"({reduction:.1f}% smaller)\n"
            f"  → {output_file.relative_to(ROOT)}\n"
        )

    except Exception as e:
        print(f"ERROR: {file}: {e}")

print("========================================")
print("GIF OPTIMIZATION DONE")
print(f"Optimized GIFs are in: {OUTPUT}")
print("========================================")