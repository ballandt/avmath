"""AVMATH MATRIX FUNCTIONS

Definition of the methods for matrix calculation. For public API see
avmath.algebra.Matrix.

Contained functions do not check input, wrong arguments will raise unexpected
errors. Standard input and output type is two-dimensional list. Input lists
are not changed.
"""

from .vectors import dot


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
