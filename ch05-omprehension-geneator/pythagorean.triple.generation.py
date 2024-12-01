from functions import gcd

N = 50
triples = sorted(
    (
        (a, b, c)
        for a, b, c in (
            (m * m - n * n, 2 * m * n, m * m + n * n)
            for m in range(1, int(N**0.5) + 1)
            for n in range(1, m)
            if (m - n) % 2 and gcd(m, n) == 1
        )
        if c < N
    ),
    key=sum,
)

print(triples)
