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

__all__ = ["Fraction", "CFraction",
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

two_digit_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
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
        if denominator == 0:
            raise ZeroDivisionError("Denominator must not be zero")
        if type(numerator) == int and type(denominator) == int:
            self.a = numerator * sgn(denominator)
            self.b = abs(denominator)
        elif type(numerator) == Fraction or type(denominator) == Fraction:
            self.a = (numerator / denominator).a
            self.b = (numerator / denominator).b
        elif type(numerator) == float or type(denominator) == float:
            numerator, denominator = float(numerator), float(denominator)
            numerators = numerator.as_integer_ratio()
            denominators = denominator.as_integer_ratio()
            self.a = numerators[0] * denominators[1]
            self.b = numerators[1] * denominators[0]

    def __repr__(self) -> str:
        """Returns string representation. Always reduced."""
        if self.a / self.b == self.a // self.b:
            ret_str = f"{self.a // self.b}"
        else:
            ret_str = f"{self.reduce().a}/{self.reduce().b}"
        return ret_str

    def __neg__(self) -> 'Fraction':
        """Returns negative fraction."""
        return Fraction(-self.a, self.b)

    def __eq__(self, other: REAL) -> bool:
        """Verifies the equality of two fractions."""
        if type(other) == Fraction:
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

    def __ge__(self, other):
        """Greater or equal."""
        return float(self) >= float(other)

    def __le__(self, other):
        """Less or equal."""
        return float(self) <= float(other)

    def __add__(self, other) -> 'Fraction':
        """Adds either two fractions or fractions and numbers."""
        if type(other) in (int, float):
            a = self.a + other * self.b
            return Fraction(a, self.b)

        elif type(other) == complex:
            return complex(self) + other

        elif type(other) == Fraction:
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

    def __rsub__(self, other: REAL) -> 'Fraction':
        return other + -self

    def __mul__(self, other: REAL) -> 'Fraction':
        """Multiplies REALS."""
        if type(other) in (int, float, complex):
            return Fraction(self.a * other, self.b)
        elif type(other) == Fraction:
            return Fraction(self.a * other.a, self.b * other.b).reduce()
        else:
            return other.__mul__(self)

    __rmul__ = __mul__

    def __truediv__(self, other: REAL) -> 'Fraction':
        if type(other) == Fraction:
            res = self * other ** -1
        else:
            res = Fraction(self.a, self.b * other)
        if type(res) == Fraction:
            res = res.reduce()
        return res

    def __rtruediv__(self, other):
        res = Fraction(self.b * other, self.a)
        if type(res) == Fraction:
            res = res.reduce()
        return res

    def __pow__(self, power: REAL) -> 'Fraction':
        if power == -1:
            return Fraction(self.b, self.a)
        else:
            return Fraction(self.a ** float(power), self.b ** float(power))

    def __rpow__(self, other: REAL) -> float:
        return (other ** self.a) ** (1 / self.b)

    def __mod__(self, other: REAL) -> float:
        return float(self) % float(other)

    __rmod__ = __mod__

    def __int__(self) -> int:
        return self.a // self.b

    def __float__(self) -> float:
        reduced_fraction = self.reduce()
        return reduced_fraction.a / reduced_fraction.b

    def __complex__(self):
        return float(self) + 0j

    def __abs__(self) -> 'Fraction':
        return Fraction(abs(self.a), self.b)

    def reduce(self) -> 'Fraction':
        divisor = gcd(self.a, self.b)
        return Fraction(int(self.a / divisor), int(self.b / divisor))

    def int_args(self) -> bool:
        return type(self.a) == int and type(self.b) == int


class CFraction:
    """Fraction with complex values"""

    def __init__(self, numerator=None, denominator=None, real=None, imag=None):
        """Enter complex numerator and denominator or real and imaginary
        values. Works with real values too."""
        if denominator == 0:
            raise ZeroDivisionError("Denominator must not be zero")
        if real is not None and imag is not None:
            if type(real) == type(imag) == Fraction:
                self.real = real
                self.imag = imag
            else:
                self.real = Fraction(*float(real).as_integer_ratio())
                self.imag = Fraction(*float(imag).as_integer_ratio())
        elif type(numerator) == CFraction or type(denominator) == CFraction:
            self.real = (numerator/denominator).real
            self.imag = (numerator/denominator).imag
        else:
            numerator = complex(numerator)
            denominator = complex(denominator)
            a = Fraction(*numerator.real.as_integer_ratio())
            b = Fraction(*numerator.imag.as_integer_ratio())
            c = Fraction(*denominator.real.as_integer_ratio())
            d = Fraction(*denominator.imag.as_integer_ratio())
            self.real = Fraction(a*c + b*d, c**2 + d**2)
            self.imag = Fraction(b*c - a*d, c**2 + d**2)

    def __repr__(self):
        """Returns string reproduction of the complex fraction."""
        if self.imag < 0:
            return f"{self.real} - {abs(self.imag)} j"
        else:
            return f"{self.real} + {self.imag} j"

    def __complex__(self):
        return float(self.real) + float(self.imag) * 0+1j

    def __neg__(self):
        return CFraction(real=-self.real, imag=-self.imag)

    def __add__(self, other):
        if type(other) == CFraction:
            real = self.real + other.real
            imag = self.imag + other.imag
            return CFraction(real=real, imag=imag)
        if type(other) in (int, float, Fraction):
            return CFraction(real=self.real+other, imag=self.imag)

    __radd__ = __add__

    def __sub__(self, other):
        return self + -other

    def __rsub__(self, other):
        return other + -self

    def __mul__(self, other):
        if type(other) == CFraction:
            real = self.real * other.real - self.imag * other.imag
            imag = self.real * other.imag + self.imag * other.real
            return CFraction(real=real, imag=imag)
        else:
            return CFraction(real=self.real*other, imag=self.imag*other)

    def __truediv__(self, other):
        if type(other) == CFraction:
            return self * other**-1
        else:
            return CFraction(
                real=Fraction(self.real, other),
                imag=Fraction(self.imag, other)
            )

    def __pow__(self, power):
        if power == -1:
            return CFraction(
                real=Fraction(self.real, self.real**2 + self.imag**2),
                imag=Fraction(-self.imag, self.real**2 + self.imag**2)
            )
        elif type(power) == int and power > 0:
            res = self
            for i in range(power-1):
                res *= self
            return res
        else:
            return (abs(self)*(cos(self.phi()) + sin(self.phi()) * 1j))**power

    def __abs__(self) -> float:
        return float((self.real**2 + self.imag**2)**0.5)

    def __eq__(self, other):
        return complex(self) == complex(other)

    def phi(self):
        return arctan(self.imag / self.real)

    def conjugate(self):
        return CFraction(real=self.real, imag=-self.imag)


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
