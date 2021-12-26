The following passages document the
functionality of  the avmath math module.

Functions and methods are given with
Typehints to show the wanted input- and return
values. Some features are followed by code
examples.

---
## Contents

* [Installation](#installation)
* [Root](Avmath-root)
  * [Constants](Avmath-root#constants)
  * [Fractions](Avmath-root#fraction)
  * [Arithmetic functions](Avmath-root#arithmetic-functions)
* [Algebra](algebra.#avmath-algebra-documentation)
  * [Tuples](algebra#tuple)
  * [Vectors](algebra#vector)
  * [Matrices](algebra#matrix)
  * [Systems of linear equations](algebra#sle)
* [Errors](#errors)

---
---
## Installation

The avmath module is registered as a _PyPi_ project and
 can be downloaded via pip command:
```
pip install avmath
```

After that, the module can be imported as follows:
```python
import avmath
from avmath import analysis, algebra
```
---
It can also manually been downloaded from GitHub as the
[current release version](https://github.com/ballandt/avmath/releases)
or as archive of the actual code using the `code` button.
Then unpack the downloaded files and open command prompt in
the unpacked file:
````
pip install .
````

---

---
## Errors

Avmath provides its own errors representing specific issues in the usage.

| Error                      | Cause                                                                                                 | Implemented in version | Last change |
|----------------------------|-------------------------------------------------------------------------------------------------------|------------------------|-------------|
| `ArgumentError`            | The argument given to a function or method is wrong.                                                  | v1.0.0                 | v3.0.0      |
| `DimensionError`           | The arguments of an operation have a different amount of dimensions and therefore cannot be combined. | v1.0.0                 | v3.0.0      |
| `algebra.GeometricalError` | A geometrical construction cannot be done due to false arguments.                                     | v1.0.0                 | v3.0.0      |
| `algebra.MatrixError`      | Matrix-argument to an operation is inappropriate. Often handles size issues.                          | v1.0.0                 | v3.0.0      |

### Warnings

Avmath also contains warnings using the logging module.

| Warning                      | Cause                                                                                                                                          | Implemented in version | Last change |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|-------------|
| `algebra.GeometricalWarning` | A geometrical instruction is possible yet there may be unwanted conditions. Can be disabled running the `GeometricalWarning.disable()` method. | v1.0.0                 | v3.0.0      |