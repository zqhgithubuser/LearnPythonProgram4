import jwt

# iss: 签发者      aud: 接收者
data = {"payload": "data", "iss": "hein", "aud": "learn-python"}
secret = "secret-key"
token = jwt.encode(data, secret)


def decode(token, secret, issuer=None, audience=None):
    try:
        print(
            jwt.decode(
                token, secret, issuer=issuer, audience=audience, algorithms=["HS256"]
            )
        )
    except {jwt.InvalidIssuerError, jwt.InvalidAudienceError} as err:
        print(err)
        print(type(err))


# jwt.exceptions.InvalidAudienceError: Invalid audience
# decode(token, secret)

# {'payload': 'data', 'iss': 'hein', 'aud': 'learn-python'}
# decode(token, secret, audience='learn-python')

# jwt.exceptions.InvalidAudienceError: Invalid audience
# decode(token, secret, issuer='hein')

# jwt.exceptions.InvalidIssuerError: Invalid issuer
# decode(token, secret, issuer='wrong', audience='learn-python')

# jwt.exceptions.InvalidAudienceError: Audience doesn't match
# decode(token, secret, issuer='hein', audience='wrong')

# {'payload': 'data', 'iss': 'hein', 'aud': 'learn-python'}
decode(token, secret, issuer="hein", audience="learn-python")
