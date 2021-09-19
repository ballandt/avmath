# AdVanced Math Changelog

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
    * `inverse()` method returns inversed matrix
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