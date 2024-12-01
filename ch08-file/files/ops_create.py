import shutil
from pathlib import Path

base_path = Path("ops_example")

if base_path.exists() and base_path.is_dir():
    shutil.rmtree(base_path)

base_path.mkdir()
path_b = base_path / "A" / "B"
path_c = base_path / "A" / "C"
path_d = base_path / "A" / "D"
path_b.mkdir(parents=True)  # mkdir: ops_example/A/B
path_c.mkdir()  # mkdir: ops_example/A/B

for filename in ("ex1.txt", "ex2.txt", "ex3.txt"):
    with open(path_b / filename, "w", encoding="utf-8") as stream:
        stream.write(f"Some content here in {filename}\n")
shutil.move(path_b, path_d)

ex1 = path_d / "ex1.txt"
ex1.rename(ex1.parent / "ex1.rename.txt")
