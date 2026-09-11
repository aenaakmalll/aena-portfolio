from pathlib import Path
import imageio.v2 as imageio
import numpy as np

ROOT = Path(__file__).parent
OUTPUT = ROOT / "optimized"

OUTPUT.mkdir(exist_ok=True)

GIF_EXTENSIONS = {".gif"}

for source in ROOT.rglob("*"):

    # Only process GIFs
    if source.suffix.lower() not in GIF_EXTENSIONS:
        continue

    # Don't process anything inside optimized
    if OUTPUT in source.parents:
        continue

    # Keep original folder structure
    relative = source.relative_to(ROOT)
    output = OUTPUT / relative.with_suffix(".webm")

    output.parent.mkdir(parents=True, exist_ok=True)

    print()
    print("=" * 60)
    print(f"Converting: {source}")
    print(f"Output:     {output}")

    try:

        reader = imageio.get_reader(source)

        writer = imageio.get_writer(
            output,
            fps=15,
            codec="libvpx-vp9",
            quality=10,
            pixelformat="yuv420p",
            macro_block_size=None
        )

        frame_count = 0

        for frame in reader:

            # Convert grayscale → RGB
            if frame.ndim == 2:
                frame = np.stack([frame] * 3, axis=-1)

            # Remove alpha channel
            elif frame.shape[2] == 4:
                frame = frame[:, :, :3]

            # Make height even
            if frame.shape[0] % 2 != 0:
                frame = np.pad(
                    frame,
                    ((0, 1), (0, 0), (0, 0)),
                    mode="edge"
                )

            # Make width even
            if frame.shape[1] % 2 != 0:
                frame = np.pad(
                    frame,
                    ((0, 0), (0, 1), (0, 0)),
                    mode="edge"
                )

            writer.append_data(frame)

            frame_count += 1

            if frame_count % 20 == 0:
                print(f"  Processed {frame_count} frames...")

        writer.close()
        reader.close()

        old_size = source.stat().st_size / (1024 * 1024)
        new_size = output.stat().st_size / (1024 * 1024)

        print()
        print(f"  Frames:   {frame_count}")
        print(f"  Original: {old_size:.2f} MB")
        print(f"  WebM:     {new_size:.2f} MB")
        print(f"  Saved:    {old_size - new_size:.2f} MB")
        print("  DONE")

    except Exception as e:

        print()
        print(f"  ERROR: {source}")
        print(f"  {e}")

print()
print("=" * 60)
print("ALL GIFS PROCESSED")
print("=" * 60)