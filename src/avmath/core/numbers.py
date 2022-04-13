from math import isqrt, sqrt
from .constants import square_numbers_to_20
from .logics import _lcm, _gcd, _sgn


def find_square_factor(x):
    """Returns tuple with number decomposed to integer a and highest square
    b such that a*b = x.
    Returns tuple in form (a, b).
    """
    if x == 0:
        return 1, 0
    for e in reversed(square_numbers_to_20):
        if x / e == x // e:
            return x // e, e


class Real:

    def __init__(self, num, den=1, rad=0, fac=1):
        # Sign handling
        num *= _sgn(den)
        den = abs(den)
        # Root decomposition
        if rad != 0:
            if isqrt(rad) == sqrt(rad):
                num += fac * isqrt(rad)
                fac = 1
                rad = 0
            else:
                decom = find_square_factor(rad)
                fac *= isqrt(decom[1])
                rad = decom[0]
        # Reduction
        gcd_num = _gcd(num, fac)
        gcd = _gcd(gcd_num, den)
        num, fac, den = num // gcd, fac // gcd, den // gcd
        # Attribute assignments
        self.num = num
        self.den = den
        self.fac = fac
        self.rad = rad

    def __repr__(self):
        ret_str = str(self.num)
        if self.fac not in (0, 1):
            ret_str += f"+{self.fac}"
        if self.rad != 0 and self.fac != 0:
            ret_str += f"\u221A({self.rad})"
        if self.den != 1:
            ret_str = f"({ret_str})/{self.den}"
        return ret_str

    def __neg__(self):
        return Real(-self.num, self.den, self.rad, -self.fac)

    def __float__(self):
        return (self.num + self.fac * sqrt(self.rad)) / self.den

    def __add__(self, other):
        if isinstance(other, Real):
            if self.rad != other.rad:
                return float(self) + float(other)
            den = _lcm(self.den, other.den)
            num = self.num * den // self.den + other.num * den // other.den
            fac = self.fac * den // self.den + other.fac * den // other.den
            return Real(num, den, self.rad, fac)
        elif float(other).is_integer():
            return self + Real(int(other))

    __radd__ = __add__

    def __sub__(self, other):
        return self + -other

    def __rsub__(self, other):
        return -self + other



