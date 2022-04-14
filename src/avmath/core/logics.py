"""LOGIC FUNCTIONS

Builds the logic functions for public API and processing."""


def sgn(__x, /):
    """Sign function."""
    if __x > 0:
        return 1
    elif __x < 0:
        return -1
    else:
        return 0


def gcd(__x, __y, /):
    """Greatest common divisor."""
    if __y == 0:
        # Greatest common divisor of x and 0 defined as x
        return __x
    while __x % __y != 0:
        r = __x % __y
        __x = __y
        __y = r
    return abs(__y)


def lcm(__x, __y, /):
    """Least common multiply."""
    if __y != 0:
        return abs(__x * __y) // gcd(__x, __y)
    else:
        # Least common multiply of x and 0 defined as 0
        return 0


def real_to_frac(__r, /, md=10000):
    a = 1
    b = 1
    while b <= md:
        if a / b < __r:
            a += 1
        elif a / b > __r:
            b += 1
        else:
            return a, b
    return __r.as_integer_ratio()