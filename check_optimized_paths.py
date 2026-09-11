from pathlib import Path
import re

ROOT = Path(__file__).parent
OPTIMIZED = ROOT / "optimized"

for html_file in ROOT.glob("*.html"):

    text = html_file.read_text(encoding="utf-8")

    # Find image paths in src="" and data-full=""
    matches = re.findall(
        r'(?:src|data-full)=["\']([^"\']+\.(?:jpg|jpeg|png|webp))["\']',
        text,
        flags=re.IGNORECASE
    )

    if not matches:
        continue

    print()
    print("=" * 70)
    print(html_file.name)
    print("=" * 70)

    seen = set()

    for path in matches:

        if path in seen:
            continue

        seen.add(path)

        # Ignore external URLs
        if path.startswith(("http://", "https://", "//")):
            continue

        original = ROOT / path.replace("/", "\\")

        # If it's already optimized, check it directly
        if path.lower().startswith("optimized/"):
            optimized = ROOT / path.replace("/", "\\")
        else:
            # Convert original path to expected optimized path
            relative = Path(path)
            optimized = OPTIMIZED / relative.with_suffix(".webp")

        exists_original = original.exists()
        exists_optimized = optimized.exists()

        print(f"\nReference: {path}")
        print(f"  Original exists:  {'YES' if exists_original else 'NO'}")
        print(f"  Optimized path:   {optimized.relative_to(ROOT)}")
        print(f"  Optimized exists: {'YES' if exists_optimized else 'NO'}")