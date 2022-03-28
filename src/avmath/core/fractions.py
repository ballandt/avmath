"""AVMATH FRACTIONS

Builds the avmath Fraction class. Is used elsewhere in core so needs to be
fully defined in this space.
"""

from .logics import _sgn, _gcd, _lcm
from .roots import Root


class Fraction:
    """Real fraction."""

    def __init__(self, num, den):
        """Takes integer or root arguments only."""
        self.num = num
        self.den = den
        if isinstance(den, Root):
            expand_value = Root(den.radical, den.factor, -den.constant)
            self.num *= expand_value
            self.den *= expand_value
        self.den *= _sgn(self.num)
        self.num = abs(self.num)

    def __repr__(self):
        if isinstance(self.num, int):
            return f"{self.num}/{self.den}"


class _Fraction:
    """Real fraction prototype for fraction operation and storage."""

    def __init__(self, num, den):
        """Initialisation with integer or avmath object values."""
        # Type conversions
        # Base case
        if isinstance(num, int) and isinstance(den, int):
            self.num = num
            self.den = den
        # Float value
        # Two cases to avoid creating new floats
        elif isinstance(num, float):
            num_num, num_den = num.as_integer_ratio()
            self.num = num_num
            self.den = num_den * den
        elif isinstance(den, float):
            den_num, den_den = den.as_integer_ratio()
            self.num = den_den * num
            self.den = den_num
        # Fraction value
        elif isinstance(num, _Fraction) or isinstance(den, _Fraction):
            self.num = (num / den).num
            self.den = (num / den).den
        # Reduction
        divisor = _gcd(self.num, self.den)
        self.num = self.num * _sgn(self.den) // divisor
        self.den = abs(self.den) // divisor

    # Mathematical methods
    def __neg__(self):
        """Returns negative fraction."""
        return _Fraction(-self.num, self.den)

    def __add__(self, other):
        """Fraction addition."""
        common_factor = _lcm(self.den, other.den)
        fac1 = self.num * common_factor // self.den
        fac2 = other.num * common_factor // other.den
        return _Fraction(fac1+fac2, common_factor)

    def __mul__(self, other):
        """Fraction multiplication."""
        if isinstance(other, _Fraction):
            return _Fraction(self.num * other.num, self.den * other.den)
        else:
            return _Fraction(self.num * other, self.den)

    __rmul__ = __mul__

    def __truediv__(self, other):
        """Fraction division."""
        return _Fraction(self.num, self.den * other)

    def __rtruediv__(self, other):
        """Reversed fraction division."""
        return _Fraction(self.den * other, self.num)

    def __pow__(self, power):
        """Fraction power method."""
        # reciprocate
        if power == -1:
            return _Fraction(self.den, self.num)
        else:
            return _Fraction(self.num**power, self.den**power)

    def __abs__(self):
        return _Fraction(abs(self.num), self.den)

    # Comparison methods
    def __eq__(self, other):
        """Returns equality of elements."""
        return float(self) == float(other)

    def __gt__(self, other):
        """Greater than method."""
        return float(self) > other

    def __lt__(self, other):
        """Less than method."""
        return float(self) < other

    def __ge__(self, other):
        """Greater equal method."""
        return float(self) >= other

    def __le__(self, other):
        """Less equal method."""
        return float(self) <= other

    # Type conversion methods
    def __float__(self):
        """Float conversion."""
        return self.num / self.den

    def __int__(self):
        """Integer conversion."""
        return self.num // self.den


class CFraction:
    """AVMATH FRACTION

    A complex fraction of the form p/q + s/t*j with p, q, s, t in Z. Used for
    more precise calculations with rational numbers if they occur. Standard
    division type in symbolic vector and matrix calculations.

    Fraction is always reduced in initialisation. If no imaginary part is
    detected, <, >, <=, >= operations are available. Representation is always
    as short as possible printing integers if possible and if there is no
    imaginary part, just the real fraction is printed. If there is no real
    part, 0 + s/t*j is printed.

    Use as follows

    Import
    >>> from avmath import Fraction

    Initialisation
    >>> Fraction(2, 3)
    2/3

    Initialisation with float values
    >>> Fraction(2.23, 1)
    5021513584518103/2251799813685248

    Initialisation with complex values
    >>> Fraction(2+3j, 4-7j)
    -1/5 + 2/5 j
    >>> r = Fraction(2, 3)
    2/3
    >>> i = Fraction(-5, 2)
    -5/2
    >>> c = Fraction(real=r, imag=i)
    2/3 - 5/2 j

    Representation is special cases
    >>> Fraction(4, 2)
    2
    >>> r = Fraction(2, 3)
    2/3
    >>> i = Fraction(0, 1)
    0
    >>> c = Fraction(real=r, imag=i)
    2/3
    >>> r = Fraction(0, 1)
    0
    >>> i = Fraction(2, 3)
    2/3
    >>> c = Fraction(real=r, imag=i)
    0 + 2/3 j
    """

    def __init__(self, num=None, den=None, **kwargs):
        """num -> numerator
        den -> denominator

        allowed kwargs:
        real -> real part of fraction as real fraction
        imag -> imaginary part of fraction as real fraction"""
        # Zero division check
        # Note that 1 / (0/1) is treated as 1 / 0
        if den == 0:
            raise ZeroDivisionError("Denominator must not be 0")
        if isinstance(num, Fraction) or isinstance(den, Fraction):
            self._real = (num / den)._real
            self._imag = (num / den)._imag
        # kwargs initialisation
        elif kwargs.get("real") or kwargs.get("imag"):
            real = kwargs.get("real")
            imag = kwargs.get("imag")
            # Error handling
            if not real and imag:
                # Not both real and imaginary value given
                raise TypeError("Initialisation must contain both real and "
                                "imaginary values")
            elif not num == den is None:
                # real and imag, numerator and denominator given
                raise TypeError("Too many arguments given")
            self._real = _Fraction(real, 1)
            self._imag = _Fraction(imag, 1)
        elif kwargs.get("real"):
            self._real = kwargs.get("_real")
            self._imag = _Fraction(0, 1)
        else:
            num = complex(num)
            den = complex(den)
            a = _Fraction(*num.real.as_integer_ratio())
            b = _Fraction(*num.imag.as_integer_ratio())
            c = _Fraction(*den.real.as_integer_ratio())
            d = _Fraction(*den.imag.as_integer_ratio())
            self._real = _Fraction(a * c + b * d, c ** 2 + d ** 2)
            self._imag = _Fraction(b * c + (-a) * d, c ** 2 + d ** 2)

    def __repr__(self):
        """Returns string reproduction of the complex fraction."""
        if self._imag < 0:
            return f"{self._real} - {abs(self._imag)} j"
        else:
            return f"{self._real} + {self._imag} j"

    # Type conversion
    def __int__(self):
        """Converts fraction p/q to the biggest integer a such that a < p/q.
        Can only be executed if imaginary part is 0 else causes
        ArithmeticError.
        """
        if self._imag != 0:
            raise ArithmeticError("Complex fraction cannot be converted to"
                                  " integer")
        return int(self._real)

    def __float__(self):
        """Converts fraction to float. Can only be executed if imaginary part
        is 0 else causes ArithmeticError.
        """
        if self._imag != 0:
            raise ArithmeticError("Complex fraction cannot be converted to"
                                  " float")
        return float(self._real)

    def __complex__(self):
        """Converts fraction to complex number."""
        return float(self._real) + float(self._imag)*1j

    # Comparison methods
    def __eq__(self, other):
        """Returns equality of fraction with another number."""
        return complex(self) == other

    def __gt__(self, other):
        """Checks if fraction is greater than another number. Can only be
        executed if the imaginary part is 0 else causes ArithmeticError.
        """
        if self._imag != 0:
            raise ArithmeticError("Complex fraction does not support"
                                  " greater than operation")
        return self._real > other




