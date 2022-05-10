"""AVMATH VECTOR FUNCTIONS

Definition of the methods for vector calculation. For public API see
avmath.algebra.Vector.

Contained functions do not check input, wrong arguments will raise unexpected
errors. Standard input and output type is list. Input lists are not changed.
"""
from math import acos, degrees
from numbers import Number, Real
from typing import Iterable, Sized
from .numbers import sqrt, div


def add(vec1, vec2):
    """Vector addition."""
    res = []
    for i in range(len(vec1)):
        res.append(vec1[i]+vec2[i])
    return res


def sub(vec1, vec2):
    """Vector subtraction."""
    res = []
    for i in range(len(vec1)):
        res.append(vec1[i]-vec2[i])
    return res


def scamul(vec, sca):
    """Scalar multiplication for vector and scalar."""
    res = vec[:]
    # range(len()) is faster than enumerate
    for i in range(len(res)):
        res[i] = res[i] * sca
    return res


def dot(vec1, vec2):
    """Vector dot product.
    (a_1, a_2, ..., a_n) * (b_1, b_2, ..., b_n)
    := a_1 * b_1 + a_2 * b_2 + ... + a_n * b_n
    """
    res = 0
    for i in range(len(vec1)):
        res += vec1[i] * vec2[i]
    return res


def cross2x2(vec1, vec2):
    """Vector cross product for R^2 vectors.
    (a_1, a_2) x (b_1, b_2) := a_1 * b_2 - a_2 * b_1
    """
    return vec1[0] * vec2[1] - vec1[1] * vec2[0]


def cross3x3(vec1, vec2):
    """Vector cross product for R^3 vectors.
    (a_1, a_2, a_3) x (b_1, b_2, b_3)
    := (a_2 * b_3 - b_2 * a_3, a_3 * b_1 - a_1 * b_3, a_1 * b_2 - a_2 * b_1)
    """
    return [vec1[1]*vec2[2] - vec1[2]*vec2[1],
            vec1[2]*vec2[0] - vec1[0]*vec2[2],
            vec1[0]*vec2[1] - vec1[1]*vec2[0]]


def intpow(vec, power):
    """Power operation for vector and integer.
    a ^ t := a * a * a * a    (a in R^n, t in R)
              t times
    """
    res = vec[:]
    for i in range(power-1):
        if i % 2 == 0:
            res = dot(vec, res)
        else:
            res = scamul(vec, res)
    return res


def lead0(vec):
    """Number of leading zeros of a vector.
    Needed for GAUSS-algorithm."""
    for i in range(len(vec)):
        if vec[i] != 0:
            return i
    return len(vec)


def euclidean(vec):
    """Euclidean absolute of the vector"""
    rad = 0
    for i in range(len(vec)):
        rad += vec[i] ** 2
    return sqrt(rad)


class vec:
    """VECTOR

    Datatype for complex vector calculations.

    Examples
    --------

    >>> linalg.vec(3, 2, 5)
    (3, 2, 5)

    >>> linalg.vec(4, 0, 2-3j)
    (4, 0, 2-3j)
    """

    def __init__(self, *args, **kwargs):
        """Initialises vector. Coordinates can be passed to `*args`. Can be
        either multiple numbers or a list. Special preferences can be passed to
         `**kwargs`. Accepted keywords are:
          - checks (boolean)
            specifies whether checks are skipped (False) or not (True)
        """
        if len(args) == 1 and isinstance(args[0], Iterable):
            args = args[0]
        checks = kwargs.get("checks")
        if checks:
            for ele in args:
                if not isinstance(ele, Number):
                    raise TypeError(f"Elements must be numbers. Got '{ele}'")
        self._value = list(args)

    def __repr__(self):
        return str(tuple(self._value))

    def __iter__(self):
        for ele in self._value:
            yield ele

    def __len__(self):
        return len(self._value)

    dim = __len__

    def __getitem__(self, item):
        return self._value[item]

    def __neg__(self):
        return scamul(self._value, -1)

    def __add__(self, other):
        """Vector addition."""
        if not isinstance(other, vec):
            raise TypeError(f"Cannot add '{other}' to vector")
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimensions")
        return vec(add(self._value, other._value))

    def __sub__(self, other):
        return self + -other

    def __mul__(self, other):
        if isinstance(other, Number):
            return scamul(self._value, other)
        elif isinstance(other, vec):
            if len(self) != len(other):
                raise ValueError("Vectors must have the same dimensions.")
            return dot(self._value, other._value)
        else:
            raise TypeError(f"Cannot multiply '{other}' with vector")

    def __truediv__(self, other):
        if not isinstance(other, Number):
            raise TypeError(f"Cannot divide vector by '{other}'")
        return scamul(self._value, div(1, other))

    def norm(self):
        return euclidean(self._value)

    euclidean = norm
    __abs__ = norm

    @staticmethod
    def from_points(p1, p2):
        return vec(sub(p2, p1))

    @staticmethod
    def zeros(n):
        return vec([0 for _ in range(n)])

    @staticmethod
    def ones(n):
        return vec([1 for _ in range(n)])


# Public functions

def angle(__v1, __v2, /, deg=False):
    """Angle between two real value vectors."""
    if not (isinstance(__v1, Sized) and isinstance(__v2, Sized)):
        raise TypeError("Arguments must be vector like")
    if len(__v1) != len(__v2):
        return ValueError("Vectors must contain the same dimensions.")
    for i in range(len(__v1)):
        if not (isinstance(__v1[i], Real) or isinstance(__v2[i], Real)):
            raise ValueError("Vectors must contain real values")
    res = acos(dot(__v1, __v2) / (euclidean(__v1) * euclidean(__v2)))
    if not deg:
        return res
    else:
        return degrees(res)
