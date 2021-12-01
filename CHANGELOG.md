# AdVanced Math Changelog

## 3.0.0 (2021-12-01)

Not all changes are listed yet.
#### API Changes
* redesigned function `avmath.pi()` to constant `avmath.pi`
* redesigned function `avmath.e()` to constant `avmath.e`
* deletion of class `avmath.algebra.Angle`
* `avmath.algebra.Vector.angle()` returns float
* deletion of class `avmath.algebra.Straight`
* renamed `avmath.algebra.Point` to `avmath.algebra.Tuple`
* changed location of vector product from `avmath.algebra.Vector.__pow__()` to `avmath.algebra.Vector.cross()`
* `avmath.algebra.Vector.pow()` returns vector multiplied n times by itself
* deletion of `avmath._Point` class
* renamed `avmath.analysis.f` to `avmath.analysis.Function`
* Deletion of `avmath.algebra.AmountOfDimensionsError`. `avmath.algebra.DimensionError`gets called instead.
* Deletion of `avmath.algebra.MatrixMultiplicationError`. `avmath.algebra.MatrixSizeError` gets called instead.
* `avmath.algebra.Matrix.row()` and `[...].Matrix.column()` return vectors
* renamed `avmath.algebra.Structure.circ()` to `[...].Structure.circumference`

#### Minor changes
* imports `time`-module for taylor-loops
* `_FLOAT_EQ` changed to value `1e-16`
* new constant `_TAYLOR_DIFFERENCE` as minimal difference between results for taylor-loops with value `1e-16`
* new constant `_MAX_CALCULATION_TIME` for maximum calculation time in taylor-loops with value 5 seconds
* `avmath.fac()` has parameter `opt` for double faculty
* `avmath._check_types()` checks if all members of tuple are of specified types
* `avmath.analysis.Function.newton_method()` for Newton's method from given x_n
* `avmath.analysis.Function.root()` returns all roots of the function in given domain
* `avmath.analysis.Function` allows `^` as power and coefficients
* new constant `avmath.phi` for golden ratio
* new constant `avmath.gamma` for Euler-Mascheroni constant
* new function `avmath.sgn()` for signum function
* `__all__` for `__init__.py`, `algebra.py` and `analysis.py`
* introduction of class `avmath.Fraction` for handling of fractions, particularly in linear algebra
* `avmath.algebra.Tuple`, `[...].Vector` and `[...].Matrix` classes contain `__truediv__()` functions returning `Fraction`
* `avmath.algebra.Tuple`, `[...].Vector` and `[...].Matrix` classes contain `no_fractions` functions returning objects with no fractions
* introduction of `avmath.algebra.Matrix.ref()` row echelon form
* introduction of `[...].Matrix.rank()` rank of a matrix
* introduction of `[...].Matrix.rref()` reduced row echelon form of a matrix
* introduction of `avmath.is_prime()` checking if integer is prime
* introduction of `avmath.two_digit_primes` list containing all primes < 100
* introduction of `avmath.gdc()` greatest common divisor
* introduction of `avmath.lcm()` least common multiply

#### Bug fixes
* `avmath.fac()` checks if input can be interpreted as integer
* `avmath.ln()` works properly in entire domain
* trigonometric functions use `while`-loops and `_TAYLOR_DIFFERENCE` to calculate to the best return value possible
* `avmath.cos()` works properly with negative values
* `avmath.analysis.Function.max()` does not raise RecursionError
* `avmath.algebra.Matrix.inverse()` works more accurately due to Fractions

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