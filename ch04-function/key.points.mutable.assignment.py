x = [1, 2, 3]


def func(x):
    x[1] = 42
    x = "something else"
    print(id(x), x)


func(x)
print(id(x), x)
