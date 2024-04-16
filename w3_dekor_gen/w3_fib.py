import functools

# w functools jest defaultowo dekorator cache - functools.cache
# istnieje też lru_cache - można ustalić liczbę zapisywanych wartości, domyślnie 128 miejsc


def cached(func):
    saved = {}  # można dorobić atrybut w dekoratorze i modyfikować go

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = args + tuple(kwargs.items())
        if key not in saved:
            saved[key] = func(*args, **kwargs)
        return saved[key]

    wrapper.cache = saved  # fukcja może mieć atrybuty - jak klasa, dzięki temu możemy podpiąć ten cache do funkcji
    return wrapper


@cached
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)
