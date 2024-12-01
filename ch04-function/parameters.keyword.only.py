def kwo(*a, c):
    print(a, c)


kwo(1, 2, 3, c=7)  # (1, 2, 3) 7
kwo(c=4)  # () 4
# kwo(1, 2)
# TypeError: kwo() missing 1 required keyword-only argument: 'c'


# c 必须通过关键字传递
def kwo2(a, b=42, *, c):
    print(a, b, c)


kwo2(3, c=99)  # 3 42 99
# kwo2(3, 23)
# TypeError: kwo2() missing 1 required keyword-only argument: 'c'
