from cmath import sqrt


def quadratic(a, b, c):
    delta = sqrt(b**2 - 4 * a * c)
    x1 = (-b + delta) / 2 * a
    x2 = (-b - delta) / 2 * a
    return x1, x2
