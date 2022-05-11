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
        ta = a[:]
        for i in range(vec_dims):
            ta[i] *= t
        self.assertEqual(scamul(a, t), ta)

    def test_dot(self):
        a = [randint(-10, 10) for _ in range(vec_dims)]
        b = [randint(-10, 10) for _ in range(vec_dims)]
        res = sum([a[i] * b[i] for i in range(vec_dims)])
        self.assertEqual(dot(a, b), res)

    def test_cross2x2(self):
        a = [randint(-10, 10) for _ in range(2)]
        b = [randint(-10, 10) for _ in range(2)]
        res = a[0] * b[1] - a[1] * b[0]
        self.assertEqual(cross2x2(a, b), res)

    def test_cross3x3(self):
        a = [randint(-10, 10) for _ in range(3)]
        b = [randint(-10, 10) for _ in range(3)]
        res = [a[1]*b[2] - a[2]*b[1],
               a[2]*b[0] - a[0]*b[2],
               a[0]*b[1] - a[1]*b[0]]
        self.assertEqual(cross3x3(a, b), res)

    def test_intpow(self):
        a = [randint(-10, 10) for _ in range(vec_dims)]
        power = randint(1, 10)
        res = a[:]
        for i in range(power - 1):
            if i % 2 == 0:
                res = dot(a, res)
            else:
                res = scamul(a, res)
        self.assertEqual(intpow(a, power), res)

    def test_lead0(self):
        a = [0 for _ in range(vec_dims)]
        self.assertEqual(lead0(a), len(a))
        b = [1 for _ in range(vec_dims)]
        self.assertEqual(lead0(b), 0)
        c = [randint(-10, 10) for _ in range(vec_dims)]
        l0 = lead0(c)
        for ele in c[:l0]:
            self.assertEqual(ele, 0)

    def test_euclidean(self):
        a = [randint(-10, 10) for _ in range(vec_dims)]
        norm = sum([ele**2 for ele in a])**0.5
        self.assertAlmostEqual(norm, euclidean(a), delta=1e-14)


if __name__ == "__main__":
    unittest.main()
