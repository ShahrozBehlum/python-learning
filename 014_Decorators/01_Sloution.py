#for make decorator create func inside func. 

import time 

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time!")
        return result
    return wrapper

@timer #decorator this func will always pass inside the the timer func.
def example_function(n):
    time.sleep(n)

example_function(2)