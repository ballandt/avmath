"""AVMATH ALGEBRA
AdVanced math algebra submodule containing linear algebra
features tuples, vectors, matrices and systems of linear
equations.
"""

import copy
import logging
from typing import Union, Optional, List

from . import ArgumentError, DimensionError, REAL, Fraction, sin, arccos,\
    _check_types
from .analysis import Function, Polynomial

__all__ = ["Tuple", "Structure", "Matrix", "Vector", "SLE"]


class GeometricalError(Exception):
    """Raised geometrical order cannot be executed."""

    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return self.arg


class MatrixError(Exception):
    """Raised if matrix operations fail due to inappropriate matrices."""

    def __init__(self, issue):
        self.arg = issue

    def __str__(self):
        return self.arg


class GeometricalWarning:
    """Raised if shape without opt="flat" is called, but flat returns 'False'.
    Program does not get interrupted.
    Use 'GeometricalWarning.disable_warning()' to ignore warning.
    """
    __warning = True

    def __init__(self, arg):
        if GeometricalWarning.__warning:
            logging.warning(arg)
        else:
            pass

    @classmethod
    def disable(cls):
        """Function to allow to permanently disable GeometricalWarning
        in case the calculation are too inexact."""
        GeometricalWarning.__warning = False


class Tuple:
    """Algebraic tuple. Can also be interpreted as
    point in the coordinate system.
    """

    def __init__(self, *args: REAL | list | tuple | 'Vector'):
        _check_types(args, int, float, list, tuple, Fraction, Vector)
        if type(args[0]) in (list, tuple) and len(args) == 1:
            self._value = list(args[0])
        else:
            self._value = list(args)

    def __iter__(self):
        """Returns iterator to convert tuple to iterable object."""
        for ele in self._value:
            yield ele

    def __getitem__(self, item):
        """Returns value of 'item's dimension."""
        return self._value[item]

    def __repr__(self) -> str:
        """Returns string representation."""
        return str(tuple(self._value))

    def __eq__(self, other: 'Tuple') -> bool:
        """Checks if elements are equal."""
        return self._value == other._value

    def __len__(self) -> int:
        """Returns the length or dimension of a tuple"""
        return len(self._value)

    dim = __len__

    def __neg__(self):
        """Returns negative tuple."""
        return self * -1

    def __add__(self, other: 'Tuple') -> 'Tuple':
        """Adds two tuples:
        a + b = (a_1 + b_1, a_2 + b_2, ... , a_n + b_n)
        """
        if not Tuple.dim_check(self, other):
            raise DimensionError(other.dim(), self.dim())
        result = []
        for i in range(self.dim()):
            result.append(self[i] + other[i])
        return Tuple(*tuple(result))

    def __sub__(self, other: 'Tuple') -> 'Tuple':
        """Reversed addition:
        a - b = a + (-b)
        """
        return self + -other

    def __mul__(self, other: REAL):
        """Scalar multiplication:
        r * a = (r*a_1, r*a_2, ... , r*a_n)    (a e R^n, r e R)
        """
        result = []
        for ele in self._value:
            result.append(ele * other)
        return Tuple(*tuple(result))

    __rmul__ = __mul__

    def __truediv__(self, other: REAL) -> 'Tuple':
        """Division. Tuple by number only.Though mathematically
        incorrect gives the possibility to return fractions for
        correct division.
        """
        ret_list = []
        for ele in self:
            if type(ele) == Fraction:
                ret_list.append(ele / other)
            else:
                ret_list.append(Fraction(ele, other))
        return Tuple(ret_list)

    def append(self, value: REAL):
        """Adds value to Tuple."""
        ret_value = copy.deepcopy(self._value)
        ret_value.append(value)
        return Tuple(ret_value)

    def no_fractions(self) -> 'Tuple':
        """Returns Tuple that does not contain Fractions.
        Converts Fractions to float.
        """
        return Tuple([float(ele) for ele in self])

    @staticmethod
    def dim_check(*args) -> bool:
        """Checks if arguments have the same amount of dimensions."""
        dimension = args[0].dim()
        for ele in args:
            if not ele.dim() == dimension:
                return False
        return True


class Vector(Tuple):
    """Vector."""

    def __init__(self, *args: REAL | 'Tuple',
                 begin: Optional['Tuple'] = None,
                 end: Optional['Tuple'] = None):
        """Takes whether number arguments, vectorizes Tuple or
        creates vector between two Tuples.

        For number insert:
        Vector(a_1, a_2, a_3)
        for
        ┌ a_1 ┐
        | a_2 |  or (a_1, a_2, a_3)
        └ a_3 ┘

        For vectorization:
        Vector(Tuple(a_1, a_2, a_3))
        for
        ┌ a_1 ┐
        | a_2 |  or (a_1, a_2, a_3)
        └ a_3 ┘

        For linking of points:
        Vector(begin=Tuple(a_1, a_2, a_3), end=Tuple(b_1, b_2, b_3))
        for
        ┌ b_1 - a_1 ┐
        | b_2 - a_2 |  or (b_1 - a_1, b_2 - a_2, b_3 - a_3)
        └ b_3 - a_3 ┘
        """

        if not begin and type(args[0]) != Tuple:
            super().__init__(*args)

        elif not begin and type(args[0]) == Tuple:
            super().__init__(*tuple(args[0]))

        elif begin and end:
            _check_types((begin, end), Tuple)
            if begin.dim() != end.dim():
                raise DimensionError(end.dim(), begin.dim())
            super().__init__(
                *tuple([end[i] - begin[i] for i in range(begin.dim())])
            )

    def __abs__(self) -> float:
        """Returns absolute of a vector.
            Insert
            abs(Vector(a_1, a_2, [...], a_n))
            For
               ________________________________
            \\/ (a_1)^2 + (a_2)^2 + ... + (a_n)^2
            """
        res = 0
        for i in range(self.dim()):
            res += self[i] ** 2
        self.abs = res ** 0.5
        return self.abs

    def __add__(self, other: 'Vector') -> 'Vector':
        """Adds two tuples:
        a + b = (a_1 + b_1, a_2 + b_2, ... , a_n + b_n)
        """
        if not Vector.dim_check(self, other):
            raise DimensionError(other.dim(), self.dim())
        result = []
        for i in range(self.dim()):
            result.append(self[i] + other[i])
        return Vector(*tuple(result))

    def __sub__(self, other: 'Vector') -> 'Vector':
        """Reversed addition:
        a - b = a + (-b)
        """
        return self + -other

    def __mul__(self, other: REAL | 'Vector') -> REAL | 'Vector':
        """Either scalar product of two vectors or
        scalar multiplication of scalar and vector.
        Insert
        Vector(a_1, a_2, [...], a_n) * Vector(b_1, b_2, [...], b_n)
        For
        (a_1, a_2, ..., a_n) * (b_1, b_2, ..., b_n)
        = a_1 b_1 + a_2 b_2 + ... + a_n b_n
        """
        if type(other) != Vector:
            return Vector(Tuple(*tuple(self)) * other)
        if not Vector.dim_check(self, other):
            raise DimensionError(self.dim(), other.dim())
        res = 0
        for i in range(self.dim()):
            res += self[i] * other[i]
        return res

    __rmul__ = __mul__

    def __truediv__(self, other: REAL) -> 'Vector':
        """Division. Vector by number only.Though mathematically
        incorrect gives the possibility to return fractions for
        correct division.
        """
        ret_list = []
        for e in self:
            if type(e) == Fraction:
                ret_list.append(e / other)
            else:
                ret_list.append(Fraction(e, other))
        return Vector(Tuple(ret_list))

    def __pow__(self, power: int) -> REAL | 'Vector':
        """Returns result of power times scalar multiplied vector.
        Power 0 returns unit-vector.
        Insert
        a = Vector(a_1, a_2, [...], a_n)
        a**p
        for
        a * a * ... * a
            p times
        """
        _check_types((power,), int)
        if power == 0:
            return self.unit()
        res = 1
        for i in range(power):
            res *= self
        return res

    def cross(self, other: 'Vector') -> 'Vector':
        """Vector multiplication.
            Only 3 dimensions supported.
            Insert
            Vector(a_1, a_2, a_3).cross(Vector(b_1, b_2, b_3))
            For
            (a_1, a_2, a_3) x (b_1, b_2, b_3)
            = (a_2 b_3 - a_3 b_2, a_1 b_1 - a_1 b_3, a_1 b_2 - a_2 b_1)
            """
        if self.dim() != 3:
            raise DimensionError(self.dim(), 3)
        elif other.dim() != 3:
            raise DimensionError(other.dim(), 3)
        res = [0, 0, 0]
        res[0] = (self[1] * other[2]) - (self[2] * other[1])
        res[1] = (self[2] * other[0]) - (self[0] * other[2])
        res[2] = (self[0] * other[1]) - (self[1] * other[0])
        return Vector(*tuple(res))

    def unit(self) -> 'Vector':
        """Returns vector with absolute 1 and same direction as self.
        Insert
        Vector(a_1, a_2, [...], a_n).unit()
        For
        a / |a|"""
        if abs(self) == 0:
            raise GeometricalError("Vector with absolute 0 has no unit vector")
        else:
            res = self * (1 / abs(self))
            return res

    def orthogonal(self, *args: 'Vector') -> list:
        q = [self]
        for i, e in enumerate(args):
            q.append(e)
            for e2 in q[:-1]:
                q[i+1] -= Fraction(q[i+1]*e2, e2**2) * e2
        return q

    def leading_zeros(self) -> int:
        """Returns number of leading zeros of a vector. Especially used for
        matrix ref.
        """
        leading_0 = 0
        for ele in self._value:
            if ele == 0:
                leading_0 += 1
            else:
                break
        return leading_0

    def no_fractions(self) -> 'Vector':
        """Returns Vector that does not contain Fractions.
        Converts Fractions to float.
        """
        return Vector(*tuple([float(e) for e in self]))

    @staticmethod
    def spat(u: 'Vector', v: 'Vector', w: 'Vector') -> float:
        """Returns spat volume.
        Insert
        Vector.spat(Vector(a_1, a_2, a_3),
                    Vector(b_1, b_2, b_3),
                    Vector(c_1, c_2, c_3))
        For
        (a x b) * c"""
        return (u.cross(v)) * w

    @staticmethod
    def angle(u: 'Vector', v: 'Vector') -> float:
        """Returns angle between two vectors.
        Insert
        Vector.angle(Vector(a_1, [...], a_n), Vector(b_1, [...], b_n))
        For
               (a_1, ..., a_n) (b_1, ..., b_n)
        arccos(-------------------------------) = phi    (1 < n < 4)
                          |a| * |b|
        """
        if not Vector.dim_check(u, v):
            raise DimensionError(v.dim(), u.dim())
        if u.dim() not in (2, 3):
            raise DimensionError(u.dim(), "2 or 3")
        angle = arccos(u * v / (abs(u) * abs(v)))
        return angle


class Structure:
    """Point structure"""

    def __init__(self, *args: 'Tuple'):
        """Insert the edges of the structure."""
        _check_types(args, Tuple)
        if not Tuple.dim_check(*args):
            raise DimensionError(
                other="Tuples have different amount of dimensions."
            )
        if args[0].dim() > 3:
            raise DimensionError(other="Tuples must have 2 or 3 dimensions.")
        self.points = args
        if self.points[0].dim() == 2:
            self.points = [e.append(0) for e in self.points]
        self.vectors = [Vector(begin=self.points[-1], end=self.points[0])]
        for i in range(1, len(self.points)):
            self.vectors.append(
                Vector(begin=self.points[i - 1], end=self.points[i])
            )

    def flat(self) -> bool:
        """Returns 'True' if the points are in a three-dimensional area."""
        if Tuple.dim_check(*self.points) and self.points[1].dim() == 2:
            return True
        unitvector = (self.vectors[0].cross(self.vectors[-1])).unit()
        for i in range(len(self.vectors) - 1):
            if (self.vectors[i].cross(self.vectors[i+1])).unit() != unitvector:
                return False
        return True

    def circumference(self) -> float:
        """Returns the circumference of the area
        opened by any amount of points.
        """
        u = 0
        for e in self.vectors:
            u += abs(e)
        return u

    def area(self, opt: str = None):
        """Returns area opened by any amount of vectors."""
        area = Vector(0, 0, 0)
        if opt == "flat":
            if not self.flat():
                raise GeometricalError("No flat area found.")
        if not self.flat():
            GeometricalWarning("Area does not seem to be flat.")
        for i in range(len(self.points) - 1):
            abv = Vector(self.points[i] - self.points[0])
            acv = Vector(self.points[i+1] - self.points[0])
            area += abv.cross(acv) * 0.5
        return abs(area)

    @staticmethod
    def triangulate(p: 'Tuple', q: 'Tuple', r: 'Tuple') -> float:
        """Returns area between three points."""
        abv = Vector(begin=p, end=q)
        acv = Vector(begin=p, end=r)
        c = abs(abv)
        b = abs(acv)
        phi = Vector.angle(abv, acv)
        area = 0.5 * b * c * (sin(phi))
        return area


class Matrix(Tuple):
    """Mathematical matrix"""

    def __init__(self, *args: tuple | list | Vector):
        """Initializes the matrix. Enter a list for each row.

        insert
        Matrix([a_11, a_12, a_13],
               [a_21, a_22, a_23],
               [a_31, a_32, a_33])
        for
        ┌ a_11  a_12  a_13 ┐
        | a_21  a_22  a_23 |
        └ a_31  a_32  a_33 ┘
        """
        if type(args[0]) == Vector and len(args) == 1:
            value = []
            for e in args[0]._value:
                value.append([e])
            super().__init__(*value)
        else:
            value = list(args)
            for e in value:
                if not len(value[0]) == len(e):
                    raise ArgumentError(e, f"row with {len(args[0])} members")
                _check_types(e, int, float, Fraction, Polynomial, Function)
            super().__init__(*tuple(args))

    def __repr__(self) -> str:
        """Prints matrix in an understandable view."""
        ret_str = "\n"
        if self.size()[0] == 1:
            ret_str += "["
            for e in self[0]:
                ret_str += 2 * " " + str(e)
            ret_str += 2 * " " + "]"
            return ret_str
        longest_element_list = list(map(str, self[0]))
        for i in range(1, self.size()[0]):
            for j in range(self.size()[1]):
                if len(str(self[i][j])) > len(longest_element_list[j]):
                    longest_element_list[j] = str(self[i][j])
        digits_list = list(map(len, longest_element_list))
        b_element = sorted(digits_list)[-1]
        if b_element < 3:
            distance = 1
        elif b_element < 8:
            distance = 2
        else:
            distance = 3
        for i in range(self.size()[0]):
            if i == 0:
                ret_str += "┌" + distance * " "
            elif i == self.size()[0] - 1:
                ret_str += "└" + distance * " "
            else:
                ret_str += "|" + distance * " "
            for j in range(self.size()[1]):
                ret_str += str(self[i][j])
                ret_str += ((digits_list[j]-len(str(self[i][j]))+distance)*" ")
            if i == 0:
                ret_str += "┐"
            elif i == self.size()[0] - 1:
                ret_str += "┘"
            else:
                ret_str += "|"
            ret_str += "\n"
        return ret_str

    def __round__(self, n: int = None) -> 'Matrix':
        """Returns matrix with rounded values."""
        ret_mat = copy.deepcopy(self)
        for i in range(self.size()[0]):
            for j in range(self.size()[1]):
                ret_mat._value[i][j] = round(ret_mat._value[i][j], n)
        return ret_mat

    def __neg__(self) -> 'Matrix':
        """Returns negative matrix."""
        args = []
        for i in range(self.size()[0]):
            args.append([])
            for j in range(self.size()[1]):
                args[i].append(self[i][j] * -1)
        return Matrix(*tuple(args))

    def __add__(self, other: 'Matrix') -> 'Matrix':
        """Adds two matrices."""
        if type(other) != Matrix:
            raise ArgumentError(type(other), Matrix)
        elif self.size() != other.size():
            raise ArgumentError("matrix with size " + str(other.size()),
                                "matrix with size" + str(self.size()))
        args = []
        for i in range(self.size()[0]):
            args.append([])
            for j in range(self.size()[1]):
                args[i].append(self[i][j] + other[i][j])
        return Matrix(*tuple(args))

    def __sub__(self, other: 'Matrix') -> 'Matrix':
        """Subtracts a matrix from another."""
        return self + -other

    def __mul__(self,
                other: REAL | 'Vector' | 'Matrix')\
            -> Union['Matrix', 'Vector']:
        """Multiplies two matrices."""
        if type(other) in (int, float):
            args = []
            for i in range(self.size()[0]):
                args.append([])
                for e in self[i]:
                    args[i].append(e * other)
            return Matrix(*tuple(args))

        elif type(other) == Vector:
            if self.size()[1] != other.dim():
                raise MatrixError(f"Vector with size {other.dim()} cannot "
                                  f"be multiplied by matrix with "
                                  f"size {self.size()}")
            v_matrix = Matrix(other)
            ret_mat = self * v_matrix
            args = ()
            for e in ret_mat._value:
                args += (e[0],)
            return Vector(*args)

        elif type(other) == Matrix:
            if self.size()[1] != other.size()[0]:
                raise MatrixError(f"Matrix with {other.size()[0]} "
                                  f"rows cannot be multiplied"
                                  f" by {self.size()[1]} column matrix.")
            ret_mat = Matrix.create(self.size()[0], other.size()[1])
            for i in range(self.size()[0]):
                for j in range(other.size()[1]):
                    ret_mat[i][j] = self.row(i) * other.column(j)
            return ret_mat

    __rmul__ = __mul__

    def __truediv__(self, other: REAL) -> 'Matrix':
        """Division. Matrix by number only.Though mathematically
        incorrect gives the possibility to return fractions for
        correct division.
        """
        ret_mat = Matrix.create(*tuple(self.size()))
        for index, ele in enumerate(self):
            for j_index, j_ele in enumerate(ele):
                ret_mat[index][j_index] = Fraction(j_ele, other)
        return ret_mat

    def __pow__(self, power: int) -> 'Matrix':
        """Power operation for matrix^scalar."""
        if self.size()[0] == self.size()[1]:
            raise MatrixError("Matrix must be quadratic.")
        if type(power) is not int:
            raise ArgumentError("Power od type"+str(type(power)), int)
        ret_mat = self
        if power == -1:
            return self.inverse()
        elif power == 0:
            return Matrix.create_identity(self.size()[0])
        else:
            for i in range(1, power):
                ret_mat *= self
            return ret_mat

    def size(self, option: str = None) -> list:
        """Returns list of matrix size. [m, n]"""
        if not option:
            return [len(self._value), len(self._value[0])]
        elif option == "xy":
            return [len(self._value[0]), len(self._value)]

    def dim(self) -> int:
        """Returns the dimension of a matrix."""
        return self.size()[0] * self.size()[1]

    def index(self, element: REAL) -> list:
        """Returns position of given element in a list. Can contain
        multiple return arguments. If ele is not in matrix an
        empty list is returned.
        """
        position = []
        for i in range(self.size()[0]):
            for e in self[i]:
                if element == e:
                    position.append([self[i].index(e), i])
        return position

    def no_fractions(self) -> 'Matrix':
        """Returns a matrix with no Fraction members. Fractions are
        converted to floats."""
        ret_mat = Matrix.create(*tuple(self.size()))
        for index, ele1 in enumerate(self):
            for jindex, ele2 in enumerate(ele1):
                ret_mat[index][jindex] = float(ele2)
        return ret_mat

    def column(self, column_index: int) -> 'Vector':
        """Returns column with specific index."""
        ret_list = []
        for e in self._value:
            ret_list.append(e[column_index])
        return Vector(*tuple(ret_list))

    def row(self, row_index: int) -> 'Vector':
        """Returns row with specific index."""
        return Vector(*tuple(self[row_index]))

    def append(self, row=None, column=None) -> 'Matrix':
        """Method to append rows or columns to matrix."""
        ret_mat = self
        if row:
            if len(row) != self.size()[1]:
                raise MatrixError(f"Cannot append {len(row)} element row "
                                  f"to matrix with size {self.size()}.")
            ret_mat._value.append(list(row))
        elif column:
            if len(column) != self.size()[0]:
                raise MatrixError(f"Cannot append {len(column)} element "
                                  f"row to matrix with size{self.size()}")
            for i in range(ret_mat.size()[0]):
                ret_mat._value[i].append(column[i])
        return ret_mat

    def remove(self,
               row_index: int = None,
               column_index: int = None) -> 'Matrix':
        """Returns a matrix with given row or column removed."""
        ret_mat = copy.deepcopy(self)
        if row_index is not None:
            del ret_mat._value[row_index]
        if column_index is not None:
            for i in range(len(ret_mat._value)):
                del ret_mat._value[i][column_index]
        return ret_mat

    def transpose(self) -> 'Matrix':
        """Returns transposed matrix."""
        args = []
        for i in range(self.size()[1]):
            args.append(list(self.column(i)))
        return Matrix(*tuple(args))

    def det(self, mode: str = "gauss") -> Union[REAL, 'Polynomial']:
        """Returns determinant of a matrix."""
        if self.size()[0] != self.size()[1]:
            raise MatrixError("Matrix must be quadratic.")
        if self.size() == [1, 1]:
            return self[0][0]
        elif self.size() == [3, 3]:
            det = self[0][0] * self[1][1] * self[2][2] \
                  + self[0][1] * self[1][2] * self[2][0] \
                  + self[0][2] * self[1][0] * self[2][1] \
                  - self[0][0] * self[1][2] * self[2][1] \
                  - self[0][1] * self[1][0] * self[2][2] \
                  - self[0][2] * self[1][1] * self[2][0]
            return det
        elif (3 < self.size()[0] < 6) or mode == "laplace":
            answer = 0
            for i in range(self.size()[1]):
                smaller_matrix = self.remove(0, i)
                k = (-1) ** i * self[0][i] * smaller_matrix.det()
                answer += k
        else:
            det = 1
            mat_list = [self.row(i) for i in range(self.size()[0])]
            for i in range(len(mat_list)):
                if mat_list[i].leading_zeros() > i:
                    for j in range(i + 1, len(mat_list)):
                        if mat_list[j].leading_zeros() == i:
                            mat_list[i], mat_list[j] = mat_list[j], mat_list[i]
                            det *= -1
                element = mat_list[i]
                if element.leading_zeros() == len(element):
                    continue
                if i == len(mat_list):
                    break
                for j in range(i + 1, len(mat_list)):
                    j_element = mat_list[j]
                    if j_element.leading_zeros() == element.leading_zeros():
                        op_vector = Fraction(
                            j_element[j_element.leading_zeros()],
                            mat_list[i][i]) * mat_list[i]
                        mat_list[j] = j_element - op_vector
            for i in range(len(mat_list)):
                det *= mat_list[i][i]
            return det
        return answer

    __abs__ = det

    def cof(self) -> 'Matrix':
        """Returns cofactor matrix."""
        ret_mat = Matrix.create(self.size()[0], self.size()[1])
        for i in range(self.size()[1]):
            for j in range(self.size()[0]):
                smaller_matrix = self.remove(i, j)
                if smaller_matrix.size() == [1, 1]:
                    ret_mat[i][j] = (-1) ** (i + j) * smaller_matrix[0][0]
                else:
                    ret_mat[i][j] = (-1) ** (i + j) * self.remove(i, j).det()
        return ret_mat

    def adj(self) -> 'Matrix':
        """Returns adjunct of a matrix."""
        return self.cof().transpose()

    def inverse(self) -> 'Matrix':
        """Returns inverse matrix."""
        if self.size()[0] != self.size()[1]:
            raise MatrixError("Matrix must be quadratic.")
        if self.det() == 0:
            raise ZeroDivisionError("Determinant must not be 0.")
        ret_mat = self.adj() / self.det()
        return ret_mat

    def ref(self) -> 'Matrix':
        """Row echelon form of a matrix."""
        sorted_arg_list = Matrix.__leading_zero_sort(list(self))
        for i in range(len(sorted_arg_list)):
            sorted_arg_list = Matrix.__leading_zero_sort(sorted_arg_list)
            element = sorted_arg_list[i]
            if element.leading_zeros() == len(element):
                continue
            sorted_arg_list[i] = element / element[element.leading_zeros()]
            if i == len(sorted_arg_list):
                break
            for j in range(i+1, len(sorted_arg_list)):
                jelement = sorted_arg_list[j]
                if jelement.leading_zeros() == element.leading_zeros():
                    op_vector = sorted_arg_list[i]\
                                * jelement[jelement.leading_zeros()]
                    sorted_arg_list[j] = jelement - op_vector
        sorted_arg_list = tuple(map(list, sorted_arg_list))
        return Matrix(*sorted_arg_list)

    def rank(self) -> int:
        """Rank of the matrix."""
        ret_val = 0
        ref_mat = self.ref()
        for ele in ref_mat._value:
            for sub_ele in ele:
                if abs(sub_ele) > 1e-14:
                    ret_val += 1
                    break
        return ret_val

    def rref(self) -> 'Matrix':
        """Reduced row echelon form."""
        ret_list = [Vector(Tuple(e)) for e in self.ref()]
        for i in range(self.rank()-1, 0, -1):
            for j in range(i):
                ret_list[j] -= ret_list[i]\
                               * ret_list[j][ret_list[i].leading_zeros()]
        return Matrix(*tuple([list(e) for e in ret_list]))

    def qr(self):
        no_fractions = self.no_fractions()
        q1 = no_fractions.column(0)
        qi = []
        for i in range(1, no_fractions.size()[1]):
            qi.append(no_fractions.column(i))
        orthogonal_vectors =\
            [e.no_fractions() for e in q1.orthogonal(*tuple(qi))]
        Q = Matrix(orthogonal_vectors[0].unit())
        for ele in orthogonal_vectors[1:]:
            Q.append(column=ele.unit())
        R = Matrix.create(Q.size()[1], Q.size()[0])
        for i in range(R.size()[0]):
            for j in range(R.size()[1]):
                if i == j:
                    R[i][j] = abs(orthogonal_vectors[i])
                elif i > j:
                    R[i][j] = 0
                else:
                    R[i][j] = no_fractions.column(j) * orthogonal_vectors[i] \
                              / abs(orthogonal_vectors[i])
        return Q.no_fractions(), R.no_fractions()

    def eigenvalues(self, mode=complex):
        """Calculates the real eigenvalues of a matrix.
        `mode=float` or `mode="real"` returns real eigenvalues
        only.
        """
        values = copy.deepcopy(list(self))
        for i in range(self.size()[0]):
            function = Polynomial(-1, values[i][i])
            values[i][i] = function
        return Matrix(*tuple(values)).det(mode="laplace").roots(mode=mode)

    def eigenvector(self, eigenvalue):
        """Calculates the eigenvector to a given eigenvalue."""
        A = list(copy.deepcopy(self))
        for i in range(len(A)):
            A[i][i] = A[i][i] - eigenvalue
        A = Matrix(*tuple(A))
        A.append(column=[0 for _ in range(A.size()[0])])
        S = SLE(*tuple(A))
        return S.solve()

    @staticmethod
    def create(m: int, n: int) -> 'Matrix':
        """Staticmethod to create an m X n matrix that contains
        only zeros.
        """
        args = []
        for i in range(m):
            args.append([])
            for j in range(n):
                args[i].append(0)
        return Matrix(*tuple(args))

    @staticmethod
    def create_identity(n: int) -> 'Matrix':
        """Staticmethod to create an identity matrix with any
        amount of rows.
        """
        ret_mat = Matrix.create(n, n)
        for i in range(n):
            for j in range(n):
                ret_mat[i][j] = 1 if i == j else 0
        return ret_mat

    @staticmethod
    def __leading_zero_sort(arg_list: list) -> 'list':
        """Sorts value list of matrix for ref."""
        longest_row = []
        for index, element in enumerate(arg_list):
            longest_row.append(
                [Vector(Tuple(list(element))).leading_zeros(), index]
            )
        sorted_longest_row = sorted(longest_row)
        sorted_arg_list = []
        for i in range(len(arg_list)):
            sorted_arg_list.append(
                Vector(Tuple(list(arg_list[sorted_longest_row[i][1]])))
            )
        return sorted_arg_list


class SLE(Matrix):
    """System of linear equations"""
    def __init__(self, *args: List[REAL]):
        """Initializes a matrix that contains both, coefficients and results.
        Insert in the following way:

        SLE([a_11, a_12, a_13, b_1],
            [a_21, a_22, a_23, b_2],
            [a_31, a_32, a_33, b_3])
         for
         | a_11 x_1 + a_12 x_2 + a_13 x_3 = b_1 |
         | a_21 x_1 + a_22 x_2 + a_23 x_3 = b_2 |
         | a_31 x_1 + a_32 x_2 + a_33 x_3 = b_3 |
         """
        super().__init__(*args)
        if self.size()[1] != self.size()[0] + 1:
            raise MatrixError(
                "Matrix for SLE must have the size m x n where n = m +1"
            )
        self.A = self.remove(column_index=-1)
        self.b = self.column(-1)

    def solve(self) -> 'Vector':
        """Splits matrix in coefficients and results and
        uses matrix multiplication to solve the system.
        """
        return self.A.inverse() * self.b

    def x(self, index: int) -> REAL:
        """Returns the unknown of given index. Starts at 0"""
        return self.solve()[index]
