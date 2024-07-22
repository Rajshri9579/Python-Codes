import time

def time_calculator(func):
    def wrapper(*args, **kwargs):              #arguments for unlimited execution...
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@time_calculator                #decorator
def example_function(n):
    time.sleep(n)

example_function(2)