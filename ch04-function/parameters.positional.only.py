# a, b 必须通过位置参数传递
def func(a, b, /, c):
    print(a, b, c)


func(1, 2, 3)
func(1, 2, c=3)
