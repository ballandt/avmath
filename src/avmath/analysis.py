"""AVMATH ANALYSIS
AdVanced math  analysis submodule
implementing function features."""

__all__ = ["Point", "Function"]

from . import scope as _scope, REAL, sgn, Fraction
from .algebra import Tuple


class Point(Tuple):
    """Point in coordinate system. (Two dimensions)"""

    def __init__(self, x: REAL, y: REAL):
        """Initialises the point. Give x and y value."""
        super().__init__(x, y)


class Polynom:
    def __init__(self, *args):
        self.factors = list(args)

    def __len__(self):
        return len(self.factors)

    def __repr__(self):
        ret_string = ""
        for i, e in enumerate(self.factors):
            power = self.grade() - i
            ret_string += f"{e}x^({power}) + " if i < self.grade() else f"{e}"
        return ret_string

    def grade(self):
        return len(self) - 1

    def append(self, value):
        ret_list = []
        for e in self.factors:
            ret_list.append(e)
        ret_list.append(value)
        return Polynom(*tuple(ret_list))

    def at(self, x):
        ret_value = 0
        for i, e in enumerate(self.factors):
            ret_value += e * x ** (self.grade() - i)
        return ret_value

    def derivative(self, x=None):
        derivative = Polynom(*tuple([e * (self.grade() - i) for i, e in enumerate(self.factors[:-1])]))
        if not x:
            return derivative
        elif x:
            return derivative.at(x)

    def integral(self, a=None, b=None, const=0):
        integral = Polynom(
            *tuple([Fraction(e, self.grade() - i + 1) for i, e in enumerate(self.factors)])).append(const)
        if not a and not b:
            return integral
        elif a and b:
            return integral.at(b) - integral.at(a)

    def root(self, xmin=None, xmax=None):
        if self.grade() == 2:
            a, b, c = (e for e in self.factors)
            roots = [(-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a), (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)]
            return roots


class Function:
    """Mathematical function. Enter argument as string."""

    def __init__(self, arg: str):
        """Initialisation of function. Enter function
        as string. Coefficient writing and ^ for power
        is allowed.
        See:
        https://github.com/ballandt/avmath/blob/master/docs/analysis.md#__init__self-arg-str
        """
        self.term = arg
        self._arg_scope = _scope

    def __repr__(self) -> str:
        """Returns string representation"""
        return f"f(x) = {self.term}"

    def __add__(self, other: 'Function') -> 'Function':
        """Adds two functions"""
        ret_formula = f"{self.term} + ({other.term})"
        return Function(ret_formula)

    def __sub__(self, other: 'Function') -> 'Function':
        """Subtracts two functions"""
        ret_formula = f"{self.term} - ({other.term})"
        return Function(ret_formula)

    def __mul__(self, other: REAL | 'Function') -> 'Function':
        """Multiplies two functions"""
        ret_formula = f"({self.term}) * ({other.term})"
        return Function(ret_formula)

    __rmul__ = __mul__

    def __truediv__(self, other: 'Function') -> 'Function':
        """Divide two functions"""
        ret_formula = f"({self.term}) / ({other.term})"
        return Function(ret_formula)

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
            if return_string[i-1] in "0123456789":
                return_string = f"{return_string[:i]}*{return_string[i:]}"
            i += 1
        return return_string.replace("x", "("+str(value)+")")

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

    def max(self, xmin: REAL, xmax: REAL, steps: int = 1000):
        """Finds maxima of a function using changed newton method:
        x_{n+1} = x_n - f'(x_n) / f''(x_n)
        """
        sgn_step = (xmax - xmin) / steps
        x_pos = xmin
        candidates = []
        for i in range(steps):
            if sgn(self.num_dif(x_pos)) != sgn(self.num_dif(x_pos+sgn_step)):
                candidates.append(x_pos)
            x_pos += sgn_step
        return_list = []
        for ele in candidates:
            value = Point(self.newton_method_extrema(ele), self.at(self.newton_method_extrema(ele)))
            if value not in return_list and self.second_num_dif(ele) < 0:
                return_list.append(value)
        return return_list

    def min(self, xmin: REAL, xmax: REAL, steps: int = 1000) -> list:
        """Finds minima of a function in a given domain."""
        neg_func = -self
        return [-e for e in neg_func.max(xmin, xmax, steps)]

    def root(self, xmin: REAL, xmax: REAL, step: int = 1000) -> list:
        """Find roots of functions with f(x) = 0.
        Returns only x-coordinate.
        """
        sgn_step = (xmax - xmin) / step
        x_pos = xmin
        candidates = []
        for i in range(step):
            if sgn(self.at(x_pos)) != sgn(self.at(x_pos+sgn_step)):
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
            x_n = x_n - self.at(x_n) / self.num_dif(x_n)
        return x_n

    def newton_method_extrema(self, x_n):
        for _ in range(50):
            x_n = x_n - self.num_dif(x_n) / self.second_num_dif(x_n)
        return x_n

    def derivative(self, x):
        differences = []
        cached_derivative = self.num_dif(x, 10**-16)
        for i in range(-15, 2):
            try:
                derivative = self.num_dif(x, 10**i)
            except Exception:
                continue
            dif = abs(cached_derivative - derivative)
            differences.append(dif)
            cached_derivative = derivative
        best = -15 + differences.index(min(*differences))
        return self.num_dif(x, 10**best)

    def second_num_dif(self, x: REAL, h: REAL = 1e-5) -> float:
        """Returns numerical second order differentiation of function at x value."""
        x1 = self.num_dif(x-h)
        x2 = self.num_dif(x+h)
        return (x2 - x1) / (2*h)

    def num_dif(self, x: REAL, h: REAL = 1e-5) -> float:
        """Returns numerical second order differentiation of function at x value."""
        return (- self.at(x + 2*h) + 8*self.at(x + h) - 8 * self.at(x - h) + self.at(x - 2*h)) / (12*h)

    def num_int(self, a: REAL, b: REAL, n: int = 1000) -> float:
        """Returns the numerical integral of a function in a given space."""
        res = (b - a) / n
        term = 0
        for i in range(n):
            xi = a + i*(b-a)/n + (b-a)/(2*n)
            term += self.at(xi)
        res *= term
        return res
