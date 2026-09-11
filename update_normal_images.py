from pathlib import Path
import re

ROOT = Path(__file__).parent
OPTIMIZED = ROOT / "optimized"

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png"}

HTML_FILES = [
    ROOT / "index.html",
    ROOT / "shehnoor.html",
    ROOT / "zen.html",
    ROOT / "meraki.html",
    ROOT / "araish.html",
]

SRC_PATTERN = re.compile(
    r'(?P<prefix>\bsrc\s*=\s*["\'])(?P<path>[^"\']+)(?P<suffix>["\'])',
    re.IGNORECASE
)


def clean_path(path):
    if path.startswith("./"):
        return path[2:]
    return path


for html_file in HTML_FILES:

    if not html_file.exists():
        print(f"SKIPPED: {html_file.name} does not exist")
        continue

    text = html_file.read_text(encoding="utf-8")
    changes = []

    def replace_src(match):

        original_path = match.group("path")
        clean = clean_path(original_path)

        if clean.lower().startswith("optimized/"):
            return match.group(0)

        if clean.startswith(("http://", "https://", "//", "data:")):
            return match.group(0)

        extension = Path(clean).suffix.lower()

        if extension not in IMAGE_EXTENSIONS:
            return match.group(0)

        original_file = ROOT / clean

        if not original_file.exists():
            return match.group(0)

        optimized_file = OPTIMIZED / Path(clean).with_suffix(".webp")

        if not optimized_file.exists():
            return match.group(0)

        new_path = "optimized/" + Path(clean).with_suffix(".webp").as_posix()

        changes.append(
            f"{original_path}  ->  {new_path}"
        )

        return (
            match.group("prefix")
            + new_path
            + match.group("suffix")
        )

    new_text = SRC_PATTERN.sub(replace_src, text)

    if new_text != text:

        html_file.write_text(new_text, encoding="utf-8")

        print()
        print("=" * 70)
        print(f"UPDATED: {html_file.name}")
        print("=" * 70)

        for change in changes:
            print(change)

    else:
        print(f"No changes: {html_file.name}")


print()
print("=" * 70)
print("DONE")
print("=" * 70)