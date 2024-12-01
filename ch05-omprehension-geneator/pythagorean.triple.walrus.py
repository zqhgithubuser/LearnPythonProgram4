from math import sqrt

mx = 10
triples = [
    (a, b, int(c))
    for a in range(1, mx)
    for b in range(a, mx)
    if (c := sqrt(a * a + b * b)).is_integer()
]
print(triples)
