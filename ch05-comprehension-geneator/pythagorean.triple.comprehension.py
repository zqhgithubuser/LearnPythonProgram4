from math import sqrt

mx = 10
triples = [
    (a, b, sqrt(a * a + b * b))
    for a in range(1, mx)
    for b in range(a, mx)
]
# print(triples)
# filter out all non-Pythagorean triples
triples = [(a, b, int(c)) for a, b, c in triples if c.is_integer()]
print(triples)  # [(3, 4, 5), (6, 8, 10)]
