def get_squares_gen(n):
    for x in range(n):
        yield x * x


squares = get_squares_gen(4)
print(squares)
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
# print(next(squares))        # StopIteration
