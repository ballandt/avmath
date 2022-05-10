"""Vector tests"""

import unittest
from ..vectors import *
from random import randint

vec_dims = 5  # Dimensions for random vectors


class FunctionTests(unittest.TestCase):
    """Tests for private functions"""
    def test_add(self):
        self.assertEqual(add([0, 0], [0, 0]), [0, 0])
        randvec = [randint(-10, 10) for _ in range(vec_dims)]
        self.assertEqual(add([0 for _ in range(vec_dims)], randvec), randvec)
        a = [randint(-10, 10) for _ in range(vec_dims)]
        b = [randint(-10, 10) for _ in range(vec_dims)]
        res = [a[i] + b[i] for i in range(vec_dims)]
        self.assertEqual(add(a, b), res)
        n_a = [-ele for ele in a]
        self.assertEqual(add(a, n_a), [0 for _ in range(vec_dims)])

    def test_sub(self):
        a = [randint(-10, 10) for _ in range(vec_dims)]
        n_a = [-ele for ele in a]
        c = [randint(-10, 10) for _ in range(vec_dims)]
        self.assertEqual(sub(c, a), add(c, n_a))

    def test_scamul(self):
        a = [randint(-10, 10) for _ in range(vec_dims)]
        self.assertEqual(scamul(a, 0), [0 for _ in range(vec_dims)])
        t = randint(-10, 10)
        ta = a
        for i in range(vec_dims):
            ta[i] *= t
        self.assertEqual(scamul(a, t), ta)




if __name__ == "__main__":
    unittest.main()
