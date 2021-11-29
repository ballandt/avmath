# Avmath analysis documentation

The `avmath.analysis` submodule provides functionalities for
analysis. It can be imported in the following way:
````python
# pip install avmath
from avmath import analysis
````
---
## Contents

Class | Usage | Implemented in version | Last change
--- | --- | --- | ---
[`Point`](#point) | Twodimensional point in the ccordinate system | v1.0.0 | v3.0.0
[`Matrix`](#matrix) | Function | v1.0.0 | v3.0.0

---
## `Point`

The Point class is the return type of some `Function` methods. It inherites from
`Tuple` and defines this extra method:

Method | Parameters | Usage | Implemented in version | Last change
--- | --- | --- | --- | ---
`__init__` | `x: Union[int, float, 'Fraction']`, <br> `y: Union[int, float, 'Fraction']` | Initialisation of point | v1.0.0 | v3.0.0

---
## `Function`

The Function class provides functionalities for mathematical functions.
