fh = open("fear.txt", encoding="utf-8")
try:
    for line in fh:
        print(line.strip())
finally:
    fh.close()
