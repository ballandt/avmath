from . import ArgumentError, sin, arccos, pi
import logging


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
    different amounts of columns and rows."""

    def __init__(self, got, want):
        self.got = got
        self.want = want

    def __str__(self):
        return "Matrix with "+str(self.got)+" rows cannot be multiplied with "+str(self.want)+"column matrix."


class GeometricalWarning:
    """Raised if shape without opt="flat" is called, but flat returns 'False'. Program does not get interrupted.
    Use 'GeometricalWarning.disable_warning()' to ignore warning."""
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

    def get(self, mode):
        """Returns float value of angle. Mode defines angle mode and is the entered
        mode if nothing is defined. If defined,mode must be given as
        f.e. 'evmath.Angle.DEG'."""
        return self.value * mode / self.mode if mode != self.mode else self.value


class Point:
    """A coordinate in a coordinate system with any amount of dimensions."""
    def __init__(self, *args):
        self.value = list(args)
        self.dims = len(self.value)

    def __getitem__(self, item):
        return self.value[item]

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
        area = 0.5*b*c*(sin(alpha.get(Angle.RAD)))
        return area


class Vector:
    """A vector with any amount of dimensions."""
    
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
        return str(self.value)

    def __neg__(self):
        """Returns negative vector."""
        return -1 * self
    
    def __len__(self):
        """Returns the amount of dimensions of a vector."""
        return len(self.value)

    def __eq__(self, other):
        """Return the equality of the vector's values"""
        return self.value == other.value

    def __ne__(self, other):
        """Returns the negative equality of the vector's values"""
        return self.value != other.value

    def __abs__(self):
        """Returns absolute of a vector.
            abs(vector) can be used."""
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

    def __mul__(self, arg2):
        """Scalar multiplication of two vectors.
            Can also be used for vector and scalar."""
        if type(arg2) in (int, float):
            return Vector.__scalar_mul(arg2, self)
        elif arg2.dims != self.dims:
            raise AmountOfDimensionsError(self.dims, arg2.dims)
        res = [self.value[i] * arg2.value[i] for i in range(self.dims)]
        ares = 0
        for e in res:
            ares += e
        return ares

    __rmul__ = __mul__

    def __truediv__(self, sca):
        """Division operator in order vector / scalar."""
        res = [self.value[i] / sca for i in range(self.dims)]
        return Vector(*tuple(res))
    
    def __pow__(self, arg2):
        """Vector multiplication. (No other sign available)
            vector1 ** vector2 (= vector1 x vector2) can be used.
            Only 3 dimensions supported."""
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
        for i in range(len(vecs)-1):
            flat = flat and ((vecs[i] ** vecs[i+1]).unitvec() == uvec)
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
        cosang = spr/(abs1*abs2)
        ang = arccos(cosang)
        return Angle(rad=ang)


class Area:
    def __init__(self, ovec, rvec1, rvec2):
        self.ovec = ovec
        self.rvec1 = rvec1
        self.rvec2 = rvec2
        self.area = abs(rvec1 ** rvec2)
    
    def nvec(self):
        return self.rvec1 ** self.rvec2


class Straight:
    def __init__(self, mode, **kwargs):
        if mode == "normal":
            self.sv = kwargs['sv']
            self.dv = kwargs['dv']
            self.par = kwargs['par']
            self.x = self.sv + (self.dv * self.par)


class Structure:
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
    """A mathematical matrix with any amount of rows and columns."""

    def __init__(self, *args):
        """Initializes the matrix. Enter a list for each row."""
        self.value = list(args)
        for e in self.value:
            if not len(self.value[0]) == len(e):
                raise ArgumentError(e, "row with "+str(len(self.value[0]))+" members")
        self.size = (len(self.value[0]), len(self.value))
        self.rows = self.size[0]
        self.columns = self.size[1]

    def __repr__(self):
        """Prints matrix in an understandable view."""
        b_e_list = []
        for e in self.value:
            b_e_list.append(sorted(e)[-1]) if abs(sorted(e)[-1]) > abs(sorted(e)[0]) else b_e_list.append(sorted(e)[0])
        b_e = sorted(b_e_list)[-1] if abs(sorted(b_e_list)[-1]) > abs(sorted(b_e_list)[0]) else sorted(b_e_list)[0]
        digits = len(str(b_e))
        ret_str = ""
        for e in self.value[0]:
            ret_str += str(e) + ((digits - len(str(e)) + 1) * " ")
        for i in range(1, len(self.value)):
            ret_str += "\n"
            for e in self.value[i]:
                ret_str += str(e) + (digits - len(str(e)) + 1) * " "
        return ret_str

    def __getitem__(self, item):
        """Returns item. To be used in following order:
        'matrix[x][y]'."""
        return self.value[item]

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
        elif self.size != other.size:
            raise ArgumentError("matrix with size "+str(other.size), "matrix with size"+str(self.size))
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
            return Matrix.__scmul(self, other)
        elif self.columns != other.rows:
            raise MatrixMultiplicationError(self.columns, other.rows)
        ret_mat = Matrix.create(self.size[0], other.size[1])
        for i in range(self.rows):
            for j in range(self.columns):
                ret_mat[i][j] = Vector(*tuple(self.row(i))) * Vector(*tuple(other.column(j)))
        return ret_mat

    __rmul__ = __mul__

    def __pow__(self, power):
        """Power operation for matrix^scalar."""
        ret_mat = self
        for i in range(1, power):
            ret_mat *= self
        return ret_mat

    def __scmul(self, other):
        """Intern scalar multiplication method"""
        args = []
        for i in range(len(self.value)):
            args.append([])
            for e in self.value[i]:
                args[i].append(e * other)
        return Matrix(*tuple(args))

    def dots(self):
        """Returns amount of coefficients."""
        return self.size[0] * self.size[1]

    def index(self, ele):
        """Returns position of given ele in a list. Can contain
        multiple return arguments. If ele is not in matrix an
        empty list is returned."""
        position = []
        for i in range(len(self.value)):
            for e in self.value[i]:
                if ele == e:
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
            if len(row) != self.size[0]:
                raise MatrixSizeError("Cannot append"+str(len(row))+"element row to matrix with size"+str(self.size))
            ret_mat.value.append(row)
        elif column:
            if len(column) != self.size[1]:
                raise MatrixSizeError("Cannot append"+str(len(column))+"element row to matrix with size"+str(self.size))
            for i in range(ret_mat.rows):
                ret_mat.value[i].append(column[i])
        return ret_mat

    def transpose(self):
        """Method for matrix transposition.
        a b          a c
        c d     gets b d"""
        args = []
        for i in range(self.columns):
            args.append(self.column(i))
        return Matrix(*tuple(args))

    @staticmethod
    def create(m, n):
        """Staticmethod to create a mXn matrix that contains
        only 0s."""
        args = []
        for i in range(n):
            args.append([])
            for j in range(m):
                args[i].append(0)
        return Matrix(*tuple(args))

    @staticmethod
    def create_identity(rows):
        """Staticmethod to create an identity matrix with any
        amount of rows."""
        ret_mat = Matrix.create(rows, rows)
        for i in range(rows):
            for j in range(rows):
                ret_mat[i][j] = 1 if i == j else 0
        return ret_mat
