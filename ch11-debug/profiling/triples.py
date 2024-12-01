def calc_triples(mx):
    triples = []
    for a in range(1, mx + 1):
        for b in range(a, mx + 1):
            hypotenuse = calc_hypotenuse(a, b)
            if is_int(hypotenuse):
                triples.append((a, b, int(hypotenuse)))
    return triples


# def calc_hypotenuse(a, b):
#     return (a**2 + b**2) ** .5
def calc_hypotenuse(a, b):
    return (a * a + b * b) ** 0.5


# def is_int(n):  # n is expected to be a float
#     return n.is_integer()
def is_int(n):  # n is expected to be a float
    return n == int(n)


triples = calc_triples(1000)
