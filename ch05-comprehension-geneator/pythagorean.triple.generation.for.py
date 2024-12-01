from functions import gcd


def gen_triples(N):
    for m in range(1, int(N**0.5) + 1):
        for n in range(1, m):
            if (m - n) % 2 and gcd(m, n) == 1:
                c = m * m + n * n
                if c < N:
                    a = m * m - n * n
                    b = 2 * m * n
                    yield a, b, c


print(list(gen_triples(50)))
print(sorted(gen_triples(50), key=sum))
