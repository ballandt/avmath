"""AVMATH

Python package for symbolic calculations. Provides

- Number objects
- Linear algebra features
- Advanced calculus features

The complete avmath documentation can be found at
https://ballandt.github.io/p/avmath/docs

Concrete help for functions can be found with
>>> help(avmath.function)

Functions, classes and methods contain docstrings that can be read using the
help function (example above). Examples are indicated with three > signs
>>> 3 + 4
7

Subpackages
-----------

- algebra
  Linear algebra features

- calculus
  Calculus features

-----
Additional information and license terms can be found at
https://github.com/ballandt/avmath
"""

from .core.numbers import Real, Complex

from .version import version

__version__ = version
__author__ = "Camillo Ballandt"
__date__ = "2022/04/17"

del version
