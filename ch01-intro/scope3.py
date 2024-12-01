def enclosing_func():
    m = 7

    def local():
        # local 函数中没有找到变量 m，接着
        # 在 enclosing_func 的作用域中查找
        print(m)

    local()


m = 5
print(m)
enclosing_func()  # 7
