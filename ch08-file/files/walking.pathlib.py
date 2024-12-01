from pathlib import Path

p = Path(".")
for root, dirs, files in p.walk():
    print(f"{root=}")
    if dirs:
        print("Directories:")
        for dir_ in dirs:
            print(dir_)
        print()
    if files:
        print("File:")
        for filename in files:
            print(filename)
        print("#############################")
