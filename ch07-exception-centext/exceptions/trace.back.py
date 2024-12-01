def square_root(number):
    if number < 0:
        raise ValueError("No negative numbers please")
    return number**0.5


def quadratic(a, b, c):
    d = b**2 - 4 * a * c
    return (-b - square_root(d)) / (2 * a), (-b + square_root(d)) / (2 * a)


print(quadratic(1, 0, 1))  # ValueError: No negative numbers please
