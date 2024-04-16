from time import perf_counter
import functools
import logging


def timer(func):
    @functools.wraps(func)  # aby uniknąć przesłonięcia tej nazwy funkcji
    def wrapper(*args, **kwargs):
        before = perf_counter()
        rv = func(*args, **kwargs)
        after = perf_counter()
        print("Time taken: ", after - before)
        return rv

    return wrapper


def ntimes(n):  # dekorator ntimes
    def inner(func):
        @functools.wraps(
            func
        )  # aby zachować nazwę i doc funkcji (ogólnie dane o funkcji)
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


# Szablon dekoratora:


def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        value = func(*args, **kwargs)
        return value

    return wrapper_decorator


# decorators with arguments (logging example):
def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        return wrapper

    return decorate


# Zastosowanie
@logged(logging.DEBUG)
def add2(x, y):
    return x + y


@logged(logging.CRITICAL, "example")
def spam(x, y):
    return "Spam!"


# Decorator with optional arguments (this is crazy)
def logged_optional(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return functools.partial(logged, level=level, name=name, message=message)
    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)

    return wrapper


# Zastosowanie
@logged
def add3(x, y):
    return x + y


@logged(logging.CRITICAL, "example")
def eggs(x, y):
    return "Eggs!"
