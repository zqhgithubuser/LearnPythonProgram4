# 普通参数
# 可变数量的位置参数
# 可变数量的关键字参数
def func(a, b, c=7, *args, **kwargs):
    print("a, b, c:", a, b, c)
    print("args: ", args)  # args:  (5, 7, 9)
    print("kwargs: ", kwargs)  # kwargs:  {'A': 'a', 'B': 'b'}


func(1, 2, 3, 5, 7, 9, A="a", B="b")
