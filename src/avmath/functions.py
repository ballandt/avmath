from .geo import Point
import avmath
from . import ArgumentError


class f:

    def __init__(self, arg, x="x"):
        """Mathematical function. Enter argument as string."""
        self.formula = arg
        self.x = x

    def __repr__(self):
        return "f("+self.x+") = "+self.formula

    def __add__(self, other):
        if self.x != other.x:
            raise ArgumentError(other.x, self.x)
        ret_formula = self.formula + " + " + other.formula
        return f(ret_formula)

    def __replace(self):
        """Replaces intuitive elements with correct ones."""
        self.formula.replace("^", " ** ")

    def at(self, value):
        """Get function value at specific x value."""
        formula_at = self.formula.replace(self.x, str(value))
        ldict = {}
        exec("ret_val = "+formula_at, globals(), ldict)
        return ldict.get("ret_val")
