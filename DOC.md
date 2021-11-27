# Avmath Documentation

The following passages document the functionality of  the avmath math module.
The documentation is tried to be held complete and accurate yet there
_may_ occur inaccuracies.
---

## Contents

* Arithmetics
  * [Fractions](#fraction)
  * [Functions](#arithmetic-functions)

---

## Constants

__Actual for avmath 3 (2021-12-01)__

Avmath includes the following constants:

Constant name | accessible name in module | accurate digits
--- | --- | ---
Pi  (&pi;)| `avmath.pi` | 21
Euler`s number (_e_) | `avmath.e` | 21
Golden ratio (&phi;) | `avmath.phi` | 21
Euler-Mascheroni constant (&gamma;)| `avmath.gamma` | 21

---

## Fraction

__Actual for avmath 3 (2021-12-01)__

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

### `is_prime`

This function returns True if the integer argument is a prime number.
The method checks, whether the integer less than the square root of
the argument is divisible by any number.

---

### `is_even`

Returns True if the argument is a even number. Used by `avmath.fac`

---
### `gcd`

Function returning the greatest common divisor of two integers.