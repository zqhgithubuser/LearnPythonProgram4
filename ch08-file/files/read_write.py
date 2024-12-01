with open("fear.txt", encoding="utf-8") as f:
    lines = [line.rstrip() for line in f]
    print(lines)
with open("fear_copy.txt", "w", encoding="utf-8") as fw:
    fw.write("\n".join(lines))
