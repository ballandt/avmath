# Avmath analysis documentation

The `avmath.analysis` submodule provides functionalities for
analysis. It can be imported in the following way:
````python
# pip install avmath
from avmath import analysis
````
---
## Contents

* [`Point`](#point)
  * [Methods](#point-method)



* [`Function`](#function)
  * [Attributes](#function-attributes)
  * [Methods](#function-methods)

---
---
# Point

The Point class is the return type of some `Function` methods. It inherites from
`algebra.Tuple` and defines this extra method:

---
## Point methods

### Point.\_\_init__(x, y)

__Implemented in v1.0.0 | Last change v3.0.0__

Initialisation of point.

---
### Point.negative_y()

__Implemented in v3.1.0 | Last change v3.1.0__

Returns point with negative y coordinate.

---
---
## Function

The Function class provides functionalities for mathematical functions.

It has got the following attributes and methods:

### Function attributes

| Attribute       | Usage                              | Implemented in | Last change |
|-----------------|------------------------------------|----------------|-------------|
| self.term       | Stores the function term as string | v1.0.0         | v3.0.0      |
| self._arg_scope | Stores the scope given to `eval`   | v2.0.0         | v2.0.0      |

### Function methods

#### Function.\_\_init__(arg)

__Implemented in v1.0.0 | Last change in v3.0.0__

The constructor takes a string argument. This shall be the function
term. Because of the `_arg_scope` there can be given functions
of `avmath` without the module name. As definition variable
x must be used. It also provides some easy to use coefficient
and polynom features.

````python
from avmath import analysis

# Polynoms can be given in intentional form
f1 = analysis.Function("2*x**2 + 3*x - 4")
f2 = analysis.Function("2x^2 + 3x - 4")

# avmath functions
g = analysis.Function("sin(x)")
h = analysis.Function("artanh(x)")
````

---
### Function.\_\_repr__()

__Implemented in v1.0.0 | Last change in v3.0.0__

Gives string representation of function.

````python
from avmath import analysis

f = analysis.Function("3x^2 + sin(x)")
print(f)
````
gives the output
````
f(x) = 3x^2 + sin(x)
````

---
### Function.\_\_add__(other)

__Implemented in v1.0.0 | Last change in v3.1.0__

Adds two formulas.

---
### Function.\_\_sub__(other)

__Implemented in v1.0.0 | Last change in v3.0.0__

Subtracts two formulas. The entire second formula is set in brackets.

---
### Function.\_\_mul__(other) / Function.\_\_rmul__(other)

__Implemented in v1.0.0 | Last change in v3.1.0__

Multiplies two formulas or Function with REAL. Both are set in brackets.

---
### Function.\_\_truediv__(other)

__Implemented in v1.0.0 | Last change in v3.1.0__

Divides two formulas or a formula by a REAL. Both are set in brackets.

---

### Function.\_\_rtruediv__(other)

__Implemented in v3.1.0 | Last change in v3.1.0__

Divides a REAL by a formula. Both are set in brackets.

---
### Function.\_\_neg__()

__Implemented in v1.0.0 | Last change in v3.0.0__

Returns negative formula. Formula is just set in brackets
and preceded by a `-` sign.

---
### Function.replace(value)

__Implemented in v1.0.0 | Last change in v3.1.0__

Function replacing the intuitive elements (shown in `__init__`)
with the correct syntax and setting given value for x.

````python
from avmath import analysis

f = analysis.Function("3x^2 + sin(x)")
print(f.replace(5))
````
gives the output
````
3*(-5)**2 + sin((-5))
````
---
### Function.set_scope(scope)

__Implemented in v2.0.0 | Last change in v3.0.0__

Sets new scope for `eval`.

---
### Function.append_scope(scope)

__Implemented in v2.0.0 | Last change in v3.0.0__

Appends scope dictionary to scope.

---
### Function.at(value)

__Implemented in v1.0.0 | Last change in v3.0.0__

Returns the y-value of a function at a given x-value.

---
### Function.max(xmin, xmax \[, steps=1000])

__Implemented in v2.0.0 | Last change in v3.1.0__

Function returning the maxima of a function in a given x domain.
`steps` are the iterative steps made to find a change in the signum. Than uses
Newton-method derivative to find the maxima. Returns list
of Point values.

---
### Function.min(xmin, xmax \[, steps=1000])

__Implemented in v2.0.0 | Last change in v3.1.0__

Opposite of max. Returns minima in a given x domain.

---
### Function.root(xmin, xmax \[, step=1000])

__Implemented in v3.0.0 | Last change in v3.0.0__

Returns the roots of function in given x domain. Uses
<span style="font-variant:small-caps;">Newton</span>-method
to approach roots. Gives list of x-values back.

! WARNING: Due to backward compatibility last parameter remains `step`
not `steps` like in max and min.

---
### Function.newton_method(x_n \[, steps=50])

__Implemented in v3.0.0 | Last change in v3.1.0__

Returns result of `steps` times executed <span style="font-variant:small-caps;">Newton</span>-method.

---

### Function.newton_method_extrema(x_n \[, steps=50])

__Implemented in v3.1.0 | Last change in v3.1.0__

Executes derivative of Newton method: x_{n+1} = f'(x_n) / f''(x_n).

---

### Function.derivative(x \[, h=None])

__Implemented in v3.1.0 | Last change in v3.1.0__

Returns the derivative of the function at a given x. If no `h` specified,
calculates a height, but this may not be the optimal one.

---

### Function.second_derivative(x_n \[, h=1e-5])

__Implemented in v3.1.0 | Last change in v3.1.0__

Returns second derivative of the function at given x. `h` is set to 1e-5
what is mostly a good compromise of arithmetic error and numeric error.

---
### Function.integral(a, b \[, n=1000]\[, option=None])

__Implemented in v3.1.0 | Last change in v3.1.0__

Calculates the integral of the function between `a` and `b` with `n` steps.
With no option specified, uses rectangular formula. If `option="trapeze"`, uses 
trapeze formula.

---
### Function.num_dif(x \[, h=1e-5])

__Implemented in v1.0.0 | Last change in v3.0.0__

Returns numeric differentiation of the function at given x.

! WARNING: INACTIVE: Use Function.derivative instead.

---
### Function.second_num_dif(x \[, h=1e-5])

__Implemented in v3.0.0 | Last change in v3.0.0__

Returns numerically calculated second differentiation at given x.

! WARNING: INACTIVE: Use Function.second_derivative instead.

---
### Function.num_int(a, b \[, n=1000])

__Implemented in v1.0.0 | Last change in v3.1.0__

Numerically calculated integral between `a` and `b` with `n` steps.

! WARNING: INACTIVE: Use Function.integral instead.

---
### Function.tangent(x)

__Implemented in v3.1.0 | Last change in v3.1.0__

Returns a linear function in the form y = ax + b that lies tangent to
the function graph at a given x.

---
### Function.normal(x)

__Implemented in v3.1.0 | Last change in v3.1.0__

Returns a linear function in the form y = ax + b that lies normal to
the function graph at a given x.