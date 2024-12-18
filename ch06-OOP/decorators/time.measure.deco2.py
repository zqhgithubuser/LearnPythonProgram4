from functools import wraps
from time import sleep, time


def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(func.__name__, "took: ", time() - t)

    return wrapper


@measure
def f(sleep_time=0.1):
    """I'm a cat. I love to sleep!"""
    sleep(sleep_time)


f(sleep_time=0.3)
print(f.__name__, ": ", f.__doc__)  # f :  I'm a cat. I love to sleep!
