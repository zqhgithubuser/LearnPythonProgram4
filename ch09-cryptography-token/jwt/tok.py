import jwt

data = {"payload": "data", "id": 123456789}
token = jwt.encode(data, "secret-key")
print(token)
algo = ["HS256", "HS512"]
data_out = jwt.decode(token, "secret-key", algo)
print(data_out)  # {'payload': 'data', 'id': 123456789}

token512 = jwt.encode(data, "secret-key", algorithm="HS512")
print(token512)
data_out = jwt.decode(token512, "secret-key", algorithms="HS512")
print(data_out)  # 'payload': 'data', 'id': 123456789}
