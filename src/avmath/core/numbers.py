from math import isqrt, sqrt
from .constants import square_numbers_to_20
from .logics import lcm, gcd, sgn, real_to_frac


def find_square_factor(x):
    """Returns tuple with number decomposed to integer a and highest square
    b such that a*b = x.
    Returns tuple in form (a, b).
    If x == 0 returns (0, 0)
    If x == 1 returns (1, 1)
    If x is negative a value will be negative and b positive
    """
    if x == 0:
        return 0, 0
    for e in reversed(square_numbers_to_20):
        if x / e == x // e:
            return x // e, e


class Real:
    """Real number

    The avmath number type with
         p + c√(r)
    a = ----------        p in Z; c, q, r in N
            q
    Allows symbolic calculations with fractions and square roots.

    Examples:
    ---------

    >>> Real(1, 2)
    1/2
    >>> Real(0.25)
    1/4
    >>> Real(3, 5, 8, 2)
    (3+4√2)/5
    """

    def __init__(self, num, den=1, rad=0, fac=1, **kwargs):
        """Initialises the Real. Default values are:
        denominator = 1
        radical = 0
        factor = 0
        If factor * radical == 0 both are set to 0.
        If initialised with float or Real only num value is checked.
        Initialisation with float forces fraction.
        """
        if isinstance(num, float):
            if md := kwargs.get("md"):
                num, den = real_to_frac(num, md=md)
            else:
                num, den = real_to_frac(num)
            self.num = num
            self.den = den
            self.rad = 0
            self.fac = 1
        elif isinstance(num, Real):
            self.num = num.num
            self.den = num.den
            self.rad = num.rad
            self.fac = num.fac
        else:
            # Sign handling
            num *= sgn(den)
            fac *= sgn(den)
            den = abs(den)
            # Root standard
            if not fac:
                fac = 0
                rad = 0
            if not rad:
                fac = 0
            # Root decomposition
            if rad != 0:
                if isqrt(rad) == sqrt(rad):
                    num += fac * isqrt(rad)
                    fac = 0
                    rad = 0
                else:
                    decom = find_square_factor(rad)
                    fac *= isqrt(decom[1])
                    rad = decom[0]
            # Reduction
            gcd_num = gcd(num, fac)
            gcd_gen = gcd(gcd_num, den)
            num, fac, den = num // gcd_gen, fac // gcd_gen, den // gcd_gen
            # Attribute assignments
            self.num = num
            self.den = den
            self.fac = fac
            self.rad = rad

    def __repr__(self):
        """Returns shortest possible string to represent the Real.
        1. num == den == fac == rad == 0
            0
        2. num != 0; den == fac == rad == 0
            num
        3. num != 0; rad != 0; fac == 1
            num+√(rad)        - no braces if len(str(rad)) == 1
        4.a num != 0; rad != 0; fac < 0
            num-abs(fac)√(rad)
        4.b num != 0; rad != 0; fac > 0
            num+fac√(rad)
        5. num == 0; rad != 0
            [fac]√(rad)        - fac like in previous examples
        6. den != 1; num != 0; rad != 0
            (num[+fac]√(rad))/den
        7. den != 1; either num or rad == 0
            [num/[fac]√(rad)]/den        - no braces for numerator
        """
        ret_str = ""
        if self == 0:
            ret_str = "0"
        else:
            if self.num:
                ret_str += str(self.num)
            if self.rad:
                if self.num and self.rad:
                    if self.fac > 0:
                        ret_str += "+"
                    else:
                        ret_str += "-"
                if self.fac and self.fac != 1:
                    ret_str += str(self.fac)
                if len(str(self.rad)) > 1:
                    ret_str += f"\u221A({self.rad})"
                else:
                    ret_str += f"\u221A{self.rad}"
            if self.den != 1:
                if self.num and self.rad:
                    ret_str = f"({ret_str})/{self.den}"
                else:
                    ret_str += f"/{self.den}"
        return ret_str

    def __neg__(self):
        return Real(-self.num, self.den, self.rad, -self.fac)

    def __float__(self):
        return (self.num + self.fac * sqrt(self.rad)) / self.den

    def __int__(self):
        return int(float(self))

    def __ceil__(self):
        if int(self) == float(self):
            return int(self)
        else:
            return 1 + int(self)

    def __complex__(self):
        return complex(float(self))

    def __add__(self, other):
        if isinstance(other, Real):
            if self.rad != other.rad:
                return float(self) + float(other)
            den = lcm(self.den, other.den)
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

    def __mul__(self, other):
        if isinstance(other, Real):
            if self.rad == other.rad:
                num = self.num * other.num + self.fac * other.fac * self.rad
                den = self.den * other.den
                rad = self.rad
                fac = self.num * other.fac + other.num * self.fac
                return Real(num, den, rad, fac)
        elif isinstance(other, int):
            num = self.num * other
            fac = self.fac * other
            return Real(num, self.den, self.rad, fac)
        else:
            return float(self) * other

    __rmul__ = __mul__

    def __pow__(self, power, modulo=None):
        if isinstance(power, int):
            if power == -1:
                num = self.den * self.num
                den = pow(self.num, 2) - pow(self.fac, 2) * self.rad
                fac = -self.fac * self.den
                return Real(num, den, self.rad, fac)
            elif power == 0:
                return Real(1, 1)
            elif power > 0:
                res = self
                for _ in range(power-1):
                    res *= self
                return res
            else:
                return (self ** (abs(power))) ** -1
        else:
            return float(self) ** power

    def __rpow__(self, other):
        return other ** float(self)

    def __truediv__(self, other):
        return self * other**-1

    def __rtruediv__(self, other):
        return self**-1 * other

    def __eq__(self, other):
        return complex(self) == other

    def __lt__(self, other):
        return float(self) < other

    def __gt__(self, other):
        return float(self) > other

    def __abs__(self):
        if self < 0:
            return -self
        else:
            return self


class Complex:
    pass


def div(__x, __y, /, md=10000, ff=False):
    """Division function. Executes the best possible division.
    Decides the following cases:
    1. Two variables of type int
      returns Real
    2. Floats or complex in division
      Tries to convert floats/complex to fractions. 'md' (maximal denominator)
      specifies the maximal duration of the search algorithm for small
      fractions.
      If successful returns Real/Complex type.
      If 'ff' (force fraction) is False and the algorithm failed, will return
      the result of the float/complex division, else (ff=True) returns the
      fraction with the float.as_integer_ratio() method.
    3. Real or Complex with each other
      Standard real/complex division
    4. Real/Complex with int
      Converts int to Real. Returns Real/Complex
    """
    # Zero division handling
    if __y == 0:
        raise ZeroDivisionError("denominator must not be 0")
    var_types = {type(__x), type(__y)}
    # 1. Only integers
    if var_types == {int}:
        return Real(__x, __y)
    # 2. floats or complex
    elif float in var_types or complex in var_types:
        arg_list = [__x, __y]
        for i, ele in enumerate(arg_list):
            if isinstance(ele, float):
                if ff:
                    arg_list[i] = Real(*real_to_frac(ele, md))
                elif vals := real_to_frac(ele, md, ff=False):
                    arg_list[i] = Real(*vals)
                else:
                    return float(__x) / float(__y)
            elif isinstance(ele, complex):
                # Force fractions
                if ff:
                    real = Real(*real_to_frac(ele.real, md))
                    imag = Real(*real_to_frac(ele.imag, md))
                    arg_list[i] = Complex(real=real, imag=imag)
                # Do not force fraction
                elif (vals_real := real_to_frac(ele.real, md, False))\
                        and (vals_imag := real_to_frac(ele.imag, md, False)):
                    arg_list[i] = Complex(real=Real(*vals_real), imag=Real(*vals_imag))
                else:
                    return complex(__x) / complex(__y)
        return div(*tuple(arg_list))
    # Real and Complex
    elif var_types == {Real} or var_types == {Complex} \
            or var_types == {Real, Complex}:
        return __x / __y
    # Real/Complex and integer
    elif var_types == {Real, int}:
        return Real(__x) / Real(__y)
    elif var_types == {Complex, int}:
        return Complex(__x) / Complex(__y)
