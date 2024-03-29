The `avmath.__init__.py` file provides basic math features.
It can be used importing:
````python
# pip install avmath
import avmath
````
---
## Contents

* [Constants](#constants)
  * [Mathematical Constants](#backend-constants)
  * [Backend constants](#working-constants)
* [Fraction](#fraction)
  * [Attributes](#attributes)
  * [Methods](#methods)
  * [Static methods](#static-methods)
* [Arithmetic functions](#arithmetic-functions)
* [Backend functions](#backend-functions)

## Constants

### Mathematical constants

Avmath includes the following constants:

| Constant name                                                                                                                   | accessible name in module | accurate post comma decimal digits digits | Implemented in version | Last change |
|---------------------------------------------------------------------------------------------------------------------------------|---------------------------|------------------------------------------:|------------------------|-------------|
| Pi  (&pi;)                                                                                                                      | avmath.pi                 |                                        21 | v1.0.0                 | v3.0.0      |
| <span style="font-variant:small-caps;">Euler</span>`s number (_e_)                                                              | avmath.e                  |                                        21 | v1.0.0                 | v3.0.0      |
| Golden ratio (&phi;)                                                                                                            | avmath.phi                |                                        21 | v3.0.0                 | v3.0.0      |
| <span style="font-variant:small-caps;">Euler</span>-<span style="font-variant:small-caps;">Mascheroni</span> constant (&gamma;) | avmath.gamma              |                                        21 | v3.0.0                 | v3.0.0      |
| Two digit prime numbers                                                                                                         | avmath.two_digit_primes   |                                         - | v3.0.0                 | v3.0.0      |

---
### Backend constants

| Constant name                |                                                  Default value | usage                                                                                                                                                      | Implemented in version | Last change |
|------------------------------|---------------------------------------------------------------:|------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|-------------|
| avmath._TAYLOR_DIFFERENCE    |                                                          1e-16 | Loops of functions using <span style="font-variant:small-caps;">Taylor</span>-series calculate until the difference of the values is less equal this value | v3.0.0                 | v3.0.0      |
| avmath._MAX_CALCULATION_TIME |                                                              5 | Some loops may need a long time for calculation. These loops may not calculate longer as this time (in seconds)                                            | v3.0.0                 | v3.0.0      |
| avmath.REAL                  |                          typing.Union\[int, float, 'Fraction'] | Real numbers for type hints                                                                                                                                | v3.0.0                 | v3.0.0      |
| avmath.scope                 |  dictionary that contains all functions for REALs and Fraction | scope for analysis.Function                                                                                                                                | v2.0.0                 | v3.1.1      |

---
---
# Fraction

__Implemented in v3.0.0 | Last change v3.0.0__

Avmath's fractions are used to bypass the float inaccuracies.

## Attributes

| Attribute | Usage       | Implemented in version | Last Change |
|-----------|-------------|------------------------|-------------|
| `self.a`  | numerator   | v3.0.0                 | v3.0.0      |
| `self.b`  | denominator | v3.0.0                 | v3.0.0      |

## Methods 

All methods simulate an immutable type.

### Fraction.\_\_init__(numerator, denominator)

__Implemented in v3.0.0 | Last change v3.1.0__

Initialises Fraction with given numerator and denominator. Can contain float values too.

A fraction can be initialised by giving numerator and denominator as parameters
to the constructor.

````python
import avmath

my_fraction = avmath.Fraction(3, 7)
````

Now the fraction is initialised and is ready to be used. It is not 
automatically reduced and never reduced to int.

---

### Fraction.\_\_repr__()

__Implemented in v3.0.0 | Last change v3.0.0__

Returns string representation of `Fraction`. Gets always
printed in reduced shape.

````python
import avmath

a = avmath.Fraction(2, 4)
b = avmath.Fraction(6, 3)
print(a)
print(b)
````
gives the output
````
1/2

2
````

---
### Fraction.\_\_neg__()

__Implemented in v3.0.0 | Last change v3.0.0__

Returns negative fraction.

---
### Fraction.\_\_eq__(other)

__Implemented in v3.0.0 | Last change v3.0.0__

Returns whether Fraction is equal to given REAL.

---
### Fraction.\_\_lt__(other)

__Implemented in v3.0.0 | Last change v3.0.0__

Returns whether Fraction is less than given REAL.

---
### Fraction.\_\_gt__(other)

__Implemented in v3.0.0 | Last change v3.0.0__

Returns whether Fraction is greater than given REAL.

---
### Fraction.\_\_add__(other) / Fraction.\_\_radd__(other)

__Implemented in v3.0.0 | Last change v3.1.0__

Adds a Fraction with a REAL. Return value is always a Fraction.

---
### Fraction.\_\_sub__(other) / Fraction.\_\_rsub__(other)

__Implemented in v3.0.0 | Last change v3.1.0__

Subtracts a REAL from a Fraction. Returns always Fractions.

---
### Fraction.\_\_mul__(other) / Fraction.\_\_rmul__(other)

__Implemented in v3.0.0 | Last change v3.0.0__

Multiplies a Fraction with a REAL.

---
### Fraction.\_\_truediv__(other) / Fraction.\_\_rtruediv__(other)

__Implemented in v3.0.0 | Last change v3.1.0__

Divides a Fraction by a REAL.

---
### Fraction.\_\_pow__(power)

__Implemented in v3.0.0 | Last change v3.0.0__

Power operation for Fraction and REAL. If `power`=-1;
switches numerator and denominator.

---
### Fraction.\_\_rpow__(other)

__Implemented in v3.0.0 | Last change v3.0.0__

Power operation with Fraction as exponent.

---
### Fraction.\_\_mod__(other) / Fraction.\_\_rmod__(other)

__Implemented in v3.0.0 | Last change v3.0.0__

Modulo operation for Fraction and REAL.

---
### Fraction.\_\_int__()

__Implemented in v3.0.0 | Last change v3.0.0__

Returns integer representation of Fraction.

---
### Fraction.\_\_float__()

__Implemented in v3.0.0 | Last change v3.0.0__

Returns float representation of Fraction.

---

### Fraction.\_\_complex__()

__Implemented in v3.1.0 | Last change v3.1.0__

Returns float representation of Fraction.

---
### Fraction.\_\_abs__()

__Implemented in v3.0.0 | Last change v3.0.0__

Returns absolute of the Fraction.

---
### Fraction.reduce()

__Implemented in v3.0.0 | Last change v3.0.0__

Returns reduced fraction.

---
### Fraction.int_args()

__Implemented in v3.0.0 | Last change v3.0.0__

Returns whether the numerator and denominator are integers
or integer-like.

---
---
# Arithmetic functions

### is_prime(x)

__Implemented in: v3.0.0 | Last change: v3.0.0__

This function returns True if the integer `x` is a prime number.
The method checks, whether the integer less than the square root of
the argument is divisible by any number.

---

### is_even(x)

__Implemented in: v2.0.0 | Last change: v3.0.0__

Function returning True if the integer `x` is an even number. Used by `avmath.fac`.

---
### gcd(x, y)

__Implemented in: v3.0.0 | Last change: v3.0.0__

Function returning the greatest common divisor of two integers `x` and `y`.

---
### lcm(x, y)

__Implemented in: v3.0.0 | Last change: v3.0.0__

Function that returns the least common multiply of two integers `x` and `y`.

---
### sgn(x)

__Implemented in: v3.0.0 | Last change: v3.0.0__

Function that returns the signum of a number. For values <0 returns
-1 for 0 returns 0 and for values >0 returns 1

---
### fac(x \[, opt])

__Implemented in: v1.0.0 | Last change: v3.0.0__

Function returning the faculty x! of a number.

Parameters for `opt`:
* `'double'`: Returns double faculty [^1]


[^1]: Double faculty is an operation that factorizes all odd numbers less equal the value if the value is odd
and all even numbers less equal the value if it is even

---
### ln(x)

__Implemented in: v1.0.0 | Last change: v3.0.0__

Function that returns the natural logarithm of a number using 
<span style="font-variant:small-caps;">Taylor</span>-series. Takes 
only not negative values. Function is recommended to use for values
between `1e-300` and. `1e300`

| x domain            | precise post comma decimal places |
|---------------------|----------------------------------:|
| `1e-300` to `1e300` |                                12 |
| `1e-3` to `1e3`     |                                14 |

---
### log(x, base)

__Implemented in: v1.0.0 | Last change: v1.0.0__

Function that returns the logarithm of any base of a number.
Returns only ln(x) / ln(base) and in this way is dependent to
the natural logarithm.

_See [Natural logarithm](#lnx)_

---
### sin(x)

__Implemented in: v1.0.0 | Last change: v3.0.0__

Sine function using <span style="font-variant:small-caps;">Taylor</span>
-series. The function is recommended to use in the domain between
-100'000 and 100'000 because of inaccuracies of the modulo operator
that increase with the value.

| x-domain        | precise post comma decimal places |
|-----------------|----------------------------------:|
| `-1e4` to `1e4` |                                12 |
| `-1e5` to `1e5` |                                10 |
| `-1e6` to `1e6` |                              9-10 |

---
### cos(x)

__Implemented in: v1.0.0 | Last change: v3.0.0__

Function returning the cosine of a number using <span style="font-variant:small-caps;">Taylor</span>
-series. Shares modulo problem with sine and is also recommended between
-100'000 and 100'000.

| x-domain        | precise post comma decimal places |
|-----------------|----------------------------------:|
| `-1e4` to `1e4` |                                12 |
| `-1e5` to `1e5` |                                10 |
| `-1e6` to `1e6` |                              9-10 |

---
### tan(x)

__Implemented in: v1.0.0 | Last change: v3.0.0__

Function returning the tangent of a number calculating 
`sin(x) / cos(x)`. Shares modulo problem with sine and cosine
and is also inaccurate when approaching the asymptotes.

| x-domain                       | precise post comma decimal places |
|--------------------------------|----------------------------------:|
| `-1e4` to `1e4` (normal case)  |                                12 |
| `-1e5` to `1e5` (normal case)  |                                10 |
| `-1e6` to `1e6` (normal case)  |                              9-10 |
| `1e-3` difference to asymptote |                                10 |
| `1e-3` difference to asymptote |                                 7 |

---
### arcsin(x)

__Implemented in: v2.0.0 | Last change: v3.0.0__

Function returning the arc sine of a number -1 < x < 1 using
<span style="font-variant:small-caps;">Taylor</span>-series.
Calculation time increases when approaching |1|. Function may be stopped
by `_MAX_CALCULATION_TIME`. Values of -1 and 1 are manually set.

| Difference of x-value to `abs(1)` | precise post comma decimal places |
|-----------------------------------|----------------------------------:|
| `0.1` to `0.9`                    |                                15 |
| `0.01` to `0.1`                   |                                13 |
| `0.001` to `0.01`                 |                                 4 |

---
### arccos(x)

__Implemented in: v2.0.0 | Last change: v3.0.0__

Function returning the arc cosine of a number -1 < x < 1 using
arccos(x) = &pi; / 2 - arcsin(x). Due to the usage of `arcsin(x)`,
the accuracy stays the same.

| Difference of x-value to `abs(1)` | precise post comma decimal places |
|-----------------------------------|----------------------------------:|
| `0.1` to `0.9`                    |                                15 |
| `0.01` to `0.1`                   |                                13 |
| `0.001` to `0.01`                 |                                 4 |

---
### arctan(x)

__Implemented in: v2.0.0 | Last change: v3.0.0__

Function that returns the arc tangent of a number using two 
<span style="font-variant:small-caps;">Taylor</span>-series.
Calculation time increases when approaching |1|.

| absolute of x-domain           | precise post comma decimal places |
|--------------------------------|----------------------------------:|
| `0` to `0.9`                   |                             14-15 |
| at least 0.01 difference to 1  |                             13-14 |
| at least 0.001 difference to 1 |                                13 |
| `1`                            |                                 6 |

---
### sinh(x)

__Implemented in: v2.0.0 | Last change: v3.1.1__

Function returning the hyperbolic sine of a number using
<span style="font-variant:small-caps;">Taylor</span>-series.
Does only work for x values |x| < 710 then throws ArgumentError.

| x-domain        | precise decimal places |
|-----------------|-----------------------:|
| `-710` to `710` |                  14-15 |

---
### cosh(x)

__Implemented in: v2.0.0 | Last change: v3.1.1__

Function returning the hyperbolic cosine of a number using
<span style="font-variant:small-caps;">Taylor</span>-series.
Does only work for x values |x| < 710 then throws ArgumentError.

| x-domain        | precise decimal places |
|-----------------|-----------------------:|
| `-710` to `710` |                  14-15 |

---
### tanh(x)

__Implemented in: v2.0.0 | Last change: v3.0.0__

Function returning the hyperbolic tangent of a number using
sinh(x) / cosh(x).
When surpassing x-value 20, returns 1.0

| x-domain      | precise post comma decimal places |
|---------------|----------------------------------:|
| `-20` to `20` |                             14-15 |
| `abs(x) > 20` |                     (returns 1.0) |

---
### arsinh(x)

__Implemented in: v2.0.0 | Last change: v3.0.0__

Function that returns the inverse hyperbolic sine (_Areasinus hyperbolicus_)
of a number using Arsinh(x) = sgn(x) ln(|x| + sqrt(x² + 1)). Values
must lie between `-1e150` and `1e150` else cause OverflowError.

| x-domain            | precise post comma decimal places |
|---------------------|----------------------------------:|
| `-1e150` to `1e150` |                             13-14 |

---
### arcosh(x)

__Implemented in: v2.0.0 | Last change: v3.0.0__

Function returning the inverse hyperbolic cosine (_Areacosinus hyperbolicus_)
of a number x >= 1 using Arcosh(x) = ln(x + sqrt(x² - 1)). Values must lie 
between `-1e150` and `1e150` else cause OverflowError.

| x-domain            | precise post comma decimal places |
|---------------------|----------------------------------:|
| `-1e150` to `1e150` |                             13-14 |

---
### artanh(x)

__Implemented in: v2.0.0 | Last change: v3.0.0__

Function returning the inverse hyperbolic tangent (_Areatangens hyperbolicus_)
of a number -1 < x < 1. Therefore, uses Artanh(x) = 0.5 ln((1 + x) / (1 - x)).

| x-domain      | precise post comma decimal places |
|---------------|----------------------------------:|
| entire domain |                             12-14 |

---
---
## Backend functions

### _check_types(arg)

__Implemented in: v3.0.0 | Last change: v3.0.0__

Checks whether all items of the iterable object are of the
given types.