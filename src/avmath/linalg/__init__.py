"""AVMATH LINEAR ALGEBRA

This module gives access to the avmath linear algebra features. Contains the
classes

- vector
- matrix

and the functions

- angle
- mat
- solve
- vec


View https://ballandt.github.io/p/avmath/docs/linalg.html for documentation.

vector
------

Datatype for complex vector calculations. Performs symbolic operations over the
given elements. It is not recommended to initiate the class manually, but to
use the `vec` function. See
https://ballandt.github.io/p/avmath/docs/linalg.html or `help(vector) for
method documentation.


angle
-----

Function to determine the angle between two real vectors. Takes Sized as
arguments.

>>> angle((2, 3, 1), (-6, 3, 0))
1.6906056111094407

Set deg=True to receive output in degrees

>>> angle((2, 3, 1), (-6, 3, 0), deg=True)
96.86456633770632

Not vector like arguments cause TypeError, different dimensions or complex
values ValueError.

vec
---

Function for the initialisation of vectors. Checks the arguments and gives the
possibility to enter Sized or lose values.

>>> vec(2, 4, 3)
(2, 4, 3)

>>> vec([2, 4, 3])
(2, 4, 3)

NaN arguments cause TypeError.
"""

from ..core.vectors import vector, vec, angle
