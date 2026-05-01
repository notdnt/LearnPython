from random import random, choice

from my_decorator import retry

exceptions = (ValueError, OSError)


def retry(count):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < count:
                try:
                    result = func(*args, **kwargs)
                except ValueError:
                    attempts += 1
                    if attempts >= count:
                        raise
                except OSError:
                    print(f"{func.__name__} raise OSError exception.")
                    attempts += 1
                    if attempts >= count:
                        raise
        return wrapper
    return decorator


@retry(count=5)
def random_exception() -> float:
    if (d := random()) > 0.5:
        raise choice(exceptions)
    return d

if __name__ == "__main__":
    for _ in range(100):
        print("result:", random_exception())
