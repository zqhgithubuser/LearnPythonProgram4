from math import sqrt, ceil


def get_primes(n):
    """Calculate a list of primes up to n (included)."""
    primes = []
    for candidate in range(2, n + 1):
        is_prime = True
        root = ceil(sqrt(candidate))
        for prime in primes:
            if prime > root:
                break
            if candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
    return primes


print(get_primes(20))
