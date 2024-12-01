import base64
import json


with open('images.json', encoding='utf-8') as f:
    data = json.loads(f.read())

for name, bs64val in data.items():
    with open(name, "wb") as f:
        f.write(base64.b64decode(bs64val))
