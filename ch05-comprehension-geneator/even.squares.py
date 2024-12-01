sq1 = list(
    map(lambda n: n * n, filter(lambda n: not n % 2, range(10)))
)

sq2 = [n * n for n in range(10) if not n % 2]

print(sq2, sq1 == sq2)
