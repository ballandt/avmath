"""AVMATH
AdVanced math is a module for algebra, arithmetics and analysis.
It is divided in the submodules lina (LINear Algebra), ana (ANAlysis)
and the arithmetics in the main directory.

It uses python algorithms to allow the access to deeper math and
shall simplify maths to concentrate on the usage of math.

Github: https://www.github.com/ballandt/avmath
PyPi: https://www.pypi.org/project/avmath
"""

__author__ = "Camillo Ballandt"
__version__ = "2.0.0"
__date__ = "2021/10/24"

_FLOAT_EQ = 1e-10
_DIVISION_ROUND_DECS = 2


class ArgumentError(Exception):
    """Raised if wrong argument is given."""

    def __init__(self, got, want):
        self.got = got
        self.want = want

    def __str__(self):
        return "False argument given. Expected " + str(self.want) + ", got " + str(self.got) + "."


class _Point:
    """Prototype for points in lina and ana"""

    def __init__(self, *args):
        self.value = list(args)

    def __getitem__(self, item):
        return self.value[item]

    def __eq__(self, other):
        """Returns the equality of two points. Uses _FLOAT_EQ to compare."""
        from . import _FLOAT_EQ
        if not _Point.dimcheck(self, other):
            return False
        for i in range(len(self.value)):
            if abs(self.value[i] - other.value[i]) > _FLOAT_EQ:
                return False
            else:
                pass
        return True

    @staticmethod
    def dimcheck(*args):
        """Returns 'True' if arguments have same amount of dimensions. Else returns 'False'."""
        dims = args[0].dims
        dimstrue = True
        for i in range(len(args)):
            dimstrue = dimstrue and (dims == args[i].dims)
        return dimstrue


def exp(*arg):
    """Exponential number in order: exp(x,y,z) = x^y^z"""
    args = len(arg)
    counter = args - 1
    res = arg[counter - 1] ** arg[counter]
    for _ in range(args - 2):
        res = arg[(counter - 2)] ** res
        counter -= 1
    return res


def is_even(x):
    return x/2 == round(x/2)


def fac(x, opt=None):
    """Faculty"""
    if x < 0:
        raise ArgumentError("x < 0", "x >= 0")
    res = 1
    if opt == "even":
        if not is_even(x):
            raise ArgumentError(x, "even number")
        for i in range(1, int(x / 2)+1):
            res *= 2*i
    elif opt == "odd":
        if is_even(x):
            raise ArgumentError(x, "odd number")
        for i in range(int(x/2) + 1):
            res *= 2*i + 1
    else:
        for i in range(1, x + 1):
            res *= i
    return res


def e():
    """Euler's number e"""
    res = 0
    for k in range(19):
        res += 1 / fac(k)
    return res


def pi():
    """Pi"""
    res = 0
    for k in range(24):
        res += ((-1) ** k) / (4 ** k) * ((2 / (4 * k + 1)) + (2 / (4 * k + 2)) + (1 / (4 * k + 3)))
    return res


def ln(x):
    """Natural logarithm"""
    if not x:
        raise ArgumentError(0, "x > 0")
    res = 0
    for k in range(round(x) * 10):
        res += (x - 1)**(2*k + 1) / ((2*k + 1) * (x + 1)**(2*k + 1))
    return 2 * res


def log(x, base):
    """Logarithm in order: log{base} ({exp})"""
    return ln(x) / ln(base)


def __period_resolving(value):
    """Returns values from -pi to pi for better handling
    for trigonometric functions.
    """
    value %= 2 * pi()
    if value >= pi():
        value = -(value % pi())
    return value


def sin(x):
    """Sine"""
    x = __period_resolving(x)
    res = 0
    for k in range(16):
        res += (-1)**k * x**(2*k + 1) / fac(2*k + 1)
    return res


def cos(x):
    """Cosine"""
    x = __period_resolving(x)
    res = 0
    for k in range(16):
        res += (-1) ** k * (x**(2 * k) / fac(2 * k))
    return res


def tan(x):
    """Tangent"""
    return sin(x) / cos(x)


def arcsin(x):
    """Arcus sine"""
    if x > 1:
        raise ArgumentError("x > 1", "x <= 1")
    x = __period_resolving(x)
    res = x
    for k in range(1, int(x*150)):
        res += fac(2*k - 1, opt="odd") * x**(2*k + 1) / (fac(2*k, opt="even") * (2*k + 1))
    return res


def arccos(x):
    """Arcus cosine"""
    return pi()/2 - arcsin(x)


def arctan(x):
    """Arcus tangent"""
    res = 0
    if abs(x) < 1:
        for k in range(80):
            res += (-1)**k * x**(2*k + 1) / (2*k + 1)
    else:
        res = pi() / 2 if x > 0 else -pi()/2
        for k in range(16):
            res += (-1)**(k + 1) / ((2*k + 1) * x**(2*k + 1))
    return res


def sinh(x):
    """Hyperbolic sin"""
    res = 0
    for k in range(int(16+x)):
        res += x**(2*k + 1) / fac(2*k + 1)
    return res


def cosh(x):
    """Hyperbolic cosine"""
    res = 0
    for k in range(int(16+x)):
        res += x**(2*k) / fac(2*k)
    return res


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
