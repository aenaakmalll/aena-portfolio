from pathlib import Path
import re

ROOT = Path(__file__).parent

CSS = """
/* Sizing for converted GIF videos only */
.optimized-gif {
    display: block;
    width: 100%;
    height: auto;
    max-width: 100%;
    object-fit: contain;
}
"""

for html_file in ROOT.glob("*.html"):

    text = html_file.read_text(encoding="utf-8")

    # Find ONLY videos whose source is an optimized WebM
    pattern = r'<video(?![^>]*class=["\'][^"\']*optimized-gif)[^>]*src=["\']optimized/[^"\']+\.webm["\'][^>]*>'

    def add_class(match):
        tag = match.group(0)

        # If the video already has a class, add optimized-gif to it
        if re.search(r'\bclass=["\']', tag):
            return re.sub(
                r'(\bclass=["\'])',
                r'\1optimized-gif ',
                tag,
                count=1
            )

        # Otherwise create the class
        return tag.replace(
            "<video",
            '<video class="optimized-gif"',
            1
        )

    new_text = re.sub(
        pattern,
        add_class,
        text,
        flags=re.IGNORECASE
    )

    # Add the CSS only if this page contains converted GIF videos
    if new_text != text and ".optimized-gif {" not in new_text:

        if "</style>" in new_text:
            new_text = new_text.replace(
                "</style>",
                CSS + "\n</style>",
                1
            )

        elif "</head>" in new_text:
            new_text = new_text.replace(
                "</head>",
                f"<style>{CSS}</style>\n</head>",
                1
            )

    if new_text != text:
        html_file.write_text(
            new_text,
            encoding="utf-8"
        )

        print(f"Updated: {html_file.name}")

    else:
        print(f"No changes: {html_file.name}")


print()
print("================================")
print("DONE")
print("Only optimized GIF videos were changed.")
print("Normal images were NOT changed.")
print("================================")