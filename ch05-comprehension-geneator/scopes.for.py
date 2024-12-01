s = 0
for A in range(5):
    s += A

print(A)  # 4
print(globals())
# {'__name__': '__main__', '__doc__': None, '__package__': None,
# '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000021BBE07D7C0>,
# '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>,
# '__file__': 'F:\\python-code\\learning-python\\ch05-omprehension-geneator\\scopes.for.py', '__cached__': None,
# 's': 10, 'A': 4}
