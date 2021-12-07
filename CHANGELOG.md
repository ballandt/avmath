# AdVanced Math Changelog

## Contents

* avmath 3
  * [3.1.0](#310-planned-for-2021-12-18)
  * [3.0.0](#300-2021-12-01)
* avmath 2
  * [2.0.0](#200-2021-10-24)
  * [2.0.0-b2](#200-beta2-2021-09-19)
* avmath 1
  * [1.2.0](#120-2021-09-10)
  * [1.1.0](#110-2021-09-01)
  * [1.0.0](#100-2021-09-01)
* table of releases

---
## 3.1.0 (Planned for 2022-01-01)

#### Minor changes

* `__init__`
  * `Fraction`
    * fractions can be used for initialisation
* `analysis
  * new class `Polynom`
    * `__init__` with coefficients
    * `__repr__` for string representation
    * `__len__` for the amount of coefficients
    * `grade` for grade of the polynom. Is `__len__`-1
    * `at` for function values
    * `append` returns polynom with appended coefficient
    * `derivatvive`
      * returns either differentiated polynom or value if `x` is specified
    * `integral`
      * returns either integrated polynom or value if `a` and `b` specified
  * `Function`
    * new method `newton_method_extrema`
      * uses newton method with differentiations for the calculation of extrema

#### Patch level changes

* `__init__`
  * `Fraction`
    * `__truediv__`
      * formula fixes
* `analysis`
  * `Function`
    * `max`-method uses newton method and is much faster and more accurate
    * `numdif` developments for accuracy
* `algebra`
  * `Structure`
    * `area`
      * fixes for angles > 180°

---
## 3.0.0 (2021-12-01)

There may be some changes missing.
#### API Changes

* `__init__`
  * redesigned function `avmath.pi()` to constant `avmath.pi`
  * redesigned function `avmath.e()` to constant `avmath.e`
  * `_FLOAT_EQ`
    * __Deletion__
  * `_Point`
    * __Deletion__
  * `DimensionError`
    * moved from `algebra`
* `algebra`
  * `Angle`
    * __Deletion__
  * `Vector`
    * `avmath.algebra.Vector.angle()` returns float
    * changed location of vector product from `__pow__` to `cross`
    * `pow` returns vector multiplied n times by itself
  * `Straight`
    * __Deletion__
  * `Point` -> `Tuple`
    * renamed `Point` to `Tuple`
  * `AmountOfDimensionsError`
    * __Deletion__
    * `DimensionError`gets called instead.
  * `MatrixMultiplicationError`
    * __Deletion__
    * `MatrixError` gets called instead
  * `Matrix`
    * `row`
      * returns `Vector` type
    * `column`
      * returns `Vector` type
  * `Structure`
    * `circ` -> `circumference`
      * renamed `circ` to `circumference`
* `analysis`
  * `f` -> `Function`
    * renamed `f` to `Function`

#### Minor changes

* `__all__` for `__init__.py`, `algebra.py` and `analysis.py`
* `__init__`
  * imports time module
  * new constant `_TAYLOR_DIFFERENCE` as minimal difference between results for taylor-loops with value `1e-16`
  * new constant `_MAX_CALCULATION_TIME` for maximum calculation time in taylor-loops with value 5 seconds
  * `fac` 
    * parameter `opt` for double faculty
  * new function `_check_types`
    * checks if all members of tuple are of specified types
  * new constant `phi`
    * for golden ratio
  * new constant `gamma`
    * for Euler-Mascheroni constant
  * new function `sgn`
    * for signum function
  * new function `is_prime`
    * checks whether integer is a prime
  * new constant `two_digit_primes`
    * contains all two digit primes
  * new function `gcd`
    * returns the greatest common divisor of two integers
  * new function `lcm`
    * returns the least common multiply of two integers
  * new class `Fraction`
    * handling of fractions, particularly in linear algebra
    * see [Documentation](https://github.com/ballandt/avmath/wiki/Avmath-root#fraction) for all methods
* `analysis`
  * `Function`
    * new function `newton_method`
      * for Newton's method from given x_n
    * new function `root`
      * returns all roots of the function in given domain
    * new function `replace`
      * allows `^` as power and coefficients
    * new method `second_num_dif`
      * numerical second differentiation
* `algebra`
  * `Tuple`
    * new method `truediv`
      * returns tuple divided by scalar for less float inaccuracies
    * new method `no_fractions`
      * returns copy of `Tuple` with no fractions
  * `Vector`
    * new method `truediv`
      * see `Tuple`
    * new method `no_fractions`
      * see `Tuple`
  * `Matrix`
    * new method `truediv`
      * see `Tuple`
    * new method `no_fractions`
      * see `Tuple`
    * new method `ref`
      * returns row echelon form
    * new method `rank`
      * returns rank of the matrix
    * new method `rref`
      * returns reduced row echelon form of the matrix

#### Bug fixes

* `__init__`
  * `fac`
    * checks if input _can be interpreted_ as integer
  * `ln` works properly and much faster
  * trigonometric functions use `while`-loops and `_TAYLOR_DIFFERENCE` to calculate to the best return value possible
  * `cos` works properly with negative values
* `algebra`
  * `Matrix`
    * `inverse`
      * works more accurately due to fractions
  * `arsinh`
    * works in negative domain due to correct spelling of formula
  * `artanh`
    * does not allow value 1 only to crash afterwards
  * `tanh`
    * surpassing a value of 20 simply returns 1 instead of calculating (and crashing)
  * `arcsin`
    * new structure for formula
    * does not crash at 710, but is stopped by the maximal time control

---
## 2.0.0 (2021-10-24)

Avmath 2.0 ended the former dependency to the math module. All mathematical
problems are now solved independently. There have been changes in function
names and parameters because of necessary syntax changes. Also, a function
implementation was made. The Taylor-functions sometimes lack of speed and
accuracy.

#### API Changes
* `avmath.sin()` takes only x argument
* `avmath.pi()` takes no arguments
* `avmath.e()` takes no arguments
* renamed `avmath.arcsinh` to `avmath.arsinh`
* renamed `avmath.arccosh` to `avmath.arcosh`
* renamed `avmath.arctanh` to `avmath.artanh`
* renamed `avmath.geo` to `avmath.algebra`
* renamed `avmath.funtions` to `avmath.analysis`

#### Minor Changes
* All functions use Taylor series instead of `math`-module
* `avmath.scope` dictionary with avmath functions for `eval` locals
* `avmath._Point` prototype for points in submodules
* `avmath.analysis`:
  * `avmath.analysis.Point` class for point values
  * `avmath.f.__neg__()` for negative function
  * `avmath.f.at()` uses `avmath.scope` for locals
  * `avmath.f.set_scope()` to set scope to different dictionary
  * `avmath.f.append_scope()` to append dictionary to scope
  * `avmath.f.max()` to find maximum of a function in a certain space
  * `avmath.f.min()` to find minimum of a function in a certain space
  * `avmath.f.numdif()` to find numerical differentiation at an x value
  * `avmath.f.numint()` to find numerical integral in a certain space
  * `avmath.Point` inherits from `avmath._Point` prototype
* `avmath.algebra`:
  * `avmath.algebra.Point` inherits from `avmath._Point`
  * `avmath.Matrix.__contains__()` function created
  * `avmath.Matrix.__setitem__()` function created
  * `avmath.Matrix.__round__()` function created

---
## 2.0.0-beta2 (2021-09-19)
#### API Changes
* renamed `avmath.geo` -> `avmath.lina`
* renamed `avmath.functions` -> `avmath.ana`
* deletion of `avmath.lina.Vector.__ne__()`
#### Minor changes
* `avmath.lina`:
  * `avmath._FLOAT_EQ` to compare float values
  * `avmath.lina.Angle.__eq__()` method uses `avmath._FLOAT_EQ`
  * `avmath.lina.Angle.__eq__()` method uses `avmath._FLOAT_EQ`
  * `avmath.line.Vector.__eq__()` method uses `avmath._FLOAT_EQ`
  * `avmath.lina.Matrix`:
    * `__init__()` `size`, `rows`, `columns` removed
    * `__init__()` can transform Vector to Matrix
    * `__repr__()` uses brackets for better view
    * `__repr__()` better algorithm for spaces
    * `__eq__()` uses `avmath._FLOAT_EQ`
    * `__pow__()` with ^-1 leads to `inverse()`
    * `size()` method returns size in format `[m, n]`
    * `at()` method returns element of given index
    * `remove()` method returns a matrix with removed row or column
    * `det()` method returns the determinant of a matrix
    * `cof()` method returns cofactor matrix
    * `adj()` method returns cofactor matrix
    * `inverse()` method returns inverted matrix
  * `avmath.lina.SLE` system of linear equations inherited from matrix:
    * `__init__()` method creates matrix with parameters and results
    * `solve` method returns matrix with all unknowns
    * `x()` method returns unknown of given index

---
## 1.2.0 (2021-09-10)
* Github-PyPi coordination
* valid metadata
* link and documentation fixes

---
## 1.1.0 (2021-09-01)
* Angle class
  * Modes DEG, RAD, GRA
  * Angle.get() method

---
## 1.0.0 (2021-09-01)
Upload to github.

---
## Before v1.0.0

When the evmath project was uploaded to github, its version
number was reset to 1.0.0 . Previously it was on version number
1.8.0 , but lacking a valid changelog.

---
## Table of releases

Release | Name | Date | Integral developments
:--- | --- | ---: | ---
[3.1.0](#310-planned-for-2022-01-01) | - | 2022-01-01 | Completions in `analysis`
[3.0.0](#300-2021-12-01) | illumination | 2021-12-01 | implementation of `Fraction`, Gauss-features for matrices
[2.0.0](#200-2021-10-24) | repensé | 2021-10-24 | independence from math module with Taylor-series, matrix features
[2.0.0-b2](#200-beta2-2021-09-19) | - | 2021-09-19 | not yet stable version of 2.0.0
[1.2.0](#120-2021-09-10) | - | 2021-09-10 | coordination of elements
[1.1.0](#110-2021-09-01) | First release | 2021-09-01 | `Angle` class in former `geo`
[1.0.0](#100-2021-09-01) | - | 2021-09-01 | Upload to GitHub