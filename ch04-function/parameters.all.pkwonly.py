# 仅位置参数
# 普通参数
# 可变数量的位置参数
# 仅关键字参数
# 可变数量的关键字参数
def all_params(a, /, b, c=42, *args, d=256, e, **kwargs):
    print("a, b, c:", a, b, c)
    print("d, e:", d, e)
    print("args: ", args)  # args:  (4, 5, 6)
    print("kwargs: ", kwargs)  # kwargs:  {'f': 9, 'g': 10}


all_params(1, 2, 3, 4, 5, 6, e=7, f=9, g=10)
