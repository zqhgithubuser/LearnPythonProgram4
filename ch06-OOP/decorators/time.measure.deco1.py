from time import sleep, time


def f(sleep_time=0.1):
    sleep(sleep_time)


def measure(func):
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(func.__name__, "took: ", time() - t)

    return wrapper


f = measure(f)
f(0.3)  # f took:  0.30088233947753906
f(sleep_time=0.5)  # f took:  0.5007214546203613
print(f.__name__)  # wrapper
