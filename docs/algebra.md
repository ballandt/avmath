# Avmath algebra documentation

The `avmath.algebra` submodule provides functionalities for
linear algebra. It can be imported in the following way:
````python
# pip install avmath
from avmath import algebra
````
---
## Contents

* [Tuple](#tuple)
  * [Attributes](#tuple-attributes)
  * [Methods](#tuple-methods)
  * [Static methods](#tuple-static-methods)


* [Vector](#vector)
  * [Methods](#vector-methods)
  * [Static methods](#vector-static-methods)


* [Structure](#structure)
  * [Attributes](#structure-attributes)
  * [Methods](#structure-methods)
  * [Static methods](#structure-static-methods)


* [Matrix](#matrix)
  * [Methods](#matrix-methods)
  * [Static methods](#matrix-static-methods)


* [`SLE`](#sle)
  * [Methods](#sle-methods)

---
---
# Tuple

__Implemented in v3.0.0 | Last change v3.0.0__

The Tuple class is the base class for the algebra submodule classes and the `avmath.analysis.Point` class.
It defines interaction methods inherited by the other classes.
The methods of `Tuple` simulate an immutable type.

## Tuple attributes

### Tuple._value

__Implemented in v3.0.0 | Last change v3.0.0__

Stores the items of the tuple in a list.

## Tuple methods

### Tuple.\_\_init__(*args)

__Implemented in v3.0.0 | Last change v3.0.0__

Initialises the Tuple.
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
### Tuple.\_\_iter__()

__Implemented in v3.0.0 | Last change v3.0.0__

Returns generator to convert Tuple to another iterable 
object.

---
### Tuple.\_\_getitem__(item)

__Implemented in v3.0.0 | Last change v3.0.0__

Gives access to the items of a Tuple.

---
#### Tuple.\_\_repr__()

__Implemented in v3.0.0 | Last change v3.0.0__

Returns string representation of the Tuple. String has the
form of built-in `tuple` representation.

---
### Tuple.\_\_eq__(other)

__Implemented in v3.0.0 | Last change v3.0.0__

Returns whether two Tuples are equal.

---
### Tuple.\_\_len__() / Tuple.dim()

__Implemented in v3.0.0 | Last change v3.0.0__

Returns the length of the Tuple. Is equal to the dimension.

---
### Tuple.\_\_neg__()

__Implemented in v3.0.0 | Last change v3.0.0__

Returns negative Tuple.

---
### Tuple.\_\_add__(other)

__Implemented in v3.0.0 | Last change v3.0.0__

Adds two Tuples.

---
### Tuple.\_\_sub__(other)

__Implemented in v3.0.0 | Last change v3.0.0__

Subtracts two tuples.

---
### Tuple\_\_mul__(other)

__Implemented in v3.0.0 | Last change v3.0.0__

Returns scalar multiplied Tuple.

---
### Tuple.\_\_truediv__(other)

__Implemented in v3.0.0 | Last change v3.0.0__

Tuple divided by a scalar. Returns Tuple with Fraction values.

---
### Tuple.append(value)

__Implemented in v3.0.0 | Last change v3.0.0__

Appends value to Tuple.

---
### Tuple.no_fractions()

__Implemented in v3.0.0 | Last change v3.0.0__

Returns Tuple that does not contain Fraction members.

---
### Tuple static methods

#### Tuple.dim_check(*args)

__Implemented in v3.0.0 | Last change v3.0.0__

Checks if arguments have the same amount of dimensions.

---
---
# Vector

__Implemented in v1.0.0 | Last change v3.0.0__

The Vector-class is an inherited class of `Tuple`.
The methods of `Vector` simulate an immutable type.
It also defines the following methods:

## Vector methods

### Vector.\_\_init__(*args \[, begin, end])

__Implemented in v1.0.0 | Last Change in v3.0.0__

Initialisation of Vector object. Takes either number arguments, vectorizes
a Tuple or is initialised by giving a beginning and end as Tuples.

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
### Vector.\_\_abs__()

__Implemented in v1.0.0 | Last Change in v3.0.0__

Returns the absolute of the vector using pythagorean formula. Use 
````python
u = algebra.Vector(1, 2, 4)
print(abs(u))
````

---
### Vector.\_\_add__(other)

__Implemented in v1.0.0 | Last Change in v3.0.0__

Adds two vectors.

---
### Vector.\_\_sub__(other)

__Implemented in v1.0.0 | Last Change in v3.0.0__

Subtracts two vectors.

---
### Vector.\_\_mul__(other) / Vector.\_\_rmul__(other)

__Implemented in v1.0.0 | Last Change in v3.0.0__

Either calculates scalar product of two vectors or
returns the scalar multiplication of a scalar and a vector.

---
### Vector.\_\_truediv__(other)

__Implemented in v3.0.0 | Last Change in v3.0.0__

Vector divided by a scalar. Returns vector with Fraction values.

---
### Vector.\_\_pow__(power)

__Implemented in v1.0.0 | Last Change in v3.0.0__

Returns `power` times scalar multiplied vector. `power`= 0 returns unit vector.

---
### Vector.cross(other)

__Implemented in v3.0.0 | Last Change in v3.0.0__

Returns vector product of two three-dimensional vectors.

---
### Vector.unit()

__Implemented in v3.0.0 | Last Change in v3.0.0__

Returns specific unit vector.

---
#### Vector.leading_zeros()

__Implemented in v3.0.0 | Last Change in v3.0.0__

Returns the number of leading zeroes of a vector.

---
### Vector.no_fractions()

__Implemented in v3.0.0 | Last Change in v3.0.0__

Returns a copied vector that does not contain `Fraction` members.

---
## Vector static methods

### Vector.spat(u, v, w)

__Implemented in v1.0.0 | Last Change in v3.0.0__

Returns the spat product of three vectors.

---
### Vector.angle(u, v)

__Implemented in v1.0.0 | Last Change in v3.0.0__

Calculates the angle (in radiant) between two vectors.

---
---
# Structure

The structure class provides features for calculation with many points.

## Structure attributes

| Attribute      | Usage                      | Implemented in version | Last Change |
|----------------|----------------------------|------------------------|-------------|
| `self.points`  | The edges of the structure | v2.0.0                 | v2.0.0      |
| `self.vectors` | The links of the points    | v2.0.0                 | v2.0.0      |

---

## Structure methods

### Structure.\_\_init__(*args)

__Implemented in v1.0.0 | Last Change in v3.0.0__

Initialises the Structure with Tuples.

---
### Structure.flat()

__Implemented in v2.0.0 | Last Change in v3.0.0__


Returns `True` if there is a flat area in which all points
lie.

---
### Structure.circumference()

__Implemented in v1.0.0 | Last Change in v3.0.0__

Returns the circumference of the structure.

---
### Structure.area(\[opt])

__Implemented in v1.0.0 | Last Change in v3.1.0__

Returns the area of the structure. `opt` can be `'flat'`,
in this case `GeometricalError` is thrown if the area is not flat.
Is not recommended because the algorithm is not very accurate.
With no option specified `GeometricalWarning` is caused if
the area is not flat.

---

## Structure static methods

### Structure.triangulate(p, q, r)

__Implemented in v1.0.0 | Last Change in v3.0.0__

Calculates the area between three points.

---
---

# Matrix

__Implemented in v1.0.0 | Last change v3.0.0__

The matrix class inherits from Tuple and also simulates
an immutable type. It defines following methods

## Matrix methods

### Matrix.\_\_init__(*args)

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
### Matrix.\_\_repr__()

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
### Matrix.\_\_round__(\[n])

__Implemented in v2.0.0 | Last change v3.0.0__

Returns matrix rounded to n digits. If no n is specified rounds with no post comma digits.

---
### Matrix.\_\_neg__()

__Implemented in v1.0.0 | Last change v2.0.0__

Returns negative matrix.

---
### Matrix.\_\_add__(other)

Adds two matrices.

---
### Matrix.\_\_sub__(other)

__Implemented in v1.0.0 | Last change v2.0.0__

Subtracts two matrices.

---
### Matrix.\_\_mul__(other) / Matrix.\_\_rmul__(other)

__Implemented in v1.0.0 | Last change v3.0.0__

Either multiplies two matrices, returns product of vector and matrix or returns the
scalar multiplication of a scalar and a matrix.

---
### Matrix.\_\_truediv__(other)

__Implemented in v3.0.0 | Last change v3.0.0__

Matrix divided by a scalar. Returns matrix with Fraction values.

---
### Matrix.\_\_pow__(power)

__Implemented in v1.0.0 | Last change v3.0.0__

Returns `power` times multiplied quadratic matrix.
`power`=0 returns identity. `power`=-1 returns
inverse matrix.

--- 
#### Matrix.size(\[option])

__Implemented in v2.0.0 | Last change v2.0.0__

Returns the size of a matrix in a list. Normally in order
(m, n) with m is number of rows and n is the number of
columns. If `opt="xy"` is specified, the order is reversed.

---
### Matrix.dim()

__Implemented in v3.0.0 | Last change v3.0.0__

Returns the dimension of the matrix (=m * n).

---
#### Matrix.index(element)

__Implemented in v1.0.0 | Last change v1.0.0__

Returns position of element in a matrix.
If There are multiple, all get returned in a list.

---
### Matrix.no_fractions()

__Implemented in v1.0.0 | Last change v3.0.0__

Returns a copied matrix that
does not contain `Fraction` members.

---
### Matrix.column(column_index)

__Implemented in v1.0.0 | Last change v3.0.0__

Returns the column vector of given index.

---
### Matrix.row(row_index)

__Implemented in v1.0.0 | Last change v3.0.0__

Returns the row vector of given index.

---
### Matrix.append(\[\[row], \[column]])

__Implemented in v1.0.0 | Last change v3.0.0__

Returns a matrix with appended iterable. Can be row or column or both.

---
### Matrix.remove(\[\[row_index], \[column_index]])

__Implemented in v1.0.0 | Last change v3.0.0__

Returns matrix without row or column specified. Can contain both row and column deletion.

---
### Matrix.transpose()

__Implemented in v1.0.0 | Last change v3.0.0__

Returns transposed matrix.

---
### Matrix.det() / Matrix.\_\_abs__()

__Implemented in v2.0.0 | Last change v2.0.0__

Returns determinant of a matrix.

---
### Matrix.cof()

__Implemented in v2.0.0 | Last change v2.0.0__

Returns cofactor matrix.

---
### Matrix.adj()

__Implemented in v2.0.0 | Last change v2.0.0__

Returns adjunct of a matrix.

---
### Matrix.inverse()

__Implemented in v2.0.0 | Last change v3.0.0__

Returns inverse matrix.

---
### Matrix.ref()

__Implemented in v3.0.0 | Last change v3.0.0__

Returns a row echelon form of a matrix.

---
### Matrix.rank()

__Implemented in v3.0.0 | Last change v3.0.0__

Returns rank of a matrix.

---
### Matrix.rref()

__Implemented in v3.0.0 | Last change v3.0.0__

Returns a reduced row echelon form of a matrix.

---
### Matrix static methods

### Matrix.create(m, n)

__Implemented in v1.0.0 | Last change v1.0.0__

Returns a matrix of size (m, n) with zeros only.

---
### Matrix.create_identity(n)

__Implemented in v1.0.0 | Last change v1.0.0__

Returns an identity matrix with n rows.

---
### Matrix.__leading_zero_sort(arg_list)

__Implemented in v3.0.0 | Last change v3.0.0__

Sorts the given matrix value list so that elements are ordered
by the numbers of leading zeroes they have.

---
---

# SLE

__Implemented in v2.0.0 | Last change v3.0.0__

The **s**ystem of **l**inear **e**quations takes coefficients
and solves the system using inverse matrix. It inherits from `Matrix`.

## SLE methods

### SLE.\_\_init__(*args)

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
### SLE.solve()

__Implemented in v2.0.0 | Last change v3.0.0__

Returns a vector with all unknown variables.

---
### SLE.x(index)

__Implemented in v2.0.0 | Last change v3.0.0__

Returns the unknown variable of given index.
