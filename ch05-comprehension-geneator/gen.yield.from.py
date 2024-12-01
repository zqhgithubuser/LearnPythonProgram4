def print_squares(start, end):
    yield from (n * n for n in range(start, end))


print(print_squares(2, 5))

for n in print_squares(2, 5):
    print(n)
