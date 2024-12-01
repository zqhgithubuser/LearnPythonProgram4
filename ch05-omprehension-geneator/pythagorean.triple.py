from math import sqrt

mx = 10
triples = [
    (a, b, sqrt(a * a + b * b))
    for a in range(1, mx)
    for b in range(a, mx)
]
# print(triples)
# filter out all non-Pythagorean triples
triples = list(
    filter(lambda triple: triple[2].is_integer(), triples)
)
print(triples)  # [(3, 4, 5.0), (6, 8, 10.0)]

triples = list(
    map(lambda triple: triple[:2] + (int(triple[2]),), triples)
)
print(triples)  # [(3, 4, 5), (6, 8, 10)]
