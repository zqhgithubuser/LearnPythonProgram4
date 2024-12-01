def gcd(a, b):
    """Calculate the Greatest Common Divisor of (a, b)."""
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    print(gcd(3, 5))
