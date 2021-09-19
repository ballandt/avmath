"""AVMATH LINA
AdVanced math LINear Algebra is a submodule of avmath.
It contains linear algebra features like vectors, matrices
angles and systems of linear equations.
It is an mathematically independent submodule, but needs to
import copy and logging for intern handling.
"""

import copy
import logging

from . import ArgumentError, sin, arccos, pi


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


class Angle:
    """Class for angle handling"""

    DEG = 90
    GRA = 100
    RAD = pi()

    def __init__(self, deg=None, rad=None, gra=None):
        if deg:
            self.value = deg
            self.mode = Angle.DEG
        elif rad:
            self.value = rad
            self.mode = Angle.RAD
        elif gra:
            self.value = gra
            self.mode = Angle.GRA

    def __eq__(self, other):
        """Checks equality of Points. Uses _FLOAT_EQ to prevent errors
        due to float operations."""
        from . import _FLOAT_EQ
        return abs(self.get(Angle.RAD) - other.get(Angle.RAD)) <= _FLOAT_EQ

    def get(self, mode):
        """Returns float value of angle. Mode defines angle mode and is the entered
        mode if nothing is defined. If defined,mode must be given as
        f.e. 'avmath.Angle.DEG'."""
        return self.value * mode / self.mode if mode != self.mode else self.value


class Point:
    """A coordinate in a coordinate system with any amount of dimensions."""

    def __init__(self, *args):
        self.value = list(args)
        self.dims = len(self.value)

    def __getitem__(self, item):
        return self.value[item]

    def __eq__(self, other):
        """Returns the equality of two points. Uses _FLOAT_EQ to compare."""
        from . import _FLOAT_EQ
        if not Point.dimcheck(self, other):
            return False
        for i in range(len(self.value)):
            if abs(self.value[i] - other.value[i]) > _FLOAT_EQ:
                return False
            else:
                pass
        return True

    def expand(self, args):
        """Expands Point -by- 'args' dimensions."""
        for _ in range(args):
            self.value.append(0)
        return Point(*self.value)

    @staticmethod
    def dimcheck(*args):
        """Returns 'True' if arguments have same amount of dimensions. Else returns 'False'."""
        dims = args[0].dims
        dimstrue = True
        for i in range(len(args)):
            dimstrue = dimstrue and (dims == args[i].dims)
        return dimstrue

    @staticmethod
    def triangulate(p1, p2, p3):
        """Returns area between three points."""
        abv = Vector(begin=p1, end=p2)
        acv = Vector(begin=p1, end=p3)
        c = abs(abv)
        b = abs(acv)
        alpha = Vector.angle(abv, acv)
        area = 0.5 * b * c * (sin(alpha.get(Angle.RAD)))
        return area


class Vector:
    """Vector with any amount of dimensions."""

    def __init__(self, *args, begin=None, end=None):
        if not begin:
            self.value = list(args)
            self.dims = len(self.value)
        else:
            if type(begin) != Point or type(end) != Point:
                raise ArgumentError([type(begin), type(end)], Point)
            if begin.dims != end.dims:
                raise DimensionError(end.dims, begin.dims)
            self.value = [end[i] - begin[i] for i in range(begin.dims)]
            self.dims = len(self.value)

    def __getitem__(self, item):
        """Returns value of 'item's dimension."""
        return self.value[item]

    def __repr__(self):
        """Returns string for built-in print function."""
        return str(Matrix(self))

    def __len__(self):
        """Returns the amount of dimensions of a vector."""
        return len(self.value)

    def __neg__(self):
        """Returns negative vector."""
        return -1 * self

    def __eq__(self, other):
        """Return the equality of the vector's values. Uses _FLOAT_EQ
        to compare.
        """
        from . import _FLOAT_EQ
        if not Vector.dimcheck(self, other):
            return False
        for i in range(self.dims):
            if abs(self.value[i] - other.value[i]) > _FLOAT_EQ:
                return False
            else:
                pass
        return True

    def __abs__(self):
        """Returns absolute of a vector.
            abs(vector) can be used.
            """
        res = 0
        for i in range(self.dims):
            res += self.value[i] ** 2
        self.abs = res ** 0.5
        return self.abs

    def __add__(self, other):
        """Adds two vectors."""
        if not Vector.dimcheck(self, other):
            raise DimensionError(other.dims, self.dims)
        res = [self.value[i] + other.value[i] for i in range(self.dims)]
        return Vector(*tuple(res))

    def __sub__(self, other):
        """Subtracts two vectors."""
        return self + -other

    def __mul__(self, other):
        """Scalar multiplication of two vectors.
            Can also be used for vector and scalar.
            """
        if type(other) in (int, float):
            return Vector.__scalar_mul(other, self)
        if other.dims != self.dims:
            raise AmountOfDimensionsError(self.dims, other.dims)
        res = [self.value[i] * other.value[i] for i in range(self.dims)]
        ares = 0
        for e in res:
            ares += e
        return ares

    __rmul__ = __mul__

    def __truediv__(self, sca):
        """Division operator in order vector / scalar. Mathematically incorrect,"""
        res = [self.value[i] / sca for i in range(self.dims)]
        return Vector(*tuple(res))

    def __pow__(self, arg2):
        """Vector multiplication. (No other sign available)
            vector1 ** vector2 (= vector1 x vector2) can be used.
            Only 3 dimensions supported.
            """
        if self.dims != 3:
            raise AmountOfDimensionsError(self.dims, 3)
        elif arg2.dims != 3:
            raise AmountOfDimensionsError(arg2.dims, 3)
        res = [0, 0, 0]
        res[0] = (self.value[1] * arg2.value[2]) - (self.value[2] * arg2.value[1])
        res[1] = (self.value[2] * arg2.value[0]) - (self.value[0] * arg2.value[2])
        res[2] = (self.value[0] * arg2.value[1]) - (self.value[1] * arg2.value[0])
        return Vector(*tuple(res))

    def unitvec(self):
        """Returns vector with absolute 1 and same direction as self."""
        if abs(self) == 0:
            raise GeometricalError("Vector with absolute 0 has no unitvec")
        else:
            res = self / abs(self)
            return res

    @staticmethod
    def spat(vec1, vec2, vec3):
        """Returns spat volume in following formula: (vec1 x vec2) * vec3"""
        return (vec1 ** vec2) * vec3

    @staticmethod
    def dimcheck(*args):
        """Returns 'True' if arguments have same amount of dimensions. Else returns 'False'."""
        dims = args[0].dims
        dimstrue = True
        for i in range(len(args)):
            dimstrue = dimstrue and (dims == args[i].dims)
        return dimstrue

    @staticmethod
    def flat(*args):
        """Returns 'True' if area between vectors is flat. Else returns 'False'"""
        twodims = True
        for e in args:
            twodims = twodims and e.dims == 2
        if twodims:
            return True
        vecs = list(args)
        flat = True
        uvec = (vecs[0] ** vecs[1]).unitvec()
        for i in range(len(vecs) - 1):
            flat = flat and ((vecs[i] ** vecs[i + 1]).unitvec() == uvec)
        return flat

    @staticmethod
    def __scalar_mul(sca, vec):
        """Intern scalar multiplication function."""
        res = [sca * vec.value[i] for i in range(vec.dims)]
        return Vector(*tuple(res))

    @staticmethod
    def angle(vec1, vec2):
        """Returns angle between two vectors."""
        if not Vector.dimcheck(vec1, vec2):
            raise DimensionError(vec2.dims, vec1.dims)
        if vec1.dims != 2 and vec1.dims != 3:
            raise AmountOfDimensionsError(vec1.dims, "2 or 3")
        spr = vec1 * vec2
        abs1 = abs(vec1)
        abs2 = abs(vec2)
        cosang = spr / (abs1 * abs2)
        ang = arccos(cosang)
        return Angle(rad=ang)


class Area:
    """Vector area"""
    def __init__(self, ovec, rvec1, rvec2):
        self.ovec = ovec
        self.rvec1 = rvec1
        self.rvec2 = rvec2
        self.area = abs(rvec1 ** rvec2)

    def nvec(self):
        """Returns normal vector of area."""
        return self.rvec1 ** self.rvec2


class Straight:
    """Vector straight"""
    def __init__(self, mode, **kwargs):
        if mode == "normal":
            self.sv = kwargs['sv']
            self.dv = kwargs['dv']
            self.par = kwargs['par']
            self.x = self.sv + (self.dv * self.par)


class Structure:
    """Point structure"""
    def __init__(self, *args):
        """A class for calculations with many points."""
        self.points = args

    def circ(self):
        """Returns the circumference of the area between any amount of points."""
        if not Point.dimcheck(*self.points):
            raise DimensionError(other="Points have different amount of dimensions.")
        u = 0
        for i in range(len(self.points)):
            if i < (len(self.points) - 1):
                u += abs(Vector(begin=self.points[i], end=self.points[i + 1]))
            elif i == (len(self.points) - 1):
                u += abs(Vector(begin=self.points[i], end=self.points[0]))
        return u

    def area(self, opt=None):
        """Returns area between any amount of points."""
        if not Vector.dimcheck(*self.points):
            raise DimensionError(other="Points have different amount of dimensions.")
        # args = list(self.points)
        twodim = True
        for i in range(len(self.points)):
            if self.points[i].dims == 2:
                pass
            else:
                twodim = False
        vecs = []
        for i in range(len(self.points)):
            if i < len(self.points) - 1:
                vecs.append(Vector(begin=self.points[i], end=self.points[i + 1]))
            else:
                vecs.append(Vector(begin=self.points[i], end=self.points[0]))
        a = 0
        if opt == "flat":
            if not Vector.flat(*vecs):
                raise GeometricalError("No flat area found.")
            for i in range(len(self.points) - 2):
                a += Point.triangulate(self.points[0], self.points[i + 1], self.points[i + 2])
            return a
        elif opt is None:
            if not Vector.flat(*vecs):
                GeometricalWarning("Area is not flat.")
            for i in range(len(self.points) - 2):
                a += Point.triangulate(self.points[0], self.points[i + 1], self.points[i + 2])
            return a
        elif opt == "twodim":
            if not twodim:
                raise DimensionError(other="Points do not have 2 dimensions")
            for i in range(len(self.points) - 2):
                a += Point.triangulate(self.points[0], self.points[i + 1], self.points[i + 2])
            return a


class Matrix:
    """Mathematical matrix with any amount of rows and columns."""

    def __init__(self, *args):
        """Initializes the matrix. Enter a list for each row."""
        if len(args) == 1 and type(args[0]) == Vector:
            self.value = []
            for e in args[0].value:
                self.value.append([e])
        else:
            self.value = list(args)
            for e in self.value:
                if not len(self.value[0]) == len(e):
                    raise ArgumentError(e, "row with " + str(len(self.value[0])) + " members")

    def __repr__(self):
        """Prints matrix in an understandable view."""
        ret_str = "\n"
        if len(self.value) == 1:
            ret_str += "["
            for e in self.value[0]:
                ret_str += 2 * " " + str(e)
            ret_str += 2 * " " + "]"
            return ret_str
        longest_element_list = list(map(str, self.value[0]))
        for i in range(1, len(self.value)):
            for j in range(len(self.value[i])):
                if len(str(self.value[i][j])) > len(longest_element_list[j]):
                    longest_element_list[j] = str(self.value[i][j])
        digits_list = list(map(len, longest_element_list))
        b_element = sorted(digits_list)[-1]
        if b_element < 3:
            distance = 1
        if b_element < 8:
            distance = 2
        else:
            distance = 3
        for i in range(len(self.value)):
            if i == 0:
                ret_str += "┌" + distance * " "
            elif i == len(self.value) - 1:
                ret_str += "└" + distance * " "
            else:
                ret_str += "|" + distance * " "
            for j in range(len(self.value[i])):
                ret_str += str(self.value[i][j]) + ((digits_list[j] - len(str(self.value[i][j])) + distance) * " ")
            if i == 0:
                ret_str += "┐"
            elif i == len(self.value) - 1:
                ret_str += "┘"
            else:
                ret_str += "|"
            ret_str += "\n"
        return ret_str

    def __getitem__(self, item):
        """Returns item. To be used in following order:
        'matrix[m][n]'."""
        return self.value[item]

    def __eq__(self, other):
        """Returns equality of two matrices. Uses _FLOAT_EQ"""
        from . import _FLOAT_EQ
        if self.size() != other.size():
            return False
        for i in range(len(self.value)):
            for j in range(len(self.value[i])):
                if abs(self[i][j] - other[i][j]) > _FLOAT_EQ:
                    pass
                else:
                    return False
        return True

    def __neg__(self):
        """Returns negative matrix."""
        args = []
        for i in range(len(self.value)):
            args.append([])
            for j in range(len(self.value[i])):
                args[i].append(self[i][j] * -1)
        return Matrix(*tuple(args))

    def __add__(self, other):
        """Adds two matrices."""
        if type(other) != Matrix:
            raise ArgumentError(type(other), Matrix)
        elif self.size() != other.size():
            raise ArgumentError("matrix with size " + str(other.size()), "matrix with size" + str(self.size()))
        args = []
        for i in range(len(self.value)):
            args.append([])
            for j in range(len(self.value[i])):
                args[i].append(self[i][j] + other[i][j])
        return Matrix(*tuple(args))

    def __sub__(self, other):
        """Subtracts a matrix from another."""
        return self + -other

    def __mul__(self, other):
        """Multiplies two matrices."""
        if type(other) == int or type(other) == float:
            return Matrix.__scalar_mul(self, other)
        elif type(other) == Vector:
            if self.size()[1] != other.dims:
                raise MatrixMultiplicationError(str(self.size()[1]), other.dims)
            v_matrix = Matrix(other)
            ret_mat = self * v_matrix
            args = ()
            for e in ret_mat.value:
                args += (e[0],)
            return Vector(*args)
        elif self.size()[1] != other.size()[0]:
            raise MatrixMultiplicationError(other.size()[0], self.size()[1])
        ret_mat = Matrix.create(self.size()[0], other.size()[1])
        for i in range(self.size()[0]):
            for j in range(other.size()[1]):
                ret_mat[i][j] = Vector(*tuple(self.row(i))) * Vector(*tuple(other.column(j)))
        return ret_mat

    __rmul__ = __mul__

    def __pow__(self, power):
        """Power operation for matrix^scalar."""
        ret_mat = self
        if power == -1:
            return self.inverse()
        for i in range(1, power):
            ret_mat *= self
        return ret_mat

    def __scalar_mul(self, other):
        """Intern scalar multiplication method"""
        args = []
        for i in range(len(self.value)):
            args.append([])
            for e in self.value[i]:
                args[i].append(e * other)
        return Matrix(*tuple(args))

    def size(self, option=None):
        """Returns list of matrix size. [m, n]"""
        if not option:
            return [len(self.value), len(self.value[0])]
        elif option == "xy":
            return [len(self.value[0]), len(self.value)]

    def at(self, m, n):
        """Returns element at given position. Begins at 0."""
        return self.value[m][n]

    def index(self, element):
        """Returns position of given element in a list. Can contain
        multiple return arguments. If ele is not in matrix an
        empty list is returned."""
        position = []
        for i in range(len(self.value)):
            for e in self.value[i]:
                if element == e:
                    position.append([self.value[i].index(e), i])
        return position

    def column(self, cindex):
        """Returns column with specific index."""
        ret_list = []
        for e in self.value:
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
            ret_mat.value.append(row)
        elif column:
            if len(column) != self.size()[0]:
                raise MatrixSizeError("Cannot append " + str(len(column))
                                      + " element row to matrix with size" + str(self.size()))
            for i in range(ret_mat.size()[1]):
                ret_mat.value[i].append(column[i])
        return ret_mat

    def remove(self, rindex=None, cindex=None):
        """Returns a matrix with given row or column removed."""
        ret_mat = copy.deepcopy(self)
        if rindex is not None:
            del ret_mat.value[rindex]
        if cindex is not None:
            for i in range(len(ret_mat.value)):
                del ret_mat.value[i][cindex]
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

    @staticmethod
    def create(m, n):
        """Staticmethod to create a m X n matrix that contains
        only 0s.
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
