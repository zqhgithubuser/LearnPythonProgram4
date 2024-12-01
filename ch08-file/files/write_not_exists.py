with open("write_x.txt", "x", encoding="utf-8") as fw:
    fw.write("Writing line 1")
with open("write_x.txt", "x", encoding="utf-8") as fw:
    fw.write("Writing line 2")  # FileExistsError: [Errno 17] File exists: 'write_x.txt'
