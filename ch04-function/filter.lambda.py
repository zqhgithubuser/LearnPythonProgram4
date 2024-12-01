def get_multiples_of_five(n):
    return list(filter(lambda n: not n % 5, range(n + 1)))


print(get_multiples_of_five(20))
