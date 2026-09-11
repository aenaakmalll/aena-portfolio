from pathlib import Path

ROOT = Path(__file__).parent

files = []

for file in ROOT.rglob("*"):
    if file.is_file():
        # Ignore Git and the Python script itself
        if ".git" in file.parts:
            continue
        if file.name == "check_sizes.py":
            continue

        size_mb = file.stat().st_size / (1024 * 1024)
        files.append((size_mb, file))

files.sort(reverse=True)

print("\nLARGEST FILES IN YOUR PORTFOLIO\n")
print("-" * 70)

for size, file in files[:50]:
    print(f"{size:8.2f} MB   {file.relative_to(ROOT)}")

print("\n" + "-" * 70)
print(f"Total files: {len(files)}")
print(f"Total size: {sum(size for size, _ in files):.2f} MB")