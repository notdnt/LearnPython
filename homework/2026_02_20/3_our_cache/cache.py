import time
def cache(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@cache
def func(a, b):
    time.sleep(2)
    return print(a + b)
func(2, 3)
func(2, 3)
