from pathlib import Path

p = Path("fear.txt")
path = p.parent.absolute()
print(p.is_file())
print(path)
print(path.is_dir())
