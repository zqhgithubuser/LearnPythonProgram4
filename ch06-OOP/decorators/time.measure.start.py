from time import sleep, time


def f():
    sleep(0.3)


def g():
    sleep(0.5)


t = time()
f()
print("f took:", time() - t)

t = time()
g()
print("g took:", time() - t)
