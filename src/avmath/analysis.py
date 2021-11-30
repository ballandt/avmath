"""AVMATH ANALYSIS
AdVanced math  analysis submodule
implementing function features."""

__all__ = ["Point", "Function"]

from typing import Union as _Union
from . import scope as _scope, REAL, sgn, Tuple


class Point(Tuple):
    """Point in coordinate system. (Two dimensions)"""

    def __init__(self, x: REAL, y: REAL):
        """Initialises the point. Give x and y value."""
        super().__init__(x, y)


class Function:
    """Mathematical function. Enter argument as string."""

    def __init__(self, arg: str):
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
        x_positions = [return_string.find("x")]
        while return_string.find("x", x_positions[-1]+1) != -1:
            x_positions.append(return_string.find("x", x_positions[-1]+1))
        for index, e in enumerate(x_positions):
            coefficient_position = e - 1 + index
            if coefficient_position == -1:
                continue
            try:
                _ = float(return_string[coefficient_position])
                return_string = return_string[:coefficient_position+1] + "*" + return_string[e+index:]
            except ValueError:
                break
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

    def max(self,
            xmin: REAL,
            xmax: REAL,
            steps: int = 100000) -> _Union[list, float]:
        """Finds maxima of a function in a given domain."""
        x_pos = xmin
        if abs(self.numdif(x_pos)) < 1e-3:
            return x_pos
        step = (xmax - xmin) / steps
        x_list = []
        for _ in range(steps):
            if sgn(self.numdif(x_pos)) != sgn(self.numdif(x_pos + step)):
                x_list.append((x_pos, x_pos + step))
            x_pos += step
        ret_list = []
        for e in x_list:
            ret_list.append(self.max(*e))
        return_list = []
        for e in ret_list:
            if self.scnd_numdif(e) < 0:
                return_list.append(Point(e, self.at(e)))
        return return_list

    def min(self,
            xmin: REAL,
            xmax: REAL,
            steps: int = 100000) -> list:
        """Finds minima of a function in a given domain."""
        neg_func = -self
        return neg_func.max(xmin, xmax, steps=steps)

    def root(self,
             xmin: REAL,
             xmax: REAL,
             step: int = 1000) -> list:
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

    def newton_method(self,
                      x_n: REAL,
                      steps: int = 50) -> float:
        """Newton's method to find root of function from given point x_n.
        x_{n+1} = x_n - f(x_n) / f'(x_n)
        """
        for _ in range(steps):
            x_np1 = x_n - self.at(x_n) / self.numdif(x_n)
            x_n = x_np1
        return x_n

    def numdif(self,
               x: REAL,
               h: REAL = 1e-5) -> float:
        """Returns numerical differentiation of function at a given x value."""
        return (self.at(x+h) - self.at(x-h)) / (2*h)

    def scnd_numdif(self,
                    x: REAL,
                    h: REAL = 1e-5):
        """Returns numerical second order differentiation of function at x value."""
        x1 = self.numdif(x-h)
        x2 = self.numdif(x+h)
        return (x2 - x1) / (2*h)

    def numint(self,
               a: REAL,
               b: REAL,
               n: int = 1000):
        """Returns the numerical integral of a function in a given space."""
        res = (b - a) / n
        term = 0
        for i in range(n):
            xi = a + i*(b-a)/n + (b-a)/(2*n)
            term += self.at(xi)
        res *= term
        return res
