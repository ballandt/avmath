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


def ref(mat):
    """Row echelon form using GAUSS-algorithm"""
    ret_mat = copy.deepcopy(mat)
    for i, ele in enumerate(ret_mat):
        ret_mat.sort(key=lambda vec: lead0(vec))
        if lead0(ele) == len(ele):
            continue
        ret_mat[i] = scamul(ele, div(1, ele[lead0(ele)]))
        for j, jele in enumerate(ret_mat[i:]):
            if lead0(jele) == lead0(ele):
                ret_mat[j] = vsub(jele, scamul(ele, jele[lead0(jele)]))
    return ret_mat
