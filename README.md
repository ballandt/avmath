# AdVanced Math

---
_Avmath_ is a python library for mathematics.

## Contents

* [Description](#description)
  * [General information](#information)
  * [Extended description](#extended-description)
* [Features](#features)
* [Changelog](CHANGELOG.md)
* [Developments](DEVELOPMENTS.md)
* [Releases](https://www.github.com/ballandt/avmath/releases)
---

## Description
### Information

Category | Data
------------ | -------------
Author | Camillo Ballandt
Release version | [2.0.0](https://www.github.com/ballandt/avmath/releases/tag/2.0.0)
Developing version | [3.0.0](https://github.com/ballandt/avmath/blob/master/DEVELOPMENTS.md)
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

the avmath project started on 22nd of March 2021.

---
## Features

* [Basic features](https://www.github.com/ballandt/avmath/blob/master/scr/avmath/__init__.py)
  * trigonometry
  * faculties
  * constants

* [Linear algebra](https://www.github.com/ballandt/avmath/blob/master/src/evmath/algebra.py)
  * vectors
  * matrices
  * point structures
  * systems of linear equations

* [Analysis](https://www.github.com/ballandt/avmath/blob/master/src/evmath/analysis.py)
  * mathematical functions
  * maxima / minima
  * roots
  * numerical differentiation and integral