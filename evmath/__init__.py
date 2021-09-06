"""EVMATH
Evmath is a module for math handling in one module.

The main part of the module is geometry ('evmath.geometry').
Geometry is a evmath submodule including methods for
geometrical calculation. Includes features for points,
vectors, straights, areas, angles, matrices and structures. It is tried
to handle different amounts of dimensions, but not in all
cases every amount of dimensions is possible.
Concrete description follows with each class and method
(see 'help(evmath.geometry)')

It also contains a small collection of important
constants and functions (for example pi or sine). These are
sometimes copied from the builtin 'math' module so that only
one module may be used.

This module has not got a license. It may be distributed
properly as wished.
"""

__author__ = "Camillo Ballandt"
__version__ = "1.1.0(100)"
__date__ = "2021/09/01"

import math


class ArgumentError(Exception):
    """Raised if wrong argument is given."""

    def __init__(self, got, want):
        self.got = got
        self.want = want

    def __str__(self):
        return "False argument given. Expected " + str(self.want) + ", got " + str(self.got) + "."


def exp(*arg):
    """Exponential number in order: exp(x,y,z) = x^y^z"""
    args = len(arg)
    counter = args - 1
    res = arg[counter - 1] ** arg[counter]
    for _ in range(args - 2):
        res = arg[(counter - 2)] ** res
        counter -= 1
    return res


def fac(arg):
    """Returns faculty of argument.
    {arg}!"""
    res = 1
    for i in range(1, arg + 1):
        res *= i
    return res


def e(n=16):
    """Returns Euler's number. 'n' defines the amount
    of times the formula is repeated and is not recommended
    to be altered."""
    res = 0
    for k in range(n + 3):
        res += 1 / fac(k)
    return res


def pi(n=24):
    """Pi. 'n' defines amount of times the formula is repeated.
    Default 'n=24' returns 15 correct digits and is not recommended
    to be altered."""
    res = 0
    for k in range(n):
        res += ((-1) ** k) / (4 ** k) * ((2 / (4 * k + 1)) + (2 / (4 * k + 2)) + (1 / (4 * k + 3)))
    return res


def ln(arg):
    """Natural logarithm"""
    return math.log(arg)


def log(exponential, base):
    """Logarithm in order: log{base} ({exp})"""
    return math.log(exponential, base)


def sin(x, n=15):
    """Returns sine of a number. Formula repeated 'n' times
    Default 'n=16' returns 15 correct digits and is not recommended
    to be altered."""
    res = 0
    for k in range(n):
        res += (-1) ** k * (x ** (2 * k + 1) / fac(2 * k + 1))
    return res


# TODO Avoid math module

def cos(arg):
    """Cosine"""
    return math.cos(arg)


def tan(arg):
    """Tangent"""
    return math.tan(arg)


def arcsin(arg):
    """Arcus sine"""
    return math.asin(arg)


def arccos(arg):
    """Arcus cosine"""
    return math.acos(arg)


def arctan(arg):
    """Arcus tangent"""
    return math.atan(arg)


def sinh(arg):
    """Hyperbolic sin"""
    return math.sinh(arg)


def cosh(arg):
    """Hyperbolic cosine"""
    return math.cosh(arg)


def tanh(arg):
    """Hyperbolic tangent"""
    return math.tanh(arg)


def arcsinh(arg):
    """Arcus sine hyperbolicus"""
    return math.asinh(arg)


def arccosh(arg):
    """Arcus cosine hyperbolicus"""
    return math.acosh(arg)


def arctanh(arg):
    """Arcus tangent hyperbolicus"""
    return math.atanh(arg)
