import hashlib

# print(hashlib.algorithms_available)
# print(hashlib.algorithms_guaranteed)

h = hashlib.blake2b()
h.update(b"Hash me")
h.update(b" now!")
# 十六进制
print(h.hexdigest())
# 字节表示
print(h.digest())
print(h.block_size)  # 128
# 摘要大小（字节）
print(h.digest_size)  # 64
print(h.name)  # blake2b

# sha256
print(hashlib.sha256(b"Hash me now!").hexdigest())
print(hashlib.sha256(b"Hash me now!").digest_size)  # 32


h1 = hashlib.blake2b(b"Important data", digest_size=16, person=b"part-1")
h2 = hashlib.blake2b(b"Important data", digest_size=16, person=b"part-2")
h3 = hashlib.blake2b(b"Important data", digest_size=16)
print(h1.hexdigest())
print(h2.hexdigest())
print(h3.hexdigest())

import os

dk = hashlib.pbkdf2_hmac(
    "sha256", b"Password123", salt=os.urandom(16), iterations=100000
)

print(dk.hex())
