import jwt

data = {"payload": "data"}


def encode(data, private_filename, algorithm="RS256"):
    with open(private_filename, "rb") as key:
        private_key = key.read()
    return jwt.encode(data, private_key, algorithm=algorithm)


def decode(data, pub_filename, algorithm="RS256"):
    with open(pub_filename, "rb") as key:
        public_key = key.read()
    return jwt.decode(data, public_key, algorithms=[algorithm])


token = encode(data, "rsa/id_rsa")
print(token)
data_out = decode(token, "rsa/id_rsa.pub")
print(data_out)
