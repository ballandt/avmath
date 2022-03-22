"""AVMATH ROOTS

Definition of the root objects for the public API and backend procession.
"""
from .constants import square_numbers_to_20


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
        self.radical = radical
        self.factor = factor
        self.constant = constant

    def __repr__(self):
        """Returns string representation:
        Base form is
        a + b*c**(1/2)

        If a or b is 0, it is not displayed.

        """
        ret_str = ""
        if self.constant:
            ret_str += f"{self.constant} + "
        if self.factor:
            ret_str += f"{self.factor}*"
        ret_str += f"{self.radical}**(1/2)"
        return ret_str

    def __add__(self, other):
        """Adds a complex number to the square root."""
