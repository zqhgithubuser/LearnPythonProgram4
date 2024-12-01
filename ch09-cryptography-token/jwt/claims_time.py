from datetime import datetime, timedelta, timezone
from time import sleep, time

import jwt

iat = datetime.now(tz=timezone.utc)  # iat: 签发时间
nbf = iat + timedelta(seconds=1)  # nbf: 生效时间
exp = iat + timedelta(seconds=3)  # exp: 过期时间
data = {"payload": "data", "nbf": nbf, "exp": exp, "iat": iat}


def decode(token, secret):
    print(time())
    try:
        print(jwt.decode(token, secret, algorithms=["HS256"]))
    except (jwt.ImmatureSignatureError, jwt.ExpiredSignatureError) as err:
        print(err)
        print(type(err))


secret = "secret-key"
token = jwt.encode(data, secret)
decode(token, secret)  # <class 'jwt.exceptions.ImmatureSignatureError'>
sleep(2)
decode(token, secret)  # {'payload': 'data', 'nbf': 1732787500, 'exp': 1732787502, 'iat': 1732787499}
sleep(2)
decode(token, secret)  # <class 'jwt.exceptions.ExpiredSignatureError'
