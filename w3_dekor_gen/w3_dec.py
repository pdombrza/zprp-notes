from time import perf_counter
import functools

def timer(func):
    @functools.wraps(func) # aby uniknąć przesłonięcia tej nazwy funkcji
    def wrapper(*args, **kwargs):
        before = perf_counter()
        rv = func(*args, **kwargs)
        after = perf_counter()
        print("Time taken: ", after - before)
        return rv
    return wrapper


def ntimes(n): # dekorator ntimes
    def inner(func):
        @functools.wraps(func) # aby zachować nazwę i doc funkcji (ogólnie dane o funkcji)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                print(f"Running {func.__name__}")
                rv = func(*args, **kwargs)
            return rv
        return wrapper
    return inner


@ntimes(n=2)
def add(x, y=10):
    """adds stuff"""
    return x + y

@timer
def sub(x, y=10):
    """subtracts stuff"""
    return x - y


#Szablon dekoratora:

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        value = func(*args, **kwargs)
        return value
    return wrapper_decorator

