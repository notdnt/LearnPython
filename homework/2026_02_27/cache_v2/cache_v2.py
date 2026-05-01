import os
import json


filename = "cache.pkl"
def cache(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            cache = json.load(f)
    else:
        cache = {}
    def dec(func):
        def wrapper(*args, **kwargs):
            key = []
            if args:
                key.append("args:" + ",".join(map(str, args)))
            if kwargs:
                kw_str = ",".join(f"{k}:{v}" for k, v in sorted(kwargs.items()))
                key.append("kwargs:" + kw_str)
            full_key = "|".join(key) if key else "none"
            if full_key in cache:
                return cache[full_key]
            result = func(*args, **kwargs)
            cache[full_key] = result
            with open(filename, "w") as f:
                json.dump(cache, f, indent = 4)
            return result
        return wrapper
    return dec

@cache(filename)
def sum(a,b):
    return a+b
#@cache(filename)
def thank(thank, name):
   return f"{thank}, {name}."

print(sum(6, 2))
print(sum(7, 5))
print(thank(name = "thx", thank = "proxi"))