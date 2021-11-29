# Avmath algebra documentation

The `avmath.algebra` submodule provides functionalities for
linear algebra. It can be imported in the following way:
````python
# pip install avmath
from avmath import algebra
````
---
## Contents

Class | Usage | Implemented in version | Last change
--- | --- | --- | ---
[`Vector`](#vector) | Vector | v1.0.0 | v3.0.0
[`Matrix`](#matrix) | Matrix | v1.0.0 | v3.0.0
[`SLE`](#sle) | System of linear equations | v2.0.0 | v3.0.0

---
## `Vector`

The Vector-class is an inherited class of `Tuple`.
The methods of `Vector` simulate an immutable type.
It also defines the following methods:

Method | Parameters | Usage | Implemented in version | Last change
--- | --- | --- | --- | ---
`__init__` | `*args: Union[int, float, 'Fraction', 'Tuple]`, <br> `begin: Optional['Tuple'] = None`, <br> `end: Optional[Tuple] = None` | Initialisation of Vector object | v1.0.0 | v3.0.0
`__abs__` | - | Returns the absolute of the vector | v1.0.0 | v3.0.0 | v3.0.0
`__add__` | `other: 'Vector'` | Adds two vectors | v1.0.0 | v3.0.0
`__sub__` | `other: 'Vector'` | Subtracts a vector from another | v1.0.0 | v3.0.0
`__mul__` <br> `__rmul__` | `other: Union['Vector', int, float]` | Either calculates scalar product of two vectors or returns the scalar multiplication of a scalar and a vector | v1.0.0 | v3.0.0
`__truediv__` | `other: Union[int, float, 'Fraction']`| Vector divided by a scalar. Returns vector with Fraction values | v3.0.0 | v3.0.0
`__pow__` | `power: int` | Returns _p_ times scalar multiplied vector. p=0 returns unit vector | v3.0.0 | v3.0.0
`cross` | `other: 'Vector'` | Returns vector product of two three dimensional vectors | v1.0.0 | v3.0.0
`unit` | - | Returns specific unit vector | v1.0.0 | v3.0.0
`leading_zeroes` | - | Returns the number of leading zeroes of a vector | v3.0.0 | v3.0.0
`no_fractions` | - | Returns a copied vector that does not contain `Fraction` members | v3.0.0 | v3.0.0

Static method | Parameters | Usage | Implemented in version | Last change
--- | --- | --- | --- | ---
`spat` | `u: 'Vector`, <br> `v: 'Vector'`, <br> `w: 'Vector` | Returns the spat product of three vectors | v1.0.0 | v3.0.0
`angle` | `u: 'Vector'`, <br> `v: 'Vector'` | Calculates the angle (in radiant) between two vectors | v1.0.0 | v3.0.0

### Initialisation

Vector can be initialised giving either number values, vectorizing
a `Tuple` or by two `Tuple`s giving begin and end of the vector.

````python
from avmath import algebra

# Initialisation via numbers
u = algebra.Vector(1, 2, 4)

# Initialisation via vectorisation
a = algebra.Tuple(2, 5, 2)
v = algebra.Vector(a)

# Initialisation via begin and end
b = algebra.Tuple(-1, 2, 0)
c = algebra.Tuple(4, 5, 8)
w = algebra.Vector(begin=b, end=c)
````

---
## `Matrix`

The matrix class inherits from `Tuple` and also simulates
an immutable type. It defines following methods

Method | Parameters | Usage | Implemented in version | Last change
--- | --- | --- | --- | ---
`__init__` | `*args: Union[int, float, 'Fraction', 'Tuple]`, <br> `begin: Optional['Tuple'] = None`, <br> `end: Optional[Tuple] = None` | Initialisation of Vector object | v1.0.0 | v3.0.0
`__repr__` | - | Returns string of Matrix | v1.0.0 | v3.0.0
`__round__` | `n: int = None` | Returns matrix rounded to n digits | 1.0.0 | 2.0.0
`__neg__` | - | Returns negative matrix | v1.0.0 | v3.0.0
`__add__` | `other: 'Matrix'` | Adds two matrices | v1.0.0 | v2.0.0
`__sub__` | `other: 'Matrix'` | Subtracts a matrix from another | v1.0.0 | v2.0.0
`__mul__` <br> `__rmul__` | `other: Union['Matrix', 'Vector', int, float]` | Either multiplies two matrices, returns product of vector and matrix or returns the scalar multiplication of a scalar and a matrix | v1.0.0 | v3.0.0
`__truediv__` | `other: Union[int, float, 'Fracition']`|  Matrix divided by a scalar. Returns matrix with Fraction values | v3.0.0 | v3.0.0
`__pow__` | `power: int` | Returns _p_ times multiplied quadratic matrix. p=0 returns identity. p=-1 returns inverse matrix | v1.0.0 | v3.0.0
`no_fractions` | - | Returns a copied matrix that does not contain `Fraction` members | v3.0.0 | v3.0.0
`size` | - | Returns list with the number of rows in 0th place and the number of columns in the 1st place | v2.0.0 | v2.0.0
`dim` | - | Returns the dimension of the matrix (=m * n) | v1.0.0 | v2.0.0
`index` | `element: Union[int, float]` | Returns position of element in a matrix. If There are multiple, all get returned in a list | v1.0.0 | v1.0.0
`column` | `column_index: int` | Returns the column vector of given index | v1.0.0 | v3.0.0
`row` | `row_index: int` | Returns the row vector of given index | v1.0.0 | v3.0.0
`append` | `row=None`, <br> `column=None` | Returns a matrix with appended iterable | v1.0.0 | v3.0.0
`remove` | `row_index: int = None`, <br> `column_index: int = None` | Returns matrix without row or column specified | v1.0.0 | v3.0.0
`transpose` | - | Returns transposed matrix | v1.0.0 | v3.0.0
`det` <br> `__abs__` | - | Returns determinant of a matrix | v2.0.0 | v2.0.0
`cof` | - | Returns cofactor matrix | v2.0.0 | v2.0.0
`adj` | - | Returns adjunct of a matrix | v2.0.0 | v3.0.0
`inverse` | - | Returns inverse matrix| v2.0.0 | v3.0.0
`ref` | - | Returns row echelon form of a matrix | v3.0.0 | v3.0.0
`rank` | - | Returns rank of a matrix | v3.0.0 | v3.0.0
`rref` | - | Returns reduced row echelon form of a matrix | v3.0.0 | v3.0.0

Static method | Parameters | Usage | Implemented in version | Last change
--- | --- | --- | --- | ---
`create` | `m: int`, <br> `n: int` | Returns a matrix of size (m, n) with zeros only | v1.0.0 | v3.0.0
`create_identity` | `n: int` | Returns an identity matrix with n rows | v1.0.0 | v3.0.0

### Initialisation

The matrix can be initialised by lists or a vector.

````python
from avmath import algebra

# Initialisation via lists (normal)
A = algebra.Matrix([1, 2, 3], [4, 2, 5], [5, 4, 2])

# Initialisation via lists (better view)
B = algebra.Matrix([1, 2, 3],
                   [4, 2, 5],
                   [5, 4, 2])

# Initialisation via Vector
u = algebra.Vector(1, 3, 2)
C = algebra.Matrix(u)       # Vector gets column vector
D = algebra.Matrix(list(u)) # Vector gets row vector
````

---
## `SLE`

The **s**ystem of **l**inear **e**quations takes coefficients
and solves the system using inverse matrix. It inherits from `Matrix`.

Method | Parameters | Usage | Implemented in version | Last change
--- | --- | --- | --- | ---
`__init__` | `*args: list` |Initialises SLE | v2.0.0 | v3.0.0
`solve` | - | Returns a vector with all unknown variables | v2.0.0 | v3.0.0
`x` | `index: int` | Returns the unknown variable of given index | v2.0.0 | v2.0.0
