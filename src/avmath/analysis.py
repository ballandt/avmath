"""AVMATH ANALYSIS
AdVanced math  analysis submodule
implementing function features."""

from . import scope as _scope, _Point, log


class Point(_Point):
    """Point in coordinate system. (Two dimensions)"""

    def __init__(self, x, y):
        super().__init__(x, y)

    def __repr__(self):
        return str(tuple(self.__value))


class f:

    def __init__(self, arg):
        """Mathematical function. Enter argument as string."""
        self.formula = arg
        self.arg_scope = _scope

    def __repr__(self):
        return "f(x) = "+self.formula

    def __add__(self, other):
        ret_formula = self.formula + " + " + other.formula
        return f(ret_formula)

    def __neg__(self):
        return f("-(" + self.formula + ")")

    def __replace(self):
        """Replaces intuitive elements with correct ones."""
        self.formula.replace("^", " ** ")

    def set_scope(self, scope):
        """Sets a new dict as scope."""
        self.arg_scope = scope

    def append_scope(self, scope):
        """Appends dict to eval() scope. If appended scope contains elements
        that are already defined the appended elements are preferred.
        """
        self.arg_scope = {**self.arg_scope, **scope}

    def at(self, value):
        """Get function value at specific x value."""
        formula_at = self.formula.replace("x", "("+str(value)+")")
        return eval(formula_at, self.arg_scope)

    def max(self, xmin, xmax, step=None):
        """Finds maxima of a function in a given space"""
        if not step:
            step = (xmax - xmin) * 1e-4
        maxima = []
        position = xmin
        last_position = xmin
        b_last_position = xmin
        while position <= xmax:
            b_last_position = last_position
            last_position = position
            position += step
            digits = 12 #round(log(1/step, 10))
            if round(self.at(b_last_position), digits) < round(self.at(last_position), digits) and round(self.at(last_position), digits) > round(self.at(position), digits):
                print(self.at(last_position), step)
                if step < 1e-14:
                    maxima.append(Point(last_position, self.at(last_position)))
                else:
                    maxima.append(*tuple(self.max(b_last_position, position)))
        return maxima

    def min(self, xmin, xmax, step=None):
        """Finds minima of a function in a given spqce"""
        if not step:
            step = (xmax - xmin) * 1e-5
        neg_func = -self
        neg_maxima = neg_func.max(xmin, xmax, step)
        minima = []
        for e in neg_maxima:
            minima.append(Point(e[0], self.at(e[0])))
        return minima

    def numdif(self, x, h=None):
        """Returns numerical differentiation of function at a given x value"""
        if not h:
            h = 1e-10
        res = (self.at(x+h) - self.at(x)) / h
        return res

    def numint(self, a, b, n=None):
        """Returns the numerical integral of a function in a given space"""
        if not n:
            n = 1000
        res = (b - a) / n
        term = 0
        for i in range(n):
            xi = a + i*(b-a)/n + (b-a)/(2*n)
            term += self.at(xi)
        res *= term
        return res
