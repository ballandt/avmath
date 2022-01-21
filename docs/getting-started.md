## Contents

* [What is avmath](#what-is-avmath)
* [How to use avmath](#how-to-use-avmath)
* [Important features](#important-features)
* [linear algebra]
* [analysis]

---
## What is avmath

Avmath is a Python library like `math` or `sys` and can be [imported](#how-to-use-avmath)
to use its functionalities.

Avmath provides features for the use of mathematics in Python and is 
oriented on a mathematical notation to simplify the process. It has got
submodules for analysis and linear algebra.

---
## How to use avmath
### Installation

Firstly, you must install avmath on your Python environment to use
it. You can use the package manager of your IDE to install avmath or 
use `pip`. Follow therefore the following steps:

* Open a terminal (command prompt) and verify if you can use `pip` by typing <br> ```pip --version``` <br> If this causes an error you should [set pip as environment variable](https://duckduckgo.com/set+pip+as+environment+variable). 
* If the output was the pip version number you can proceed: type `pip install avmath`

### Import

Now create a python file wherein you use avmath. If you want to 
use only the basic features you need only type the following:

```python
import avmath
```

If you also want to use the advanced algebra and analysis features
type
 ```python
# Imports basic features
import avmath

# Imports the advanced features
from avmath import algebra, analysis
```

Now you are able to use avmath.

---
## Important features
### Functions

But what to use avmath for? You can use avmath for calculations of
function values as sine or logarithms. These are accessible under:

```python
import avmath

a = avmath.sin(1)     # Returns the sine of 1
b = avmath.cos(2)     # Returns the cosine of 2
c = avmath.log(3, 6)  # Returns the logarithm with the base 6 of 3
```

All functions available are listed in the [documentation](avmath-root#arithmetic-functions).

### Fractions

Avmath contains a fraction class for the use of arithmetical fractions to minimize
the arithmetical error. The fractions can be used in combination with `int`, `float`
and `complex` numbers, but when combined with `float` or `complex` some features may
not be usable. Fractions are automatically reduced.

```python
import avmath

a = avmath.Fraction(22, 484) # Initialize a fraction

print(a) # Output: 1/22

b = a + 2 # b = 45/22
b /= 3    # b = 15/22
```
