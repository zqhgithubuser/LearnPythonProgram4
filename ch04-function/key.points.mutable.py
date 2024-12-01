x = [1, 2, 3]


def func(x):
    x[1] = 42
    print(id(x), x)


func(x)
print(id(x), x)  # [1, 42, 3]
