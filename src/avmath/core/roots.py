"""AVMATH ROOTS

Definition of the root objects for the public API and backend procession.
"""
from .constants import square_numbers_to_20
from math import isqrt


def find_square_factor(x):
    """Returns tuple with number decomposed to integer a and highest square
    b such that a*b = x.
    Returns tuple in form (a, b).
    """
    for e in reversed(square_numbers_to_20):
        if x / e == x // e:
            return x // e, e


class Root:
    """AVMATH SQUARE ROOT

    Object of square root computations in the form a + b*(c)**(1/2) with
    complex a and b and integer c.
    """

    def __init__(self, radical, factor=None, constant=None):
        """Square root initialisation. Creates root of the form
        <constant> + <factor>*(<radical>)**(1/2).
        """
        # Tries to divide a square number
        decomposed = find_square_factor(radical)
        if factor:
            self.factor = factor * isqrt(decomposed[1])
        else:
            self.factor = isqrt(decomposed[1])
        # Checks if root is real or complex
        if decomposed[0] >= 0:
            self.radical = decomposed[0]
        else:
            # Multiplies factor times j
            self.radical = abs(decomposed[0])
            self.factor *= 0+1j
        # Appends constant
        if constant:
            self.constant = constant
        else:
            self.constant = 0

    def __repr__(self):
        """Returns string representation:
        Base form is
        a + b*c**(1/2)

        If a or b is 0, it is not displayed.

        """
        ret_str = ""
        if self.constant:
            ret_str += f"{self.constant}+"
        if self.factor:
            ret_str += f"{self.factor}"
        ret_str += f"\u221A({self.radical})"
        return ret_str

    def __neg__(self):
        return Root(self.radical, -self.factor, -self.constant)

    def __add__(self, other):
        """Adds a complex number to the square root.
        Does not return Root type if other is a root too.
        """
        if isinstance(other, Root):
            if not self.radical == other.radical:
                res = complex(self) + complex(other)
                if res.imag == 0:
                    return res.real
                else:
                    return res
            else:
                return Root(self.radical,
                            self.factor+other.factor,
                            self.constant+other.constant)
        else:
            return Root(self.radical, self.factor, self.constant+other)

    __radd__ = __add__

    def __sub__(self, other):
        """Root subtraction method. See __add__."""
        return self + -other

    def __rsub__(self, other):
        """Reversed subtraction method."""
        return other + -self

    def __mul__(self, other):
        if isinstance(other, Root):
            if self.radical == other.radical:
                return Root(radical=self.radical,
                            factor=self.factor*other.constant +
                            other.factor*self.constant,
                            constant=self.factor*other.factor*self.radical +
                            self.constant*other.constant)
            else:
                res = complex(self) * complex(other)
                if res.imag == 0:
                    return res.real
                else:
                    return res
        else:
            return Root(radical=self.radical,
                        factor=self.factor*other,
                        constant=self.constant*other)

    __rmul__ = __mul__

    def __float__(self):
        """Returns float representation of the root.
        If the result is a complex number, raises ValueError."""
        res = self.factor * self.radical**0.5 + self.constant
        if isinstance(res, complex):
            raise ValueError("Complex root cannot be converted to float")
        else:
            return res

    def __complex__(self):
        """Returns complex representation of the root."""
        return complex(self.factor * self.radical**0.5 + self.constant)



