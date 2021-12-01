<img src="docs/avmath.svg" width="400" title="avmath" class="center">

---

_Avmath_ is a python library for mathematics. 

---
## Contents

* [Description](#description)
* [Features](#features)
* [Installation](https://github.com/ballandt/avmath/blob/master/docs/README.md#installation)
* [Documentation](https://github.com/ballandt/avmath/tree/master/docs)
* [Changelog](https://github.com/ballandt/avmath/blob/master/CHANGELOG.md)
* [Developments](https://github.com/ballandt/avmath/blob/master/DEVELOPMENTS.md)
* [Releases](https://www.github.com/ballandt/avmath/releases)
---

## Description
### Information

Category | Data
------------ | -------------
Name | avmath
PyPi name  | [avmath](https://pypi.org/project/avmath/)
Author | Camillo Ballandt
Release version | [2.0.0](https://www.github.com/ballandt/avmath/releases/tag/v2.0.0)
Developing version | [3.0.0](https://github.com/ballandt/avmath/blob/master/DEVELOPMENTS.md)
Requirements | Python 3.10

### Extended description

Avmath is a library project that uses python algorithms to numerically solve
math problems. Its interface is based on mathematical habits of
writing. It particularly concentrates on the concepts of linear algebra
and analysis, but also generates its own functions based on Taylor-series.

Avmath 2.0 ended the former dependency to the math module. All mathematical
problems are now solved independently. There have been changes in function
names and parameters because of necessary syntax changes. Also, a function
implementation was made. The Taylor-functions sometimes lack of speed and
accuracy.

The first drafts of avmath are dated on the 22nd of March 2021.

---
## Features

* [Basic features](https://www.github.com/ballandt/avmath/blob/master/scr/avmath/__init__.py)
  * __fractions__
    * Basic operations
    * reducing
  * __primes__
    * detection of primes
    * primes < 100
  * __trigonometry__
    * trigonometrical functions (sine, cosine, tangent)
    * inverse trigonometrical functions (arc sine, arc cosine, arc tangent)
    * hyperbolic functions (hyperbolic sine, hyp. cosine, hyp. tangent)
    * inverted hyperbolic functions (inverse hyp. sine, inv. hyp. cosine, inv. hyp. tangent)
  * __faculties__
    * simple and double faculties
  * __constants__
    * pi
    * e
    * phi
    * gamma

* [Linear algebra](https://www.github.com/ballandt/avmath/blob/master/src/avmath/algebra.py)
  * __tuples__
    * Basic iterable operations
    * basic mathematical operations
    * parent class for vector and matrix
  * __vectors__
    * basic operations
    * vector product, spat product
    * angle between vectors
  * __matrices__
    * matrix visual representation
    * basic operations
    * determinant
    * transposed matrix
    * cofactor matrix
    * adjunct of matrix
    * inverse matrix
    * row echelon form, reduced row echelon form
    * rank of a matrix
  * __point structures__
    * circumference
    * area
  * __systems of linear equations__

* [Analysis](https://www.github.com/ballandt/avmath/blob/master/src/avmath/analysis.py)
  * __functions__
    * usual input possibility
    * basic calculations
    * maxima / minima
    * roots
    * numerical first and second differentiation
    * numerical integral