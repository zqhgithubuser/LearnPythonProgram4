s = "This is üŋíc0de"

encoded_s = s.encode("utf-8")
print(type(encoded_s))
print(encoded_s)

decoded_s = encoded_s.decode("utf-8")
print(type(decoded_s))
print(decoded_s)

name = "Fab"
age = 48
print(f"Hello! My name is {name} and I'm {age}")

user = "heinrich"
password = "super-secret"
print(f"Log in with: {user=} and {password=}")