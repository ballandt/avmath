"""AVMATH ANALYSIS
AdVanced math  analysis submodule
implementing function features."""

__all__ = ["Point", "Function", "Polynomial"]

import copy
import sys
from typing import Union

from . import scope as _scope, REAL, sgn,is_even, Fraction, ArgumentError

eps = sys.float_info.epsilon


class Point:
    """Point in coordinate system. (Two dimensions)"""

    def __init__(self, x: REAL, y: REAL):
        """Initialises the point. Give x and y value."""
        self._value = [x, y]

    def __iter__(self):
        for e in self._value:
            yield e

    def __repr__(self):
        return str(tuple(self))

    def __getitem__(self, item):
        return self._value[item]

    def negative_y(self) -> 'Point':
        """Returns a point with negative y coordinate."""
        return Point(self[0], -self[1])


class Function:
    """Mathematical function. Enter argument as string."""

    def __init__(self, arg: str):
        """Initialisation of function. Enter function
        as string. Coefficient writing and ^ for power
        is allowed.
        See:
        https://github.com/ballandt/avmath/wiki/analysis#function__init__arg
        """
        self.term = arg
        self._arg_scope = _scope

    def __repr__(self) -> str:
        """Returns string representation"""
        return f"f(x) = {self.term}"

    def __add__(self, other: Union[REAL, 'Function']) -> 'Function':
        """Adds two functions"""
        if type(other) == Function:
            ret_formula = f"{self.term} + {other.term}"
        else:
            ret_formula = f"{self.term} + {other}"
        return Function(ret_formula)

    __radd__ = __add__

    def __sub__(self, other: 'Function') -> 'Function':
        """Subtracts two functions"""
        ret_formula = f"{self.term} - ({other.term})"
        return Function(ret_formula)

    def __mul__(self, other: REAL | 'Function') -> 'Function':
        """Multiplies two functions."""
        if type(other) == Function:
            ret_formula = f"({self.term}) * ({other.term})"
        else:
            ret_formula = f"{other} * ({self.term})"
        return Function(ret_formula)

    __rmul__ = __mul__

    def __truediv__(self, other: REAL | 'Function') -> 'Function':
        """Divides two functions or a function and a REAL."""
        if type(other) == Function:
            ret_formula = f"({self.term}) / ({other.term})"
        else:
            ret_formula = f"({self.term}) / {other}"
        return Function(ret_formula)

    def __rtruediv__(self, other: REAL | 'Function') -> 'Function':
        """Divides a REAL by a function."""
        return Function(f"{other} / ({self.term})")

    def __neg__(self) -> 'Function':
        """Returns negative function"""
        return Function(f"-({self.term})")

    def replace(self, value: REAL) -> str:
        """Replaces intuitive elements with correct ones."""
        return_string = self.term.replace("^", "**")
        i = 0
        while True:
            i = return_string.find("x", i)
            if i == -1:
                break
            elif i == 0:
                i += 1
                continue
            if return_string[i-1] in "0123456789":
                return_string = f"{return_string[:i]}*{return_string[i:]}"
            i += 1
        return return_string.replace("x", f"({value})")

    def set_scope(self, scope: dict):
        """Sets a new dict as scope."""
        self._arg_scope = scope

    def append_scope(self, scope: dict):
        """Appends dict to eval() scope. If appended scope contains elements
        that are already defined the appended elements are preferred.
        """
        self._arg_scope = {**self._arg_scope, **scope}

    def at(self, value: REAL) -> REAL:
        """Get function value at specific x value."""
        formula_at = self.replace(value)
        return eval(formula_at, self._arg_scope)

    def max(self, xmin: REAL, xmax: REAL, steps: int = 1000) -> list:
        """Finds maxima of a function using changed newton method:
        x_{n+1} = x_n - f'(x_n) / f''(x_n)
        """
        sgn_step = (xmax - xmin) / steps
        x_pos = xmin
        candidates = []
        for i in range(steps):
            if sgn(self.derivative(x_pos))\
                    != sgn(self.derivative(x_pos+sgn_step)):
                candidates.append(x_pos)
            x_pos += sgn_step
        return_list = []
        for ele in candidates:
            value = Point(self.newton_method_extrema(ele),
                          self.at(self.newton_method_extrema(ele)))
            if value not in return_list and self.second_derivative(ele) < 0:
                return_list.append(value)
        return return_list

    def min(self, xmin: REAL, xmax: REAL, steps: int = 1000) -> list:
        """Finds minima of a function in a given domain."""
        neg_func = -self
        return [e.negative_y() for e in neg_func.max(xmin, xmax, steps)]

    def root(self, xmin: REAL, xmax: REAL, step: int = 1000) -> list:
        """Find roots of functions with f(x) = 0.
        Returns only x-coordinate.
        """
        sgn_step = (xmax - xmin) / step
        x_pos = xmin
        candidates = []
        for i in range(step):
            if sgn(self.at(x_pos)) != sgn(self.at(x_pos + sgn_step)):
                candidates.append(x_pos)
            x_pos += sgn_step
        return_list = []
        for element in candidates:
            if not self.newton_method(element) in return_list:
                return_list.append(self.newton_method(element))
        return return_list

    def newton_method(self, x_n: REAL, steps: int = 50) -> float:
        """Newton's method to find root of function from given point x_n.
        x_{n+1} = x_n - f(x_n) / f'(x_n)
        """
        for _ in range(steps):
            if self.derivative(x_n) != 0:
                x_n = x_n - self.at(x_n) / self.derivative(x_n)
            else:
                x_n += 1e-2
        return x_n

    def newton_method_extrema(self, x_n, steps: int = 50) -> float:
        """Method to find extrema of a function. Derived from Newton's method:
         x_{n+1} = x_n - f'(x_n) / f''(x_n)"""
        for _ in range(steps):
            if self.second_derivative(x_n) != 0:
                x_n = x_n - self.derivative(x_n) / self.second_derivative(x_n)
            else:
                x_n += 1e-2
        return x_n

    def derivative(self, x: REAL, h=None) -> float:
        """Returns derivative of a function.
        Uses an algorithm to calculate the best h."""
        if not h:
            if self.second_derivative(x) < 1e-3 or self.at(x) == 0:
                h = eps ** (1 / 3)
            else:
                h = 2 * (eps * abs(self.at(x))
                         / abs(self.second_derivative(x))) ** 0.5
        return (4 * self.at(x + h / 2) - 3 * self.at(x) - self.at(x + h)) / h

    def second_derivative(self, x: REAL, h=1e-5) -> float:
        """Returns the second derivative of a formula.
        There may be better h than default instruction."""
        return (self.at(x + h) - 2 * self.at(x) + self.at(x - h)) / h ** 2

    def num_dif(self, x: REAL, h: REAL = 1e-5) -> float:
        """Returns numerical second order differentiation
        of function at x value.
        === INACTIVE ===
        Use Function.derivative instead.
        """
        return (self.at(x + h) - self.at(x - h)) / 2 * h

    def second_num_dif(self, x: REAL, h: REAL = 1e-5) -> float:
        """Returns numerical second order differentiation
        of function at x value.
        === INACTIVE ===
        Use Function.second_derivative instead.
        """
        x1 = self.num_dif(x - h)
        x2 = self.num_dif(x + h)
        return (x2 - x1) / (2 * h)

    def num_int(self, a: REAL, b: REAL, n: int = 1000) -> float:
        """Returns the numerical integral of a function in a given space.
        === INACTIVE ===
        Use Function.integral instead.
        """
        res = (b - a) / n
        term = 0
        for i in range(n):
            xi = a + i * (b - a) / n + (b - a) / (2 * n)
            term += self.at(xi)
        res *= term
        return res

    def integral(self,
                 a: REAL,
                 b: REAL,
                 n: int = 1000,
                 option: str = None) -> float:
        """Returns a numerical calculation of the integral of
        a function in the domain between a and b.
        Option `option="trapeze"` uses trapeze formula.
        """
        h = (b - a) / n
        if option == "trapeze":
            res = (self.at(a) - self.at(b)) / 2
            for i in range(1, n):
                res += self.at(a + i * h)
        else:
            res = 0
            for i in range(n):
                res += self.at(a + i * h + h / 2)
        res *= h
        return res

    def tangent(self, x: REAL) -> 'Function':
        """Returns a function that lies tangential to self at a given x."""
        a = self.derivative(x)
        b = a * -x + self.at(x)
        return Function(f"{a} * x + {b}")

    def normal(self, x: REAL) -> 'Function':
        """Returns a function that lies normal to self at a given x."""
        a = -self.derivative(x)
        b = a * -x + self.at(x)
        return Function(f"{a} * x + {b}")


class Polynomial:
    """A real function a_0 x^n + a_1 x^{n-1} + ... + a_{n-1} x + a_n
    with real n.
    """

    def __init__(self, *args):
        """Insert arguments in analytical order:
        args[0] x^n + args[1] x^{n-1} + ...
        """
        if type(args[0]) in (int, float, complex, Fraction):
            self._value = []
            i = 0
            while args[i] == 0:
                i += 1
            self._value = list(args[i:])
        elif type(args[0]) == Point:
            arg_list = [[] for _ in range(len(args))]
            for i, e in enumerate(args):
                for j in range(len(args)):
                    if e[0] == arg_list[i-1][0]:
                        raise ArithmeticError("Points with same x coordinate"
                                              "cannot be processed")
                    arg_list[i].append(e[0] ** (len(args)-j-1))
                arg_list[i].append(e[-1])
            from .algebra import SLE
            self._value = list(SLE(*tuple(arg_list)).solve())
        else:
            raise ArgumentError(type(args[0]), "int, float, complex, Fraction")

    def __iter__(self):
        """Yields an iterator of the polynomial coefficients."""
        for e in self._value:
            yield e

    def __getitem__(self, item):
        """Allows item access for coefficients."""
        return copy.deepcopy(self._value[item])

    def __repr__(self):
        """Gives string return in form
        f(x) = (a_0)x^n + (a_1)x^{n-1} + ...
        """
        ret_str = "f(x) = "
        for i, e in enumerate(self):
            power = self.degree() - i
            if power > 1:
                ret_str += f"({e})x^{self.degree() - i} + "
            elif power == 1:
                ret_str += f"({e})x + "
            else:
                ret_str += str(e)
        return ret_str

    def __neg__(self):
        """Returns negative polynomial. All coefficient signs are switched."""
        return Polynomial(*tuple([-e for e in self]))

    def __len__(self):
        """Returns the amount of coefficients. Corresponds to degree + 1"""
        return len(self._value)

    def __add__(self, other):
        """Adds two polynomials or a polynomial with a REAL."""
        if type(other) == Polynomial:
            self_list, self_len = list(self), len(self)
            other_list, other_len = list(other), len(other)
            if self_len > other_len:
                other_list = [0 for _ in range(self_len - other_len)]\
                             + other_list
            elif self_len < other_len:
                self_list = [0 for _ in range(other_len - self_len)]\
                             + self_list
            arg_list = [e + other_list[i] for i, e in enumerate(self_list)]
        elif type(other) in (int, float, Fraction):
            arg_list = list(self)
            arg_list[-1] += other
        else:
            raise ArgumentError(type(other), "function or real number")
        return Polynomial(*tuple(arg_list))

    __radd__ = __add__

    def __sub__(self, other):
        """Subtracts polynomials from another or REAL from polynomial."""
        return self + -other

    def __rsub__(self, other):
        """Reversed subtraction."""
        return -self + other

    def __mul__(self, other):
        """Multiplies two polynomials or a polynomial with a REAL."""
        arg_list = []
        if type(other) == Polynomial:
            arg_list = [0 for _ in range(self.degree() + other.degree() + 1)]
            for i, e_self in enumerate(self):
                power_self = self.degree() - i
                for j, e_other in enumerate(other):
                    power_other = other.degree() - j
                    arg_list[-power_self-power_other-1] += e_self * e_other
        elif type(other) in (float, int, Fraction):
            arg_list = [other * e for e in self] if other != 0 else [0]
        return Polynomial(*tuple(arg_list))

    __rmul__ = __mul__

    def __truediv__(self, other: REAL) -> 'Polynomial':
        return Polynomial(*tuple([Fraction(e, other) for e in self]))

    def at(self, x):
        """Returns y value to given x."""
        res = 0
        for i, e in enumerate(self):
            res += e * x**(self.degree() - i)
        return res

    def no_fractions(self):
        """All coefficients are made to floats."""
        return Polynomial(*tuple([float(e) for e in self]))

    def degree(self):
        """Returns the grade of the polynomial."""
        return len(self) - 1

    def newton_method(self, x_n, max_steps: int = 10000):
        """Executes Newton's method to find a root of the polynomial
        numerically. Used for root-method."""
        for _ in range(max_steps):
            if self.derivative(x_n) != 0:
                mem_x_n = x_n
                x_n = x_n - self.at(x_n) / self.derivative(x_n)
                if abs(x_n - mem_x_n) < 1e-16:
                    break
            else:
                x_n += 1e-2
        if abs(self.at(x_n)) < 1e-12:
            return x_n
        else:
            raise ArithmeticError("No root found")

    def even_powers(self):
        for index, e in enumerate(reversed(list(self))):
            if not is_even(index) and e != 0:
                return False
        return True

    def odd_powers(self):
        for index, e in enumerate(reversed(list(self))):
            if is_even(index) and e != 0:
                return False
        return True

    def decomposition(self):
        ret_list = [copy.deepcopy(self)]
        while True:
            new_ret_list = []
            for e in ret_list:
                if len(e) <= 2:
                    continue
                if e[-1] == 0:
                    new_ret_list += [Polynomial(1, 0),
                                     Polynomial(*tuple(e[:-1]))]
                    continue
                elif e.even_powers():
                    pass

    def horner(self, x_0: int | float = 0):
        """Returns a polynomial with executed Horner's scheme with given
        root x_0. Note that the root must be exact for proper results.
        """
        arg_list = []
        product = 0
        for i, e in enumerate(self[:-1]):
            arg_list.append(e + product)
            product = x_0 * (e + product)
        return Polynomial(*tuple(arg_list))

    def roots(self, mode=complex):
        """Returns a list of the roots of a polynomial.
        `mode=float` or `mode="real"` returns real solutions only.
        """
        if self.degree() == 0:
            if self[0] != 0:
                return []
            else:
                return ArithmeticError("Null function has an infinite amount"
                                       "of roots")
        elif self.degree() == 1:
            ret_list = [Fraction(-self[1], self[0])]
        elif self.degree() == 2:
            ret_list = [
                (-self[1]-(self[1]**2-4*self[0]*self[2])**.5)/(2*self[0]),
                (-self[1]+(self[1]**2-4*self[0]*self[2])**.5)/(2*self[0])
            ]
        elif self.degree() > 2 and self.even_powers():
            first_one = self / self[0]
            substitute = []
            for e in first_one:
                if e != 0:
                    substitute.append(e)
            ret_list = []
            for e in Polynomial(*tuple(substitute)).roots():
                ret_list.append(e**0.5)
                ret_list.append(-e**0.5)
        else:
            ret_list = sorted(
                        [self.newton_method(1+1j)]
                        + self.horner(self.newton_method(1+1j)).roots(),
                        key=lambda ele: ele.real
                )
        if mode == complex:
            return ret_list
        elif mode == float or mode == "real":
            real_solutions = []
            for e in ret_list:
                if e.imag == 0:
                    real_solutions.append(e.real)
            return real_solutions

    def max(self):
        """Returns the maxima of the polynomial based on the real roots."""
        x_values = self.derivative().roots(mode=float)
        ret_list = []
        for e in x_values:
            if self.derivative(e, grade=2) < 0:
                ret_list.append(Point(e, self.at(e)))
        return ret_list

    def min(self):
        """Returns the minima of a function based on the real roots."""
        return [e.negative_y() for e in (-self).max()]

    def intersection(self, other, mode=complex):
        return [Point(e, self.at(e)) for e in (self - other).roots(mode=mode)]

    def derivative(self,
                   x: float | int = None,
                   grade: int = 1) -> REAL | 'Polynomial':
        """Returns the derivative polynom if no x is specified. Else returns
        the value of the derivative at given x.
        """
        function = copy.deepcopy(self)
        for _ in range(grade):
            arg_list = []
            if len(function) == 1:
                arg_list = [0]
            for i, e in enumerate(function[:-1]):
                arg_list.append(e * (function.degree() - i))
            function = Polynomial(*tuple(arg_list))
            if list(function) == [0]:
                break
        if x is not None:
            return function.at(x)
        else:
            return function

    def tangent(self, x):
        """Returns a Polynomial of degree 1 (linear function) that lies tangent
        to the function.
        """
        m = self.derivative(x)
        n = self.at(x) - m * x
        return Polynomial(m, n)

    def normal(self, x):
        """Returns a Polynomial of degree 1 (linear function) that lies normal
        to the function.
        """
        m = -Fraction(1, self.derivative(x))
        n = self.at(x) - m * x
        return Polynomial(m, n)

    def integral(self,
                 a: REAL = None,
                 b: REAL = None,
                 grade: int = 1) -> REAL | 'Polynomial':
        """Returns the integral polynom if no a and b specified. Else returns
        the integral between a and b."""
        function = copy.deepcopy(self)
        for _ in range(grade):
            arg_list = []
            for i, e in enumerate(function):
                power = function.degree() - i + 1
                arg_list.append(Fraction(e, power))
            arg_list.append(0)
            function = Polynomial(*tuple(arg_list))
        if not a and b:
            return function
        elif a and b:
            return function.at(b) - function.at(a)
