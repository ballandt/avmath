"""LOGIC FUNCTIONS

Builds the logic functions for public API and processing."""


def _sgn(arg):
    """Sign function."""
    if arg > 0:
        return 1
    elif arg < 0:
        return -1
    else:
        return 0


def _gcd(arg1, arg2):
    """Greatest common divisor."""
    if arg2 == 0:
        # Greatest common divisor of x and 0 defined as x
        return arg1
    while arg1 % arg2 != 0:
        r = arg1 % arg2
        arg1 = arg2
        arg2 = r
    return abs(arg2)


def _lcm(arg1, arg2):
    """Least common multiply."""
    if arg2 != 0:
        return abs(arg1 * arg2) // _gcd(arg1, arg2)
    else:
        # Least common multiply of x and 0 defined as 0
        return 0
