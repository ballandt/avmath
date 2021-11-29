# Avmath Documentation

The following passages document the functionality of  the avmath math module.
The documentation is currently built and not yet complete. 
---

## Contents

* [Constants](#constants)
* Arithmetics
  * [Fractions](#fraction)
  * [Functions](#arithmetic-functions)

---

## Constants

### Mathematical constants

Avmath includes the following constants:

Constant name | accessible name in module | accurate post comma decimal digits digits | Implemented in version | Last change
--- | --- | ---: | --- | ---
Pi  (&pi;)| `avmath.pi` | 21 | v1.0.0 | v3.0.0
Euler`s number (_e_) | `avmath.e` | 21 | v1.0.0 | v3.0.0
Golden ratio (&phi;) | `avmath.phi` | 21 | v3.0.0 | v3.0.0
Euler-Mascheroni constant (&gamma;)| `avmath.gamma` | 21 | v3.0.0 | v3.0.0

---
### Working constants

Constant name | Default value | usage | Implemented in version | Last change
--- | ---: | --- | --- | ---
`_TAYLOR_DIFFERENCE` | `1e-16` | Loops of functions using <span style="font-variant:small-caps;">Taylor</span>-series calculate until the difference of the values is less equal this value | v3.0.0 | v3.0.0
`_MAX_CALCULATION_TIME` | `5` | Some loops may need a long time for calculation. These loops may not calculate longer as this time (in seconds) | v3.0.0 | v3.0.0

---
## Fraction

Avmath's fractions are used to bypass the float inaccuracies.

### Attributes and methods

The `Fraction` class contains following attributes:

Attribute | Usage | Last Change
--- | --- | ---
`self.a` | numerator | v3.0.0
`self.b` | denominator | v3.0.0

and the following methods

All methods simulate an immutable type.

Method | Parameters | Usage | implemented in version | Last Change
--- | --- | --- | --- | ---
`__init__` | `numerator` <br> `denominator` | Initialises Fraction with given numerator and denominator. Can contain float values too. | v3.0.0 | v3.0.0
`__repr__` | - | String representation of Fraction in the manner `a/b`. Always gets printed reduced. | v3.0.0 | v3.0.0
`__neg__` | - | Negation of Fraction | v3.0.0 | v3.0.0
`__eq__` | `other` | Checks equality of fractions (in case of two fractions prefers to compare reduced fraction| v3.0.0 | v3.0.0
`__lt__` | `other` | Checks which element is greater using float values | v3.0.0 | v3.0.0
`__gt__` | `other` | Checks which element is less | v3.0.0 | v3.0.0
`__add__` <br> `__radd__` | `other` | Adds either two fractions or a fraction and another number value | v3.0.0 | v3.0.0
`__sub__` <br> `__rsub__` | `other` | Subtracts either two fractions or a fractions and a number value| v3.0.0 | v3.0.0
`__mul__` <br> `__rmul__` | `other` | Multiplies fractions with another or with number values | v3.0.0 | v3.0.0
`__truediv__` <br> `__rtruediv__` | `other` | Divides fractions from another or from number values | v3.0.0 | v3.0.0
`__pow__` | `other` | Power operation for fractions. Power -1 changes numerator and denominator | v3.0.0 | v3.0.0
`__float__` <br> `__abs__` | - | Returns fraction's result as float | v3.0.0 | v3.0.0
`reduce` | - | Returns reduced fraction. Always stays Fraction. Can only be executed with integer values, else raises `ArgumentError`. | v3.0.0 | v3.0.0
`int_args` | - | Returns True if both numerator and denominator are integers | v3.0.0 | v3.0.0

---

### Initialisation

A fraction can be initialised by giving numerator and denominator as parameters
to the constructor.

````python
import avmath

my_fraction = avmath.Fraction(3, 7)
````

Now the fraction is initialised and is ready to be used. It is not 
automatically reduced and never reduced to int, but when printed, it
takes the most reduced shape

````python
import avmath

a = avmath.Fraction(2, 4)
b = avmath.Fraction(6, 3)
print(a)
print(b)
````
gives the output
````commandline
>>> 1/2
>>> 2
````
---

## Arithmetic functions

### `is_prime(x)`

__Implemented in: v3.0.0 | Last change: v3.0.0__

This function returns True if the integer `x` is a prime number.
The method checks, whether the integer less than the square root of
the argument is divisible by any number.

---

### `is_even(x)`

__Implemented in: v2.0.0 | Last change: v3.0.0__

Function returning True if the integer `x` is an even number. Used by `avmath.fac`.

---
### `gcd(x, y)`

__Implemented in: v3.0.0 | Last change: v3.0.0__

Function returning the greatest common divisor of two integers `x` and `y`.

---
### `lcm(x, y)`

__Implemented in: v3.0.0 | Last change: v3.0.0__

Function that returns the least common multiply of two integers `x` and `y`.

---
### `sgn(x)`

__Implemented in: v3.0.0 | Last change: v3.0.0__

Function that returns the signum of a number. For values <0 returns
-1 for 0 returns 0 and for values >0 returns 1

---
### `fac(x, opt=None)`

__Implemented in: v1.0.0 | Last change: v3.0.0__

Function returning the faculty x! of a number.

Parameters for `opt`:
* `'double'`: Returns double faculty [^1]


[^1]: Double faculty is an operation that factorizes
* all odd numbers less equal the value if the value is odd
* all even numbers less equal the value if it is even

---
### `ln(x)`

__Implemented in: v1.0.0 | Last change: v3.0.0__

Function that returns the natural logarithm of a number using 
<span style="font-variant:small-caps;">Taylor</span>-series. Takes 
only not negative values. Function is recommended to use for values
between `1e-300` and. `1e300`

x domain | precise post comma decimal places
--- | ---:
`1e-300` to `1e300` | 12
`1e-3` to `1e3` | 14

---
### `log(x, base)`

__Implemented in: v1.0.0 | Last change: v1.0.0__

Function that returns the logarithm of any base of a number.
Returns only `ln(x) / ln(base)` and in this way is dependent to
the natural logarithm.

_See [Natural logarithm](#lnx)_

---
### `sin(x)`

__Implemented in: v1.0.0 | Last change: v3.0.0__

Sine function using <span style="font-variant:small-caps;">Taylor</span>
-series. The function is recommended to use in the domain between
-100'000 and 100'000 because of inaccuracies of the modulo operator
that increase with the value.

x-domain | precise post comma decimal places
--- | ---:
`-1e4` to `1e4` | 12
`-1e5` to `1e5` | 10
`-1e6` to `1e6` | 9-10

---
### `cos(x)`

__Implemented in: v1.0.0 | Last change: v3.0.0__

Function returning the cosine of a number using <span style="font-variant:small-caps;">Taylor</span>
-series. Shares modulo problem with sine and is also recommended between
-100'000 and 100'000.

x-domain | precise post comma decimal places
--- | ---:
`-1e4` to `1e4` | 12
`-1e5` to `1e5` | 10
`-1e6` to `1e6` | 9-10

---
### `tan(x)`

__Implemented in: v1.0.0 | Last change: v3.0.0__

Function returning the tangent of a number calculating 
`sin(x) / cos(x)`. Shares modulo problem with sine and cosine
and is also inaccurate when approaching the asymptotes.

x-domain | precise post comma decimal places
--- | ---:
`-1e4` to `1e4` (normal case) | 12
`-1e5` to `1e5` (normal case) | 10
`-1e6` to `1e6` (normal case) | 9-10
`1e-3` difference to asymptote | 10
`1e-3` difference to asymptote | 7

---
### `arcsin(x)`

__Implemented in: v2.0.0 | Last change: v3.0.0__

Function returning the arc sine of a number -1 < x < 1 using
<span style="font-variant:small-caps;">Taylor</span>-series.
Calculation time increases when approaching |1|. Function may be stopped
by `_MAX_CALCULATION_TIME`. Values of -1 and 1 are manually set.

x-domain | precise post comma decimal places
--- | ---:
`-0.9` to `0.9` | 15
`-0.99` to `0.99` | 13
`-0.999` to `0.999` | 4

---
### `arccos(x)`

__Implemented in: v2.0.0 | Last change: v3.0.0__

Function returning the arc cosine of a number -1 < x < 1 using
arccos(x) = &pi; / 2 - arcsin(x). Due to the usage of `arcsin(x)`,
the accuracy stays the same.

x-domain | precise post comma decimal places
--- | ---:
`-0.9` to `0.9` | 15
`-0.99` to `0.99` | 13
`-0.999` to `0.999` | 4

---
### `arctan(x)`

__Implemented in: v2.0.0 | Last change: v3.0.0__

Function that returns the arc tangent of a number using two 
<span style="font-variant:small-caps;">Taylor</span>-series.
Calculation time increases when approaching |1|.

absolute of x-domain | precise post comma decimal places
--- | ---:
`0` to `0.9` | 14-15
at least 0.01 difference to 1 | 13-14
at least 0.001 difference to 1 | 13
`1` | 6

---
### `sinh(x)`

__Implemented in: v2.0.0 | Last change: v3.0.0__

Function returning the hyperbolic sine of a number using
<span style="font-variant:small-caps;">Taylor</span>-series.
Does only work for x values < 710 then throws OverflowError.

x-domain | precise decimal places
--- | ---:
`-710` to `710` | 14-15

---
### `cosh(x)`

__Implemented in: v2.0.0 | Last change: v3.0.0__

Function returning the hyperbolic cosine of a number using
<span style="font-variant:small-caps;">Taylor</span>-series.
Does only work for x values < 710 then throws OverflowError.

x-domain | precise decimal places
--- | ---:
`-710` to `710` | 14-15

---
### `tanh(x)`

__Implemented in: v2.0.0 | Last change: v3.0.0__

Function returning the hyperbolic tangent of a number using
sinh(x) / cosh(x).
When surpassing x-value 20, returns 1.0

x-domain | precise post comma decimal places
--- | ---:
`-20` to `20` | 14-15
`abs(x) > 20` | (returns 1.0)

---
### `arsinh(x)`

__Implemented in: v2.0.0 | Last change: v3.0.0__

Function that returns the inverse hyperbolic sine (_Areasinus hyperbolicus_)
of a number using Arsinh(x) = sgn(x) ln(|x| + sqrt(x² + 1)). Values
must lie between `-1e150` and `1e150` else cause OverflowError.

x-domain | precise post comma decimal places
--- | ---:
`-1e150` to `1e150` | 13-14

---
### `arcosh(x)`

__Implemented in: v2.0.0 | Last change: v3.0.0__

Function returning the inverse hyperbolic cosine (_Areacosinus hyperbolicus_)
of a number x >= 1 using Arcosh(x) = ln(x + sqrt(x² - 1)). Values must lie 
between `-1e150` and `1e150` else cause OverflowError.

x-domain | precise post comma decimal places
--- | ---:
`-1e150` to `1e150` | 13-14

---
### `artanh(x)`

__Implemented in: v2.0.0 | Last change: v3.0.0__

Function returning the inverse hyperbolic tangent (_Areatangens hyperbolicus_)
of a number -1 < x < 1. Therefore, uses Artanh(x) = 0.5 ln((1 + x) / (1 - x)).

x-domain | precise post comma decimal places
--- | ---:
entire domain | 12-14

---
## Algebra
The `avmath.algebra` submodule provides functionalities for
linear algebra. It contains the classes

Class | Usage | Implemented in version | Last change
--- | --- | --- | ---
[`Tuple`](#tuple) | Mathematical tuple. May also be interpreted as point | v3.0.0 | v3.0.0
`Vector` | Vector | v1.0.0 | v3.0.0
`Matrix` | Matrix | v1.0.0 | v3.0.0

### `Tuple`

The Tuple class is the base class of the algebra submodule.
It defines interaction methods inherited by the other classes.

#### Attributes and methods

Attribute | Usage | Implemented in version | Last change
--- | --- | --- | ---
`self._value` | Stores the values of the Tuple | v3.0.0 | v3.0.0

Method | Parameters | Usage | Implemented in version | Last change
--- | --- | --- | --- | ---
`__init__` | `*args: Union[int, float, list, Fraction]` | Initialisation of the object | v3.0.0 | v3.0.0
`__iter__` | - | Returns generator to convert Tuple to iterable object. | v3.0.0 | v3.0.0
`__getitem__` | `item` | Get item method for Tuple. | v3.0.0 | v3.0.0
`__repr__` | - | Returns string of Tuple in form `(a, b, c)` | v3.0.0 | v3.0.0
`__eq__` | `other: 'Tuple'` | Equality checker for Tuple | v3.0.0 | v3.0.0
`__len__` <br> `dim` | - | Returns the length or amount of dimensions of a Tuple | v3.0.0 | v3.0.0
`__neg__` | - | Returns negative Tuple | v3.0.0 | v3.0.0
`__add__` | `other: 'Tuple'` | Tuple addition method | v3.0.0 | v3.0.0
`__sub__` | `other: 'Tuple'` | Negative Tuple addition | v3.0.0 | v3.0.0
`__mul__` <br> `__rmul__` | `other: Union[int, float, 'Fraction']` | Scalar multiplication | v3.0.0 | v3.0.0
`__truediv__` | `other: Union[int, float, 'Fraction']` | Division by scalar. Returns fraction to bypass floats. | v3.0.0 | v3.0.0
`append` | `value: Union[int, float, 'Fraction']` | Returns Tuple with the value appended to `self._value` | v3.0.0 | v3.0.0
`no_fractions` | - | Returns Tuple that does not contain Fraction members | v3.0.0 | v3.0.0

Static method | Parameters | Usage | Implemented in version | Last change
--- | --- | --- | --- | ---
`dim_check` | `*args` | Returns `True` if all given values have the same amount of dimensions. Else returns `False` | v3.0.0 | v3.0.0
`triangulate` | `p: 'Tuple'`, <br> `q: 'Tuple'`, <br> `r: 'Tuple'` | Calculates the area between three points. | v3.0.0 | v3.0.0

#### Initialisation

Tuple can be initialised giving either numbers as parameters or a list.
```python
from avmath import algebra

a = algebra.Tuple(1, 2, 4)

b_list = [4, 3, 4.9]
b = algebra.Tuple(b_list)
```
Tuples are printed like built-in `tuple`s.

---
## Errors

Avmath provides its own errors representing specific issues in the usage.

Error | Cause | Implemented in version | Last change
--- | --- | --- | ---
`ArgumentError` | The argument given to a function or method is wrong. | v1.0.0 | v3.0.0
`algebra.DimensionError` | The arguments of an operation have a different amount of dimensions and therefore cannot be combined | v1.0.0 | v3.0.0
`algebra.GeometricalError` | A geometrical construction cannot be done due to false arguments | v1.0.0 | v3.0.0
`algebra.MatrixError` | Matrix-argument to an operation is inappropriate. Often handles size issues. | v1.0.0 | v3.0.0

### Warnings

Avmath also contains warnings using the logging module.

Warning | Cause | Implemented in version | Last change
--- | --- | --- | ---
`algebra.GeometricalWarning` | A geometrical instruction is possible yet there may be unwanted conditions. Can be disabled running the `GeometricalWarning.disable()` method. | v1.0.0 | v3.0.0

