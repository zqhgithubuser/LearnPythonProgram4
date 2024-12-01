# 可变数量的关键字参数
def func(**kwargs):
    print(type(kwargs), kwargs)


func(a=1, b=2)  # <class 'dict'> {'a': 1, 'b': 2}
func(a=1, b=46, c=99)  # <class 'dict'> {'a': 1, 'b': 46, 'c': 99}
