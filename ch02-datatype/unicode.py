s = "This is üŋíc0de"

print(type(s))

encoded_s = s.encode("utf-8")
print(encoded_s)

print(type(encoded_s))

print(encoded_s.decode("utf-8"))
