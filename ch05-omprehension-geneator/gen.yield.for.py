def print_squares(start, end):
    for n in range(start, end):
        yield n * n


print(print_squares(2, 5))

for n in print_squares(2, 5):
    print(n)
