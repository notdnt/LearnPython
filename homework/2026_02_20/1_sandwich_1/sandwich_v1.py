

def dec_bread(func):
    def wrapper():
        func()
        print("Bread")
    return wrapper

def dec_salat(func):
    def wrapper():
        func()
        print("Salat")
    return wrapper

def dec_tomato(func):
    def wrapper():
        func()
        print("Tomato")
    return wrapper

def dec_meat(func):
    def wrapper():
        func()
        print("Meat")
    return wrapper

@dec_bread
@dec_salat
@dec_tomato
@dec_meat
@dec_bread
def make_sandwich():
    ...

make_sandwich()