def get_squares(n):
    return [x * x for x in range(n)]


print(get_squares(10))


def get_squares_gen(n):
    for x in range(n):
        yield x * x


print(list(get_squares_gen(10)))
