from functools import wraps
def retry(count):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(count):
                try:
                    return func(*args, **kwargs)
                except ValueError:
                    pass
                except OSError:
                    print(f"{func.__name__} raised OSError exception")
        return wrapper
    return decorator