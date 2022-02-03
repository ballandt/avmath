"""AVMATH

Avmath is a Python module for mathematical purposes.
It contains functionalities for simple mathematical
usage as sine or logarithm functions and submodules
for more advanced applied math in the topics of ana-
lysis and linear algebra.

The module uses a mathematical syntax. The classes
and functions are named in a mathematical manner and
the class operations enable a mathematical workflow.
Its issue is to calculate as accurate as possible and
not firstly the aspect of time.

Documentation: https://github.com/ballandt/avmath/wiki/documentation
GitHub: https://www.github.com/ballandt/avmath
PyPi: https://www.pypi.org/project/avmath
"""

__author__ = "Camillo Ballandt"
__version__ = "3.1.1"
__date__ = "2022/01/08"

__all__ = ["Fraction",
           "sin", "cos", "tan",
           "arcsin", "arccos", "arctan",
           "sinh", "cosh", "tanh",
           "arsinh", "arcosh", "artanh",
           "ln", "log", "is_even", "fac", "sgn",
           "pi", "e", "phi", "gamma"]

import time
from typing import Union as _Union, Iterable as _Iterable

_TAYLOR_DIFFERENCE = 1e-16
_MAX_CALCULATION_TIME = 5
REAL = _Union[int, float, 'Fraction']

e: float = 2.718_281_828_459_045_235_360
pi: float = 3.141_592_653_589_793_238_463
phi: float = 1.618_033_988_749_894_848_205
gamma: float = 0.577_215_664_901_532_860_607

two_digit_primes: list[int] = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                               43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


class ArgumentError(Exception):
    """Raised if false argument is given."""

    def __init__(self, got, want):
        self.got = got
        self.want = want

    def __str__(self):
        return f"False argument given. Expected {self.want}, got {self.got}."


class DimensionError(Exception):
    """Raised if arguments have different amount of dimensions."""

    def __init__(self, got=None, want=None, other=None):
        if other is None:
            self.got = got
            self.want = want
        else:
            self.other = other

    def __str__(self):
        try:
            return f"Wrong amount of dimensions." \
                   f"Expected {self.want}; got {self.got}"
        except AttributeError:
            return self.other


class Fraction:
    """Mathematical fraction"""

    def __init__(self, numerator: REAL, denominator: REAL):
        """Initializes fraction. Denominator will be made positive.
        Insert
        Fraction(a, b)
        for
        a/b

        and
        Fraction(a, Fraction(b, c))
        for
        a/(b/c)
        """
        while not type(numerator) in (int, Fraction):
            if numerator.is_integer():
                numerator = int(numerator)
            numerator *= 10
            denominator *= 10
        while not type(denominator) in (int, Fraction):
            if denominator.is_integer():
                denominator = int(denominator)
            numerator *= 10
            denominator *= 10
        if numerator == 0 and type(denominator) == Fraction:
            self.a = 0
            self.b = denominator.b
        elif (type(numerator) == Fraction or type(denominator) == Fraction)\
                and numerator != 0:
            self.a = (numerator / denominator).a
            self.b = (numerator / denominator).b
        else:
            self.a = numerator * sgn(denominator)
            self.b = abs(denominator)
        if self.b == 0:
            raise ZeroDivisionError("Zero inserted as denominator.")

    def __repr__(self) -> str:
        """Returns string representation. Always reduced."""
        if self.b == 1:
            ret_str = f"{self.a}"
        elif self.a / self.b == self.a // self.b:
            ret_str = f"{self.a // self.b}"
        elif self.int_args():
            ret_str = f"{self.reduce().a}/{self.reduce().b}"
        else:
            ret_str = f"{self.a}/{self.b}" if not self.b == 1 else f"{self.a}"
        return ret_str

    def __neg__(self) -> 'Fraction':
        """Returns negative fraction."""
        return Fraction(-self.a, self.b)

    def __eq__(self, other: REAL) -> bool:
        """Verifies the equality of two fractions."""
        if type(other) == Fraction and self.int_args() and other.int_args():
            return self.reduce().a == other.reduce().a \
                and self.reduce().b == other.reduce().b
        else:
            return float(self) == float(other)

    def __lt__(self, other: REAL) -> bool:
        """Less than."""
        return float(self) < float(other)

    def __gt__(self, other: REAL) -> bool:
        """Greater than."""
        return float(other) < float(self)

    def __add__(self, other: REAL | complex) -> 'Fraction':
        """Adds either two fractions or fractions and numbers."""
        if type(other) in (int, float):
            a = self.a + other * self.b
            return Fraction(a, self.b)

        elif type(other) == complex:
            return complex(self) + other

        elif type(other) == Fraction and self.int_args() and other.int_args():
            reduced_self = self.reduce()
            reduced_other = other.reduce()
            factor = lcm(reduced_self.b, reduced_other.b)
            summand1 = Fraction(reduced_self.a*int(factor/reduced_self.b),
                                reduced_self.b*int(factor/reduced_self.b))
            summand2 = Fraction(reduced_other.a*int(factor/reduced_other.b),
                                reduced_other.b*int(factor/reduced_other.b))
            return Fraction(summand1.a + summand2.a, summand1.b)

    __radd__ = __add__

    def __sub__(self, other: REAL) -> 'Fraction':
        """Subtracts either real from Fraction or Fraction from Fraction."""
        return self + -other

    __rsub__ = __sub__

    def __mul__(self, other: REAL) -> 'Fraction':
        """Multiplies REALS."""
        if type(other) in (int, float):
            return Fraction(self.a * other, self.b)
        elif type(other) == Fraction:
            if self.int_args() and other.int_args:
                return Fraction(self.a * other.a, self.b * other.b).reduce()
            else:
                return Fraction(self.a * other.a, self.b * other.b)
        else:
            return other.__mul__(self)

    __rmul__ = __mul__

    def __truediv__(self, other: REAL) -> 'Fraction':
        if type(other) == Fraction:
            res = self * other ** -1
        else:
            res = Fraction(self.a, self.b * other)
        if type(res) == Fraction and res.int_args():
            res = res.reduce()
        return res

    __rtruediv__ = __truediv__

    def __pow__(self, power: REAL) -> 'Fraction':
        if power == -1:
            return Fraction(self.b, self.a)
        else:
            # print(self.a, self.b, power)
            return Fraction(self.a ** float(power), self.b ** float(power))

    def __rpow__(self, other: REAL) -> float:
        return (other ** self.a) ** (1 / self.b)

    def __mod__(self, other: REAL) -> float:
        return float(self) % float(other)

    __rmod__ = __mod__

    def __int__(self) -> int:
        return int(float(self))

    def __float__(self) -> float:
        reduced_fraction = self.reduce()
        return reduced_fraction.a / reduced_fraction.b

    def __complex__(self):
        return float(self) + 0j

    def __abs__(self) -> 'Fraction':
        return Fraction(abs(self.a), self.b)

    def reduce(self) -> 'Fraction':
        if not self.int_args():
            raise ArgumentError("float values", "integer values")
        divisor = gcd(self.a, self.b)
        return Fraction(int(self.a / divisor), int(self.b / divisor))

    def int_args(self) -> bool:
        return type(self.a) == int and type(self.b) == int


def _check_types(arg: _Iterable, *types):
    """Checks if the elements of the argument belong to the given types."""
    for ele in arg:
        if not type(ele) in types:
            raise ArgumentError(type(ele), types)
    return True


def is_even(x: int) -> bool:
    """Checks if x is an even number"""
    return x/2 == x // 2


def is_prime(x: int) -> bool:
    """Checks if integer is prime."""
    int_root = int(x ** 0.5)
    for i in range(2, int_root):
        if x / i == x // i:
            return False
    return True


def gcd(x: int, y: int) -> int:
    """Greatest common divisor."""
    if y == 0:
        return x
    while x % y != 0:
        r = x % y
        x = y
        y = r
    return abs(y)


def lcm(x: int, y: int) -> int:
    """Least common multiply."""
    return int(abs(x * y) / gcd(x, y)) if y != 0 else 0


def sgn(x: REAL) -> int:
    """Returns signum of x."""
    if x < 0:
        return -1
    elif x == 0:
        return 0
    elif x > 0:
        return 1


def fac(x: REAL, opt: str = None):
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


def ln(x: REAL) -> float:
    """Natural logarithm."""
    if x <= 0:
        raise ArgumentError(x, "x >= 0")
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


def log(x: REAL, base: REAL) -> float:
    """Logarithm."""
    return ln(x) / ln(base)


def sin(x: REAL) -> float:
    """Sine."""
    x %= 2 * pi
    res = 0
    k = 0
    while True:
        mem_res = res
        res += (-1) ** k * x ** (2 * k + 1) / fac(2 * k + 1)
        if abs(mem_res - res) < _TAYLOR_DIFFERENCE:
            return res
        k += 1


def cos(x: REAL) -> float:
    """Cosine."""
    x %= 2 * pi
    res = 0
    k = 0
    while True:
        mem_res = res
        res += (-1) ** k * (x**(2 * k) / fac(2 * k))
        if abs(mem_res - res) < _TAYLOR_DIFFERENCE:
            return res
        k += 1


def tan(x: REAL) -> float:
    """Tangent."""
    return sin(x) / cos(x)


def arcsin(x: REAL) -> float:
    """Arc sine."""
    if abs(x) > 1:
        raise ArgumentError("x > 1", "x <= 1")
    if abs(x) == 1:
        return sgn(x) * pi / 2
    res = x
    k = 1
    start_time = time.time()
    while (time.time() - start_time) < _MAX_CALCULATION_TIME:
        mem_res = res
        res += fac(2 * k - 1, opt="double") /\
            (fac(2 * k, opt="double") * (2 * k + 1)) * x ** (2 * k + 1)
        if abs(mem_res - res) < _TAYLOR_DIFFERENCE:
            break
        k += 1
    return res


def arccos(x: REAL) -> float:
    """Arc cosine."""
    return pi/2 - arcsin(x)


def arctan(x: REAL) -> float:
    """Arc tangent."""
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


def sinh(x: REAL) -> float:
    """Hyperbolic sine."""
    if abs(x) > 710:
        raise ArgumentError(x, "argument |x| < 710")
    res = 0
    k = 0
    while True:
        mem_res = res
        res += x ** (2 * k + 1) / fac(2 * k + 1)
        if abs(mem_res - res) < _TAYLOR_DIFFERENCE:
            return res
        k += 1


def cosh(x: REAL) -> float:
    """Hyperbolic cosine."""
    if abs(x) > 710:
        raise ArgumentError(x, "argument |x| < 710")
    res = 0
    k = 0
    while True:
        mem_res = res
        res += x**(2*k) / fac(2*k)
        if abs(mem_res - res) < _TAYLOR_DIFFERENCE:
            return res
        k += 1


def tanh(x: REAL) -> float:
    """Hyperbolic tangent."""
    return sinh(x) / cosh(x) if abs(x) <= 20 else sgn(x) * 1.0


def arsinh(x: REAL) -> float:
    """Inverse hyperbolic sine."""
    return sgn(x) * ln(abs(x) + (x**2 + 1)**0.5)


def arcosh(x: REAL) -> float:
    """Inverse hyperbolic cosine."""
    if x < 1:
        raise ArgumentError(x, "x >= 1")
    return ln(x + (x**2 - 1)**0.5)


def artanh(x: REAL) -> float:
    """Inverse hyperbolic tangent."""
    if abs(x) >= 1:
        raise ArgumentError(x, "|x| < 1")
    return 0.5 * ln((1 + x) / (1 - x))


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
    "sgn": sgn,
    "e": e,
    "pi": pi,
}
