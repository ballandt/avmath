"""AVMATH MATRIX FUNCTIONS

Definition of the methods for matrix calculation. For public API see
avmath.algebra.Matrix.

Contained functions do not check input, wrong arguments will raise unexpected
errors. Standard input and output type is two-dimensional list. Input lists
are not changed.
"""
import copy

from .vectors import sub as vsub, scamul, dot, lead0
from .numbers import div


def add(mat1, mat2):
    """Matrix addition."""
    res = []
    for i in range(len(mat1)):
        res.append([])
        for j in range(len(mat1[1])):
            res[i].append(mat1[i][j]+mat2[i][j])
    return res


def sub(mat1, mat2):
    """Matrix subtraction."""
    res = []
    for i in range(len(mat1)):
        res.append([])
        for j in range(len(mat1[1])):
            res[i].append(mat1[i][j]-mat2[i][j])
    return res


def mul(mat1, mat2):
    """Matrix multiplication."""
    # Creates list of columns one time
    columns = []
    for i in range(len(mat2[0])):
        columns.append([])
        for j in range(len(mat2)):
            columns[i].append(mat2[j][i])
    res = []
    for i in range(len(mat1)):
        res.append([])
        for j in range(len(mat2[0])):
            res[i].append(dot(mat1[i], columns[j]))
    return res


def intpow(mat, power):
    """Power operation for quadratic matrix and integer.
        A ^ t := A * A * A * A    (a in R^{n x n}, t in R)
                  t times
    """
    # Creates list of columns one time instead of power times
    columns = []
    for i in range(len(mat[0])):
        columns.append([])
        for j in range(len(mat)):
            columns[i].append(mat[j][i])
    res = mat[:]
    for i in range(power-1):
        new_res = []
        for j in range(len(res)):
            new_res.append([])
            for k in range(len(res[0])):
                new_res[j].append(dot(res[j], columns[k]))
        res = new_res
    return res


def laplacedet(mat):
    """Determinant using Laplace development."""
    if len(mat) == 1:
        # Base case
        return mat[0][0]
    elif len(mat) == 3:
        # Rule of Sarrus for faster calculation
        return mat[0][0] * mat[1][1] * mat[2][2] \
               + mat[0][1] * mat[1][2] * mat[2][0] \
               + mat[0][2] * mat[1][0] * mat[2][1] \
               - mat[0][0] * mat[1][2] * mat[2][1] \
               - mat[0][1] * mat[1][0] * mat[2][2] \
               - mat[0][2] * mat[1][1] * mat[2][0]
    else:
        # Development
        res = 0
        for i in range(len(mat[0])):
            smaller_mat = []
            for j in range(1, len(mat)):
                smaller_mat.append(mat[j][:i] + mat[j][i+1:])
            res += (-1)**i * mat[0][i] * laplacedet(smaller_mat)
        return res


def diagonal(mat):
    """Transforms matrix to diagonal matrix using GAUSS-algorithm. Returns
    diagonal matrix and the factor of the change of the determinant.
    """
    ret_mat = copy.deepcopy(mat)
    det_fac = 1
    for i in range(len(ret_mat)):
        if lead0(ret_mat[i]) > i:
            for j in range(i+1, len(ret_mat)):
                if lead0(ret_mat[j]) == i:
                    ret_mat[i], ret_mat[j] = ret_mat[j], ret_mat[i]
                    det_fac *= -1
                    break
        if lead0(ret_mat[i]) == i:
            for j in range(i+1, len(ret_mat)):
                if lead0(ret_mat[j]) == i:
                    ret_mat[j] = vsub(
                        ret_mat[j],
                        scamul(ret_mat[i], div(ret_mat[j][i], ret_mat[i][i]))
                    )
    return ret_mat, det_fac


def gaussdet(mat):
    """Calculates determinant using diagonal matrix."""
    ret_mat, det = diagonal(mat)
    for i in range(len(ret_mat)):
        det *= ret_mat[i][i]
    return det


def ref(mat):
    """Row echelon form using GAUSS-algorithm"""
    ret_mat = copy.deepcopy(mat)
    for i in range(len(ret_mat)):
        ret_mat.sort(key=lambda vec: lead0(vec))
        if lead0(ret_mat[i]) == len(ret_mat[i]):
            continue
        ret_mat[i] = scamul(ret_mat[i], div(1, ret_mat[i][lead0(ret_mat[i])]))
        for j in range(i+1, len(ret_mat)):
            if lead0(ret_mat[j]) == lead0(ret_mat[i]):
                ret_mat[j] = vsub(
                    ret_mat[j],
                    scamul(ret_mat[i], ret_mat[j][lead0(ret_mat[j])])
                )
    return ret_mat


def rank(mat):
    """Rank of a matrix"""
    ret_val = len(mat)
    ret_mat = ref(mat)
    for ele in reversed(ret_mat):
        if lead0(ele) == len(ret_mat[0]):
            ret_val -= 1
        else:
            break
    return ret_val


def rref(mat):
    """Reduced row echelon form of a matrix"""
    ret_mat = ref(mat)
    n = len(ret_mat[0])
    for i in range(len(ret_mat)-1, 0, -1):
        if lead0(ret_mat[i]) == n:
            continue
        for j in range(i):
            ret_mat[j] = vsub(
                ret_mat[j],
                scamul(ret_mat[i], ret_mat[j][lead0(ret_mat[i])])
            )
    return ret_mat


def solve(mat):
    """Solves the system of linear equations"""
    ret_mat = rref(mat)
    ret_val = []
    m = len(ret_mat)
    n = len(ret_mat[0])
    if m <= n-1:
        for i in range(m-1, -1, -1):
            l0 = lead0(ret_mat[i])
            if l0 == n:
                ret_val.append(1)
            elif l0 == n - 1:
                raise ArithmeticError("Cannot calculate solutions")
            else:
                ret_val.append(ret_mat[i][n-1])
                for j in range(l0+1, n-2):
                    ret_val[-1] -= ret_mat[i][j] * ret_val[i-j]
        return list(reversed(ret_val))
    else:
        for i in range(m-1, n-2, -1):
            if lead0(ret_mat[i]) != n:
                raise ArithmeticError("Cannot calculate solutions: overdetermined")
        for i in range(n-2, -1, -1):
            l0 = lead0(ret_mat[i])
            if l0 == n:
                ret_val.append(1)
            elif l0 == n - 1:
                raise ArithmeticError("Cannot calculate solutions")
            else:
                ret_val.append(ret_mat[i][n-1])
                for j in range(l0+1, n-2):
                    ret_val[-1] -= ret_mat[i][j] * ret_val[i-j]
        return list(reversed(ret_val))

