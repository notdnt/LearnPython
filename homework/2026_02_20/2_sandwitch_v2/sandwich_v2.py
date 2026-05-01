

def dec_bread(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return "Bread\n" + result
    return wrapper

def dec_salat(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return "Salat\n" + result
    return wrapper

def dec_tomato(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return "Tomato\n" + result
    return wrapper

def dec_meat(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return "Meat\n" + result
    return wrapper
@dec_bread
@dec_salat
@dec_tomato
@dec_meat
@dec_bread
def make_sandwich():
    return ""

print(make_sandwich())