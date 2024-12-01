x = 3


def func(x):
    x = 7
    print(id(x), x)


func(x)
print(id(x), x)
