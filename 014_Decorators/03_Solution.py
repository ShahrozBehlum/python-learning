import time


def cache(func):
    cache_vlaue = {}
    print(cache_vlaue)
    def wrapper(*args):
        if args in cache_vlaue:
            return cache_vlaue[args]
        result = func(*args)
        cache_vlaue[args] = result
        return result
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b

print(long_running_function(2,3))
print(long_running_function(2,3))