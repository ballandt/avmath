"""AVMATH ALGEBRA
AdVanced math algebra submodule containing
linear algebra features like vectors, matrices
angles and systems of linear equations.
It is an mathematically independent submodule,
but needs to import copy and logging for intern
handling.
"""

import copy
import logging
from typing import Union, Optional

from . import ArgumentError, sin, arccos, _check_types


class DimensionError(Exception):
    """Raised if arguments have different amount of dimensions."""

    def __init__(self, got=None, want=None, other=None):
        if other is None:
            self.got = got
            self.want = want
        else:
            self.other = other

    def __str__(self):
        try:
            return "Different amount of dimensions. Expected " + str(self.want) + "; got " + str(self.got)
        except AttributeError:
            return self.other


class AmountOfDimensionsError(Exception):
    """Raised if vector has not got a defined amount of dimensions."""

    def __init__(self, got, want):
        self.got = got
        self.want = want

    def __str__(self):
        return "Wrong amount of dimensions. Expected " + str(self.want) + "; got " + str(self.got)


class GeometricalError(Exception):
    """Raised if shape with opt="flat" is called, but the flat returns 'False'"""

    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return self.arg


class MatrixSizeError(Exception):
    """Raised if operations require matrix with wrong size."""

    def __init__(self, issue):
        self.arg = issue

    def __str__(self):
        return self.arg


class MatrixMultiplicationError(Exception):
    """Raised if matrix multiplication can not be executed due to
    different amounts of columns and rows.
    """

    def __init__(self, got, want):
        self.got = got
        self.want = want

    def __str__(self):
        return "Matrix with " + str(self.got) + " rows cannot be multiplied with " + str(self.want) + "column matrix."


class GeometricalWarning:
    """Raised if shape without opt="flat" is called, but flat returns 'False'. Program does not get interrupted.
    Use 'GeometricalWarning.disable_warning()' to ignore warning.
    """
    __warning = True

    def __init__(self, arg):
        if GeometricalWarning.__warning:
            logging.warning(arg)
        else:
            pass

    @classmethod
    def disable_warning(cls):
        GeometricalWarning.__warning = False


# class Angle:
#     """Class for angle handling"""
#
#     DEG = 90
#     GRA = 100
#     RAD = pi
#
#     def __init__(self, deg=None, rad=None, gra=None):
#         if deg:
#             self.__value = deg
#             self.mode = Angle.DEG
#         elif rad:
#             self.__value = rad
#             self.mode = Angle.RAD
#         elif gra:
#             self.__value = gra
#             self.mode = Angle.GRA
#
#     def __eq__(self, other):
#         """Checks equality of Points. Uses _FLOAT_EQ to prevent errors
#         due to float operations."""
#         from . import _FLOAT_EQ
#         return abs(self.get(Angle.RAD) - other.get(Angle.RAD)) <= _FLOAT_EQ
#
#     def get(self, mode):
#         """Returns float value of angle. Mode defines angle mode and is the entered
#         mode if nothing is defined. If defined,mode must be given as
#         f.e. 'avmath.Angle.DEG'.
#         """
#         return self.__value * mode / self.mode if mode != self.mode else self.__value


class Tuple:
    """Algebraic tuple. Can also be interpreted as point in the coordinate system."""

    def __init__(self, *args: Union[int, float, complex, list]):
        _check_types(args, int, float, complex, list)
        if type(args[0]) == list:
            self._value = args[0]
        self._value = list(args)

    def __iter__(self):
        for ele in self._value:
            yield ele

    def __getitem__(self, item):
        """Returns value of 'item's dimension."""
        return self._value[item]

    # def __setitem__(self, key, value):
    #     """Sets specific item in copied version. Warning: operation changes
    #     mutable _value list so all id-members will be infected.
    #     """
    #     self._value[key] = value

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

    def __neg__(self) -> 'Tuple':
        return self * -1

    def __add__(self, other: 'Tuple') -> 'Tuple':
        """Adds two tuples:
        a + b = (a_1 + b_1, a_2 + b_2, ... , a_n + b_n)
        """
        if not Tuple.dimcheck(self, other):
            raise AmountOfDimensionsError(other.dim(), self.dim())
        result = []
        for i in range(self.dim()):
            result.append(self[i] + other[i])
        return Tuple(*tuple(result))

    def __sub__(self, other: 'Tuple') -> 'Tuple':
        """Reversed addition:
        a - b = a + (-b)"""
        return self + -other

    def __mul__(self, other: Union[int, float]):
        """Scalar multiplication:
        r * a = (r*a_1, r*a_2, ... , r*a_n)    (a e R^n, r e R)"""
        result = []
        for ele in self._value:
            result.append(ele * other)
        return Tuple(*tuple(result))

    __rmul__ = __mul__

    def append(self, value: Union[int, float]):
        """Expands tuple by args dimensions."""
        self._value.append(value)

    @staticmethod
    def dimcheck(*args) -> bool:
        """Checks if arguments have the same amount of dimensions."""
        dimension = args[0].dim()
        for ele in args:
            if not ele.dim() == dimension:
                return False
        return True

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


class Vector(Tuple):
    """Vector with any amount of dimensions."""

    def __init__(self, *args: Union[int, float, complex, 'Tuple'],
                 begin: Optional['Tuple'] = None,
                 end: Optional['Tuple'] = None):

        if not begin and type(args[0]) != Tuple:
            super().__init__(*args)

        elif not begin and type(args[0]) == Tuple:
            super().__init__(*tuple(args[0]))

        else:
            _check_types((begin, end), Tuple)
            if begin.dim() != end.dim():
                raise DimensionError(end.dim(), begin.dim())
            super().__init__(*tuple([end[i] - begin[i] for i in range(begin.dim())]))

    def __abs__(self):
        """Returns absolute of a vector.
            abs(vector) can be used.
            """
        res = 0
        for i in range(self.dim()):
            res += self._value[i] ** 2
        self.abs = res ** 0.5
        return self.abs

    def __mul__(self, other: Union['Vector', int, float, complex]):
        """Scalar multiplication of two vectors.
            """
        if type(other) != Vector:
            return Vector(Tuple(*tuple(self)) * other)
        if not Vector.dimcheck(self, other):
            raise AmountOfDimensionsError(self.dim(), other.dim())
        res = 0
        for i in range(self.dim()):
            res += self[i] * other[i]
        return res

    __rmul__ = __mul__

    def __pow__(self, power: int, modulo=None):
        _check_types((power,), int)
        if power == 0:
            return self.unit()
        res = 1
        for i in range(power):
            res *= self
        return res

    def cross(self, other: 'Vector') -> 'Vector':
        """Vector multiplication.
            vector1 * vector2 means vector1 x vector2
            Only 3 dimensions supported.
            """
        if self.dim() != 3:
            raise AmountOfDimensionsError(self.dim(), 3)
        elif other.dim() != 3:
            raise AmountOfDimensionsError(other.dim(), 3)
        res = [0, 0, 0]
        res[0] = (self[1] * other[2]) - (self[2] * other[1])
        res[1] = (self[2] * other[0]) - (self[0] * other[2])
        res[2] = (self[0] * other[1]) - (self[1] * other[0])
        return Vector(*tuple(res))

    def unit(self) -> 'Vector':
        """Returns vector with absolute 1 and same direction as self."""
        if abs(self) == 0:
            raise GeometricalError("Vector with absolute 0 has no unitvec")
        else:
            res = self * (1 / abs(self))
            return res

    @staticmethod
    def spat(a: 'Vector', b: 'Vector', c: 'Vector') -> float:
        """Returns spat volume in following formula: (a x b) * c"""
        return (a.cross(b)) * c

    @staticmethod
    def lin_indep(*args: 'Vector', dim: int) -> bool:
        """Returns 'True' if area between vectors is flat. Else returns 'False'"""
        twodims = True
        for e in args:
            twodims = twodims and e.dim() == 2
        if twodims and dim > 2:
            return True
        unitvector = args[0].unit()
        for e in args:
            if e.unit() != unitvector:
                return False
        return True

    @staticmethod
    def angle(a: 'Vector', b: 'Vector') -> float:
        """Returns angle between two vectors."""
        if not Vector.dimcheck(a, b):
            raise DimensionError(b.dim(), a.dim())
        if a.dim() not in (2, 3):
            raise AmountOfDimensionsError(a.dim(), "2 or 3")
        angle = arccos(a*b / (abs(a) * abs(b)))
        return angle


class Structure:
    """Point structure"""
    def __init__(self, *args: 'Tuple'):
        _check_types(args, Tuple)
        if not Tuple.dimcheck(*args):
            raise DimensionError(other="Tuples have different amount of dimensions.")
        self.points = args
        self.vectors = [Vector(begin=self.points[-1], end=self.points[0])]
        for i in range(1, len(self.points)):
            self.vectors.append(Vector(begin=self.points[i - 1], end=self.points[i]))

    def flat(self):
        unitvector = (self.vectors[0].cross(self.vectors[-1])).unit()
        for i in range(len(self.vectors) - 1):
            if (self.vectors[i].cross(self.vectors[i+1])).unit() != unitvector:
                return False
        return True

    def circ(self):
        """Returns the circumference of the area opened by any amount of vectors."""
        u = 0
        for e in self.vectors:
            u += abs(e)
        return u

    def area(self, opt=None):
        """Returns area opened by any amount of vectors."""
        area = 0
        if opt == "flat":
            if not self.flat():
                raise GeometricalError("No flat area found.")
        if not self.flat():
            GeometricalWarning("Area does not seem to be flat.")
        for i in range(1, len(self.points) - 1):
            area += Tuple.triangulate(self.points[0], self.points[i], self.points[i + 1])
        return area


class Matrix(Tuple):
    """Mathematical matrix"""

    def __init__(self, *args: Union[list, 'Vector']):
        """Initializes the matrix. Enter a list for each row."""
        if type(args[0]) == Vector:
            value = []
            for e in args[0]._value:
                value.append([e])
        else:
            value = list(args)
            for e in value:
                if not len(value[0]) == len(e):
                    raise ArgumentError(e, "row with " + str(len(args[0])) + " members")
                # _check_types(e, int, float)
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
                ret_str += str(self[i][j]) + ((digits_list[j] - len(str(self[i][j])) + distance) * " ")
            if i == 0:
                ret_str += "┐"
            elif i == self.size()[0] - 1:
                ret_str += "┘"
            else:
                ret_str += "|"
            ret_str += "\n"
        return ret_str

    def __contains__(self, item: Union[int, float]) -> bool:
        ret_val = True
        for e in self._value:
            ret_val = ret_val and (item in e)
        return ret_val

    def __round__(self, n: int = None) -> 'Matrix':
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
            raise ArgumentError("matrix with size " + str(other.size()), "matrix with size" + str(self.size()))
        args = []
        for i in range(self.size()[0]):
            args.append([])
            for j in range(self.size()[1]):
                args[i].append(self[i][j] + other[i][j])
        return Matrix(*tuple(args))

    def __sub__(self, other: 'Matrix') -> 'Matrix':
        """Subtracts a matrix from another."""
        return self + -other

    def __mul__(self, other: Union['Matrix', 'Vector', int]) -> Union['Matrix', 'Vector']:
        """Multiplies two matrices."""
        if type(other) == int or type(other) == float:
            return Matrix.__scalar_multiplication(self, other)
        elif type(other) == Vector:
            if self.size()[1] != other.dim():
                raise MatrixMultiplicationError(str(self.size()[1]), other.dim())
            v_matrix = Matrix(other)
            ret_mat = self * v_matrix
            args = ()
            for e in ret_mat._value:
                args += (e[0],)
            return Vector(*args)
        elif type(other) == Matrix:
            if self.size()[1] != other.size()[0]:
                raise MatrixMultiplicationError(other.size()[0], self.size()[1])
            ret_mat = Matrix.create(self.size()[0], other.size()[1])
            for i in range(self.size()[0]):
                for j in range(other.size()[1]):
                    ret_mat[i][j] = Vector(*tuple(self.row(i))) * Vector(*tuple(other.column(j)))
            return ret_mat

    __rmul__ = __mul__

    def __pow__(self, power: int):
        """Power operation for matrix^scalar."""
        if self.size()[0] == self.size()[1]:
            raise MatrixSizeError("Matrix must be quadratic for A^0 = E_m")
        if type(power) is not int:
            raise ArgumentError("Power od type"+str(type(power)), int)
        ret_mat = self
        if power == -1:
            return self.inverse()
        elif power == 0:
            return Matrix.create_identity(self.size()[0])
        for i in range(1, power):
            ret_mat *= self
        return ret_mat

    def __scalar_multiplication(self, other):
        """Intern scalar multiplication method"""
        args = []
        for i in range(self.size()[0]):
            args.append([])
            for e in self[i]:
                args[i].append(e * other)
        return Matrix(*tuple(args))

    def size(self, option=None):
        """Returns list of matrix size. [m, n]"""
        if not option:
            return [len(self._value), len(self._value[0])]
        elif option == "xy":
            return [len(self._value[0]), len(self._value)]

    def dim(self):
        return self.size()[0] * self.size()[1]

    def at(self, m, n):
        """Returns element at given position. Begins at 0."""
        return self[m][n]

    def index(self, element):
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

    def column(self, cindex):
        """Returns column with specific index."""
        ret_list = []
        for e in self._value:
            ret_list.append(e[cindex])
        return ret_list

    def row(self, rindex):
        """Returns row with specific index."""
        return self[rindex]

    def append(self, row=None, column=None):
        """Method to append rows or columns to matrix."""
        ret_mat = self
        if row:
            if len(row) != self.size()[1]:
                raise MatrixSizeError(
                    "Cannot append" + str(len(row)) + "element row to matrix with size" + str(self.size()))
            ret_mat._value.append(row)
        elif column:
            if len(column) != self.size()[0]:
                raise MatrixSizeError("Cannot append " + str(len(column))
                                      + " element row to matrix with size" + str(self.size()))
            for i in range(ret_mat.size()[1]):
                ret_mat._value[i].append(column[i])
        return ret_mat

    def remove(self, rindex=None, cindex=None):
        """Returns a matrix with given row or column removed."""
        ret_mat = copy.deepcopy(self)
        if rindex is not None:
            del ret_mat._value[rindex]
        if cindex is not None:
            for i in range(len(ret_mat._value)):
                del ret_mat._value[i][cindex]
        return ret_mat

    def transpose(self):
        """Returns transposed matrix."""
        args = []
        for i in range(self.size()[1]):
            args.append(self.column(i))
        return Matrix(*tuple(args))

    def det(self):
        """Returns determinant of a matrix."""
        if self.size()[0] != self.size()[1]:
            raise MatrixSizeError("Matrix must be quadratic.")
        if self.size() == [2, 2]:
            return self[0][0] * self[1][1] - self[1][0] * self[0][1]
        else:
            answer = 0
            for i in range(self.size()[1]):
                smaller_matrix = self.remove(0, i)
                k = (-1) ** i * self[0][i] * smaller_matrix.det()
                answer += k
        return answer

    __abs__ = det

    def cof(self):
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

    def adj(self):
        """Returns adjunct of a matrix."""
        ret_mat = copy.deepcopy(self)
        return ret_mat.cof().transpose()

    def inverse(self):
        """Returns inverted matrix."""
        if self.size()[0] != self.size()[1]:
            raise MatrixSizeError("Matrix must be quadratic.")
        if self.det() == 0:
            raise ZeroDivisionError("Determinant must not be 0.")
        ret_mat = copy.deepcopy(self).adj()
        ret_mat *= 1 / self.det()
        return ret_mat

    # def ref(self):
    #     """Returns matrix in row echelon form."""
    #     copy_mat = copy.deepcopy(self)
    #     for i in range(copy_mat.size()[0]):
    #         copy_mat._value[i].append(i)
    #     sorted_rows = []
    #     for j in range(copy_mat.size()[1]):
    #         for i in range(copy_mat.size()[0]):
    #             if (copy_mat._value[i][j] != 0 or j == copy_mat.size()[1] - 1) and copy_mat._value[i] not in sorted_rows:
    #                 sorted_rows.append(copy_mat._value[i])
    #     for e in sorted_rows:
    #         e = e.pop()
    #     j = 0
    #     while sorted_rows[0][j] == 0:
    #         j += 1
    #     dividend = sorted_rows[0][j]
    #     for i in range(len(sorted_rows[0])):
    #         sorted_rows[0][i] /= dividend
    #     for k in range(j, len(sorted_rows[0])):
    #         for i in range(1, len(sorted_rows)):
    #             if sorted_rows[i][j] != 0:
    #                 pass
    #     return sorted_rows

    @staticmethod
    def create(m, n):
        """Staticmethod to create a m X n matrix that contains
        only zeros.
        """
        args = []
        for i in range(m):
            args.append([])
            for j in range(n):
                args[i].append(0)
        return Matrix(*tuple(args))

    @staticmethod
    def create_identity(rows):
        """Staticmethod to create an identity matrix with any
        amount of rows.
        """
        ret_mat = Matrix.create(rows, rows)
        for i in range(rows):
            for j in range(rows):
                ret_mat[i][j] = 1 if i == j else 0
        return ret_mat


class SLE(Matrix):
    """System of linear equations"""
    def __init__(self, *args):
        """Initializes a matrix that contains both, coefficients and results. Insert in the following way:
        SLE([a,b,c,d],
            [e,f,g,h],
            [i,j,k,l])
         for
         | a x1 + b x2 + c x3 = d |
         | e x1 + f x2 + g x3 = h |
         | i x1 + j x2 + k x3 = l |
         """
        super().__init__(*args)
        if self.size()[1] != self.size()[0] + 1:
            raise MatrixSizeError("Matrix for SLE must have the size m x n where n = m +1")

    def solve(self):
        """Splits matrix in coefficients and results and uses matrix multiplication to solve
        the system.
        """
        coefficients = copy.deepcopy(self).remove(cindex=-1)
        results = Matrix(self.column(-1)).transpose()
        return coefficients.inverse() * results

    def x(self, index):
        """Returns the unknown of given index. Starts at 0"""
        return self.solve().at(index, 0)
