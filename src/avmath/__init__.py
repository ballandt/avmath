"""AVMATH
Avmath is a module for algebra, arithmetics and analysis.

Avmath uses python algorithms to numerically calculate mathematical
problems. It mainly concentrates on the concepts of functions, vec-
tors and matrices.

Github: https://www.github.com/ballandt/avmath
PyPi: https://www.pypi.org/project/avmath
"""

__author__ = "Camillo Ballandt"
__version__ = "3.0.0"
__date__ = "2021/12/01"

__all__ = ["sin", "cos", "tan",
           "arcsin", "arccos", "arctan",
           "sinh", "cosh", "tanh",
           "arsinh", "arcosh", "artanh",
           "ln", "log", "is_even", "fac", "sgn",
           "pi", "e", "phi", "gamma"]

import time
from typing import Iterable as _Iterable

_FLOAT_EQ = 1e-16
_TAYLOR_DIFFERENCE = 1e-16
_MAX_CALCULATION_TIME = 5

e = 2.718_281_828_459_045_235_360
pi = 3.141_592_653_589_793_238_463
phi = 1.618_033_988_749_894_848_205
gamma = 0.577_215_664_901_532_860_607


class ArgumentError(Exception):
    """Raised if false argument is given."""

    def __init__(self, got, want):
        self.got = got
        self.want = want

    def __str__(self):
        return f"False argument given. Expected {self.want}, got {self.got}."


def _check_types(arg: _Iterable, *types):
    """Checks if the elements of the argument belong to the given types."""
    for ele in arg:
        if not type(ele) in types:
            raise ArgumentError(ele, "int or float")
    return True


def is_even(x):
    """Checks if x is an even number"""
    return x/2 == round(x/2)


def sgn(x):
    """Returns signum of x"""
    if x < 0:
        return -1
    elif x == 0:
        return 0
    elif x > 0:
        return 1


def fac(x, opt=None):
    """Returns faculty of x.
    fac(x)               is x!
    fac(x, opt="double") is x!!
    """
    if x < 0:
        raise ArgumentError("x < 0", "x >= 0")
    if int(x) != x:
        raise ArgumentError("real x", "natural x")
    x = int(x)
    res = 1
    if opt == "double":
        if not is_even(x):
            for i in range(int(x / 2) + 1):
                res *= 2 * i + 1
        else:
            for i in range(1, int(x / 2)+1):
                res *= 2*i
    else:
        for i in range(1, x + 1):
            res *= i
    return res


def ln(x):
    """Natural logarithm"""
    if x < 0:
        raise ArgumentError(x, "x > 0")
    summand = 0
    while x > e:
        x /= e
        summand += 1
    while x < 1/e:
        x *= e
        summand -= 1
    res = 0
    k = 0
    while True:
        mem_res = res
        res += (x - 1) ** (2 * k + 1) / ((2 * k + 1) * (x + 1) ** (2 * k + 1))
        if abs(mem_res - res) < _TAYLOR_DIFFERENCE:
            break
        k += 1
    return 2 * res + summand


def log(x, base):
    """Logarithm"""
    return ln(x) / ln(base)


def sin(x):
    """Sine"""
    x %= 2 * pi
    res = 0
    k = 0
    while True:
        mem_res = res
        res += (-1) ** k * x ** (2 * k + 1) / fac(2 * k + 1)
        if abs(mem_res - res) < _TAYLOR_DIFFERENCE:
            return res
        k += 1


def cos(x):
    """Cosine"""
    x %= 2 * pi
    res = 0
    k = 0
    while True:
        mem_res = res
        res += (-1) ** k * (x**(2 * k) / fac(2 * k))
        if abs(mem_res - res) < _TAYLOR_DIFFERENCE:
            return res
        k += 1


def tan(x):
    """Tangent"""
    return sin(x) / cos(x)


def arcsin(x):
    """Arcus sine"""
    if x > 1:
        raise ArgumentError("x > 1", "x <= 1")
    if x == 1:
        return pi / 2
    res = x
    k = 1
    while k < 150:
        mem_res = res
        res += fac(2 * k - 1, opt="double") * x ** (2 * k + 1) / (fac(2 * k, opt="double") * (2 * k + 1))
        if abs(mem_res - res) < _TAYLOR_DIFFERENCE:
            break
        k += 1
    return res


def arccos(x):
    """Arcus cosine"""
    return pi/2 - arcsin(x)


def arctan(x):
    """Arcus tangent"""
    res = 0
    k = 0
    if abs(x) <= 1:
        start_time = time.time()
        while (time.time() - start_time) < _MAX_CALCULATION_TIME:
            mem_res = res
            res += (-1)**k * x**(2*k + 1) / (2*k + 1)
            if abs(mem_res - res) < _TAYLOR_DIFFERENCE:
                break
            k += 1
    else:
        if x >= 0:
            res = pi / 2
        else:
            res = -pi / 2
        start_time = time.time()
        while (time.time() - start_time) < _MAX_CALCULATION_TIME:
            mem_res = res
            res += (-1)**(k + 1) / ((2*k + 1) * x**(2*k + 1))
            if abs(mem_res - res) < _TAYLOR_DIFFERENCE:
                break
            k += 1
    return res


def sinh(x):
    """Hyperbolic sin"""
    res = 0
    k = 0
    while True:
        mem_res = res
        res += x ** (2 * k + 1) / fac(2 * k + 1)
        if abs(mem_res - res) < _TAYLOR_DIFFERENCE:
            return res
        k += 1


def cosh(x):
    """Hyperbolic cosine"""
    res = 0
    k = 0
    while True:
        mem_res = res
        res += x**(2*k) / fac(2*k)
        if abs(mem_res - res) < _TAYLOR_DIFFERENCE:
            return res
        k += 1


def tanh(x):
    """Hyperbolic tangent"""
    return sinh(x) / cosh(x)


def arsinh(x):
    """Area sine hyperbolicus"""
    return ln(x + (x**2 + 1)**0.5)


def arcosh(x):
    """Area cosine hyperbolicus"""
    if x < 1:
        raise ArgumentError(x, "x >= 1")
    return ln(x + (x**2 - 1)**0.5)


def artanh(x):
    """Area tangent hyperbolicus"""
    if abs(x) > 1:
        raise ArgumentError(x, "|x| < 1")
    return 0.5 * ln((x + 1) / (x - 1))


scope = {
    "sin": sin, "arcsin": arcsin,
    "cos": cos, "arccos": arccos,
    "tan": tan, "arctan": arctan,
    "sinh": sinh, "arsinh": arsinh,
    "cosh": cosh, "arccosh": arcosh,
    "tanh": tanh, "artanh": artanh,
    "log": log,
    "ln": ln,
    "fac": fac,
    "e": e,
    "pi": pi,
}
