import unittest
import avmath
from avmath import algebra


class TupleTest(unittest.TestCase):

    def testInit(self):
        a = algebra.Tuple(1, 0, 0)
        b = algebra.Tuple(1e3, 1, 0)
        c = algebra.Tuple(0, 3+4j, 1)
        d = algebra.Tuple([4, 3e2, 1+4j])

        self.assertRaises(avmath.ArgumentError, algebra.Tuple.__init__, 1, "e", 0)

    def testIter(self):
        a = algebra.Tuple(2, 4, 3)
        self.assertEqual(list(a), [2, 4, 3])

    def testAdd(self):
        a = algebra.Tuple(2, 3+3j, 0)
        b = algebra.Tuple(-5, 3, 1e3)
        res = algebra.Tuple(-3, 6+3j, 1000)

        self.assertEqual(a+b, res)

    def testTriangulate(self):
        a = algebra.Tuple(2, 5, 4)
        b = algebra.Tuple(-2, 4, 1e1)
        c = algebra.Tuple(0, 0, 3)
        d = algebra.Tuple(2-3j, 3, 0)

        self.assertAlmostEqual(algebra.Tuple.triangulate(a, b, c), 19.62778642)
        self.assertRaises(TypeError, algebra.Tuple.triangulate, a, b, d)


class VectorTest(unittest.TestCase):

    def testInit(self):
        a = algebra.Tuple(1, 0, 0)
        b = algebra.Tuple(1e3, 1, 0)
        c = algebra.Tuple(0, 3+4j, 1)

        u = algebra.Vector(a)
        v = algebra.Vector(begin=b, end=c)
        w = algebra.Vector(2, 2e3, 4+2j)

        self.assertRaises(avmath.ArgumentError, algebra.Vector.__init__, 1, "e", 0)

    def testPow(self):
        a = algebra.Vector(2, 4, 3)
        b = algebra.Vector(58, 116, 87)

        self.assertEqual(a ** 0, a.unit())
        self.assertEqual(a**1, a)
        self.assertEqual(a**2, 29)
        self.assertEqual(a**3, b)


if __name__ == "__main__":
    unittest.main()