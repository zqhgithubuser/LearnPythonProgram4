def outer():
    test = 1
    def inner():
        test = 2
        print("inner: ", test)

    inner()
    print("outer: ", test)


test = 0
outer()
print("global: ", test)
