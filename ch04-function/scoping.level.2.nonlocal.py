def outer():
    test = 1

    def inner():
        nonlocal test  # outer scope
        test = 2
        print("inner: ", test)

    inner()
    print("outer: ", test)  # 2


test = 0
outer()
print("global: ", test)
