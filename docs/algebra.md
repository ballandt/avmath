# Avmath algebra documentation

The `avmath.algebra` submodule provides functionalities for
linear algebra. It can be imported in the following way:
````python
# pip install avmath
from avmath import algebra
````
---
## Contents

* [`Tuple`](#tuple)
  * [Attributes](#attributes)
  * [Methods](#methods)
    * [`__init__`](#__init__self-args-real--list)
    * [`__iter__`](#__iter__self)
    * [`__getitem__`](#__getitem__self-item)
    * [`__repr__`](#__repr__self---str-tuple)
    * [`__eq__`](#__eq__self-other-tuple---bool)
    * [`__len__`/`dim`](#__len__self---int--dim)
    * [`__neg__`](#__neg__self)
    * [`__add__`](#__add__self-other-tuple---tuple)
    * [`__sub__`](#__sub__self-other-tuple---tuple)
    * [`__mul__`/`__rmul__`](#__mul__self-other-real--__rmul__)
    * [`__truediv__`](#__truediv__self-other-real---tuple)
    * [`append`](#appendself-value-real)
    * [`no_fractions`](#no_fractionsself---tuple)
  * [Static methods](#static-methods)
    * [`dim_check`](#dim_checkargs---bool)


* [`Vector`](#vector)
  * [Methods](#vector-methods)
    * [`__init__`](#__init__self-args-real--tuple-begin-optionaltuple--none-end-optionaltuple--none)
    * [`__abs__`](#__abs__self---float)
    * [`__add__`](#__add__self-other-vector---vector)
    * [`__sub__`](#__sub__self-other-vector---vector)
    * [`__mul__`/`__rmul__`](#__mul__self-other-real--vector---real--vector--br-__rmul__)
    * [`__truediv__`](#__truediv__self-other-real)
    * [`__pow__`](#__pow__self-power-int---real--vector)
    * [`cross`](#crossself-other-vector---vector)
    * [`unit`](#unitself---vector)
    * [`leading_zeroes`](#leading_zerosself---int)
    * [`no_fractions`](#no_fractionsself---vector)
  * [Static methods](#vector-static-methods)
    * [`spat`](#spatu-vector-v-vector-w-vector---float)
    * [`anlge`](#angleu-vector-v-vector---float)


* [`Structure`](#structure)
  * [Attributes](#structure-attributes)
  * [Methods](#structure-methods)
    * [`__init__`](#__init__self-args-tuple)
    * [`flat`](#flatself---bool)
    * [`circumference`](#circumferenceself---float)
    * [`area`](#areaself-opt-str--none)
  * [Static methods](#structure-static-methods)
    * [`triangulate`](#triangulatep-tuple-q-tuple-r-tuple---float)


* [`Matrix`](#matrix)
  * [Methods](#matrix-methods)
    * [`__init__`](#__init__self-args-listreal--vector)
    * [`__repr__`](#__repr__self---str)
    * [`__round__`](#__round__self-n-int--none---matrix)
    * [`__neg__`](#__neg__self---matrix)
    * [`__add__`](#__add__self-other-matrix---matrix)
    * [`__sub__`](#__sub__self-other-matrix---matrix)
    * [`__mul__`/`__rmul__`](#__mul__self-other-real--vector--matrix---unionmatrix-vector--br-__rmul__)
    * [`__truediv__`](#__truediv__self-other-real---matrix)
    * [`__pow__`](#__pow__self-power-int---matrix)
    * [`size`](#sizeself-option-str--none---list)
    * [`dim`](#dimself---int)
    * [`index`](#indexself-element-real---list)
    * [`no_fractions`](#no_fractionsself---matrix)
    * [`column`](#columnself-column_index-int---vector)
    * [`row`](#rowself-row_index-int---vector)
    * [`append`](#appendself-rownone-columnnone---matrix)
    * [`remove`](#removeself-row_index-int--none-column_index-int--none---matrix)
    * [`transpose`](#transposeself---matrix)
    * [`det`](#detself---real--br-__abs__)
    * [`cof`](#cofself---matrix)
    * [`adj`](#adjself---matrix)
    * [`inverse`](#inverseself---matrix)
    * [`ref`](#refself---matrix)
    * [`rank`](#rankself---int)
    * [`rref`](#rrefself---matrix)
  * [Static methods](#matrix-static-methods)
    * [`create`](#createm-int-n-int---matrix)
    * [`create_identity`](#create_identityn-int---matrix)


* [`SLE`](#sle)
  * [Methods](#sle-methods)
    * [`__init__`](#__init__self-args-listreal)
    * [`solve`](#solveself---vector)
    * [`x`](#xself-index-int---real)

---
---
## `Tuple`

__Implemented in v3.0.0 | Last change v3.0.0__

The Tuple class is the base class for the algebra submodule classes and the `avmath.analysis.Point` class.
It defines interaction methods inherited by the other classes.
The methods of `Tuple` simulate an immutable type.

### Attributes

Attribute | Usage | Implemented in version | Last change
--- | --- | --- | ---
`self._value` | Stores the values of the Tuple | v3.0.0 | v3.0.0

### Methods

#### `__init__(self, *args: REAL | list)`

__Implemented in v3.0.0 | Last change v3.0.0__

Initialises the `Tuple`.
Tuple can be initialised giving either numbers as parameters or a list.
```python
import avmath

# Initialisation via numbers
a = avmath.Tuple(1, 2, 4)

# Initialisation via iterable object
b_list = [4, 3, 4.9]
b = avmath.Tuple(b_list)
```

---
#### `__iter__(self)`

__Implemented in v3.0.0 | Last change v3.0.0__

Returns generator to convert `Tuple` to another iterable 
object.

---
#### `__getitem__(self, item)`

__Implemented in v3.0.0 | Last change v3.0.0__

Gives access to the items of a `Tuple`.

---
#### `__repr__(self) -> str` (Tuple)

__Implemented in v3.0.0 | Last change v3.0.0__

Returns string representation of the `Tuple`. String has the
form of built-in `tuple` representation.

---
#### `__eq__(self, other: 'Tuple') -> bool`

__Implemented in v3.0.0 | Last change v3.0.0__

Returns whether two `Tuple`s are equal.

---
#### `__len__(self) -> int` / `dim`

__Implemented in v3.0.0 | Last change v3.0.0__

Returns the length of the `Tuple`. Is equal to the dimension.

---
#### `__neg__(self)`

__Implemented in v3.0.0 | Last change v3.0.0__

Returns negative `Tuple`.

---
#### `__add__(self, other: 'Tuple') -> 'Tuple'`

__Implemented in v3.0.0 | Last change v3.0.0__

Adds two `Tuple`s.

---
#### `__sub__(self, other: 'Tuple') -> 'Tuple'`

__Implemented in v3.0.0 | Last change v3.0.0__

Subtracts two tuples.

---
#### `__mul__(self, other: REAL)` / `__rmul__`

__Implemented in v3.0.0 | Last change v3.0.0__

Returns scalar multiplied`Tuple`.

---
#### `__truediv__(self, other: REAL) -> 'Tuple`

__Implemented in v3.0.0 | Last change v3.0.0__

`Tuple` divided by a scalar. Returns `Tuple` with Fraction values.

---
#### `append(self, value: REAL)`

__Implemented in v3.0.0 | Last change v3.0.0__

Appends value to `Tuple`.

---
#### `no_fractions(self) -> 'Tuple'`

__Implemented in v3.0.0 | Last change v3.0.0__

Returns `Tuple` that does not contain `Fraction` members.

---
### Static Methods

#### `dim_check(*args) -> bool`

__Implemented in v3.0.0 | Last change v3.0.0__

Checks if arguments have the same amount of dimensions.

---
---

---
---
## `Vector`

__Implemented in v1.0.0 | Last change v3.0.0__

The Vector-class is an inherited class of `Tuple`.
The methods of `Vector` simulate an immutable type.
It also defines the following methods:

### Vector methods

#### `__init__(self, *args: REAL | 'Tuple', begin: Optional['Tuple'] = None, end: Optional['Tuple'] = None)`

__Implemented in v1.0.0 | Last Change in v3.0.0__

Initialisation of Vector object. Takes either number arguments, vectorizes
a `Tuple` or is initialised by giving a beginning and end as `Tuple`s.

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
#### `__abs__(self) -> float`

__Implemented in v1.0.0 | Last Change in v3.0.0__

Returns the absolute of the vector using pythagorean formula. Use 
````python
u = algebra.Vector(1, 2, 4)
print(abs(u))
````

---
#### `__add__(self, other: 'Vector') -> 'Vector'`

__Implemented in v1.0.0 | Last Change in v3.0.0__

Adds two vectors.

---
#### `__sub__(self, other: 'Vector') -> 'Vector'`

__Implemented in v1.0.0 | Last Change in v3.0.0__

Subtracts two vectors.

---
#### `__mul__(self, other: REAL | 'Vector') -> REAL | 'Vector'` / <br> `__rmul__`

__Implemented in v1.0.0 | Last Change in v3.0.0__

Either calculates scalar product of two vectors or
returns the scalar multiplication of a scalar and a vector.

---
#### `__truediv__(self, other: REAL)`

__Implemented in v3.0.0 | Last Change in v3.0.0__

Vector divided by a scalar. Returns vector with Fraction values.

---
#### `__pow__(self, power: int) -> REAL | 'Vector'`

__Implemented in v1.0.0 | Last Change in v3.0.0__

Returns `power` times scalar multiplied vector. `power`= 0 returns unit vector.

---
#### `cross(self, other: 'Vector') -> 'Vector'`

__Implemented in v3.0.0 | Last Change in v3.0.0__

Returns vector product of two three-dimensional vectors.

---
#### `unit(self) -> 'Vector'`

__Implemented in v3.0.0 | Last Change in v3.0.0__

Returns specific unit vector.

---
#### `leading_zeros(self) -> int`

__Implemented in v3.0.0 | Last Change in v3.0.0__

Returns the number of leading zeroes of a vector.

#### `no_fractions(self) -> 'Vector'`

__Implemented in v3.0.0 | Last Change in v3.0.0__

Returns a copied vector that does not contain `Fraction` members.

---
### Vector static methods

#### `spat(u: 'Vector', v: 'Vector', w: 'Vector') -> float`

__Implemented in v1.0.0 | Last Change in v3.0.0__

Returns the spat product of three vectors.

---
#### `angle(u: 'Vector', v: 'Vector') -> float`

__Implemented in v1.0.0 | Last Change in v3.0.0__

Calculates the angle (in radiant) between two vectors.

---
---
## `Structure`

The structure class provides features for calculation with many points.

### Structure attributes

Attribute | Usage | Implemented in version | Last Change
--- | --- | --- | ---
`self.points` | The edges of the structure | v2.0.0 | v2.0.0
`self.vectors` | The links of the points| v2.0.0 | v2.0.0

---

### Structure methods

#### `__init__(self, *args: 'Tuple')`

__Implemented in v1.0.0 | Last Change in v3.0.0__

Initialises the `Structure` with `Tuple`s.

---
#### `flat(self) -> bool`

__Implemented in v2.0.0 | Last Change in v3.0.0__


Returns `True` if there is a flat area in which all points
lie.

---
#### `circumference(self) -> float`

__Implemented in v1.0.0 | Last Change in v3.0.0__

Returns the circumference of the structure.

---
#### `area(self, opt: str = None)`

__Implemented in v1.0.0 | Last Change in v3.0.0__

Returns the area of the structure. `opt` can be `'flat'`,
in this case `GeometricalError` is thrown if the area is not flat.
Is not recommended because the algorithm is not very accurate.
With no option specified `GeometricalWarning` is caused if
the area is not flat.

---

### Structure static methods

#### `triangulate(p: 'Tuple', q: 'Tuple', r: 'Tuple') -> float`

__Implemented in v1.0.0 | Last Change in v3.0.0__

Calculates the area between three points. Used for `area`.

---
---

## `Matrix`

__Implemented in v1.0.0 | Last change v3.0.0__

The matrix class inherits from `Tuple` and also simulates
an immutable type. It defines following methods

### Matrix methods

#### `__init__(self, *args: List[REAL] | 'Vector')`

__Implemented in v1.0.0 | Last change v3.0.0__

Initialises the matrix. 
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
#### `__repr__(self) -> str`

__Implemented in v1.0.0 | Last change v3.0.0__

Returns string of matrix.

````python
A = algebra.Matrix([1, 2, 4],
                   [4, avmath.Fraction(2, 3), 2],
                   [5, 2, 9])
````
gives the output:

````
┌  1  2    4  ┐
|  4  2/3  2  |
└  5  2    9  ┘
````

---
#### `__round__(self, n: int = None) -> 'Matrix'`

__Implemented in v2.0.0 | Last change v3.0.0__

Returns matrix rounded to n digits.

---
#### `__neg__(self) -> 'Matrix'`

__Implemented in v1.0.0 | Last change v2.0.0__

Returns negative matrix.

---
#### `__add__(self, other: 'Matrix') -> 'Matrix'`

Adds two matrices.

---
#### `__sub__(self, other: 'Matrix') -> 'Matrix'`

__Implemented in v1.0.0 | Last change v2.0.0__

Subtracts two matrices.

---
#### `__mul__(self, other: REAL | 'Vector' | 'Matrix') -> Union['Matrix', 'Vector']` / <br> `__rmul__`

__Implemented in v1.0.0 | Last change v3.0.0__

Either multiplies two matrices, returns product of vector and matrix or returns the
scalar multiplication of a scalar and a matrix.

---
#### `__truediv__(self, other: REAL) -> 'Matrix'`

__Implemented in v3.0.0 | Last change v3.0.0__

Matrix divided by a scalar. Returns matrix with Fraction values.

---
#### `__pow__(self, power: int) -> 'Matrix'`

__Implemented in v1.0.0 | Last change v3.0.0__

Returns `power` times multiplied quadratic matrix.
`power`=0 returns identity. `power`=-1 returns
inverse matrix.

--- 
#### `size(self, option: str = None) -> list`

__Implemented in v2.0.0 | Last change v2.0.0__

Returns the size of a matrix in a list. Normally in order
(m, n) with m is number of rows and n is the number of
columns. If `opt="xy"` is specified, the order is reversed.

---
#### `dim(self) -> int`

__Implemented in v3.0.0 | Last change v3.0.0__

Returns the dimension of the matrix (=m * n).

---
#### `index(self, element: REAL) -> list`

__Implemented in v1.0.0 | Last change v1.0.0__

Returns position of element in a matrix.
If There are multiple, all get returned in a list.

---
#### `no_fractions(self) -> 'Matrix'`

__Implemented in v1.0.0 | Last change v3.0.0__

Returns a copied matrix that
does not contain `Fraction` members.

---
#### `column(self, column_index: int) -> 'Vector'`

__Implemented in v1.0.0 | Last change v3.0.0__

Returns the column vector of given index.

---
#### `row(self, row_index: int) -> 'Vector'`

__Implemented in v1.0.0 | Last change v3.0.0__

Returns the row vector of given index.

---
#### `append(self, row=None, column=None) -> 'Matrix'`

__Implemented in v1.0.0 | Last change v3.0.0__

Returns a matrix with appended iterable.

---
#### `remove(self, row_index: int = None, column_index: int = None) -> 'Matrix'`

__Implemented in v1.0.0 | Last change v3.0.0__

Returns matrix without row or column specified.

#### `transpose(self) -> 'Matrix'`

__Implemented in v1.0.0 | Last change v3.0.0__

Returns transposed matrix.

---
#### `det(self) -> REAL` / <br> `__abs__`

__Implemented in v2.0.0 | Last change v2.0.0__

Returns determinant of a matrix.

---
#### `cof(self) -> 'Matrix'`

__Implemented in v2.0.0 | Last change v2.0.0__

Returns cofactor matrix.

---
#### `adj(self) -> 'Matrix'`

__Implemented in v2.0.0 | Last change v2.0.0__

Returns adjunct of a matrix.

---
#### `inverse(self) -> 'Matrix'`

__Implemented in v2.0.0 | Last change v3.0.0__

Returns inverse matrix.

---
#### `ref(self) -> 'Matrix'`

__Implemented in v3.0.0 | Last change v3.0.0__

Returns a row echelon form of a matrix.

---
#### `rank(self) -> int`

__Implemented in v3.0.0 | Last change v3.0.0__

Returns rank of a matrix.

---
#### `rref(self) -> 'Matrix'`

__Implemented in v3.0.0 | Last change v3.0.0__

Returns a reduced row echelon form of a matrix.

---
### Matrix static methods

#### `create(m: int, n: int) -> 'Matrix'`

__Implemented in v1.0.0 | Last change v1.0.0__

Returns a matrix of size (m, n) with zeros only.

---
#### `create_identity(n: int) -> 'Matrix'`

__Implemented in v1.0.0 | Last change v1.0.0__

Returns an identity matrix with n rows.

---
#### `__leading_zero_sort(arg_list: list) -> 'list'`

__Implemented in v3.0.0 | Last change v3.0.0__

Sorts the given matrix value list so that elements are ordered
by the numbers of leading zeroes they have.

---
---

## `SLE`

__Implemented in v2.0.0 | Last change v3.0.0__

The **s**ystem of **l**inear **e**quations takes coefficients
and solves the system using inverse matrix. It inherits from `Matrix`.

### SLE methods

#### `__init__(self, *args: List[REAL])`

__Implemented in v2.0.0 | Last change v3.0.0__

Initialises SLE.

Type
````python
a = algebra.SLE([a_11, a_12, a_13, b_1],
                [a_21, a_22, a_23, b_2],
                [a_31, a_32, a_33, b_3])
````
for

| a_11 x_1 + a_12 x_2 + a_13 x_3 = b_1 | <br>
| a_21 x_1 + a_22 x_2 + a_23 x_3 = b_2 | <br>
| a_31 x_1 + a_32 x_2 + a_33 x_3 = b_3 | <br>

---
#### `solve(self) -> 'Vector'`

__Implemented in v2.0.0 | Last change v3.0.0__

Returns a vector with all unknown variables.

---
#### `x(self, index: int) -> REAL`

__Implemented in v2.0.0 | Last change v3.0.0__

Returns the unknown variable of given index.
