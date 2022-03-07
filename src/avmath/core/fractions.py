"""AVMATH FRACTIONS

Builds the avmath Fraction class. Is used elsewhere in core so needs to be
fully defined in this space.
"""


class _Fraction:
    """Real fraction prototype for fraction operation and storage."""


class Fraction:
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