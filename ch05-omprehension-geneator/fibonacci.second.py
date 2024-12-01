def fibonacci(N):
    """Return all fibonacci numbers up to N."""
    yield 0
    if N == 0:
        return
    a, b = 0, 1
    while b <= N:
        yield b
        a, b = b, a + b


print(list(fibonacci(0)))
print(list(fibonacci(1)))
print(list(fibonacci(50)))
