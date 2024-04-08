def square(x):
    """
    Squares the input.

    >>> square(2)
    4
    >>> square(-2)
    4
    """
    return x * x


if __name__ == "__main__":
    import doctest
    doctest.testmod()