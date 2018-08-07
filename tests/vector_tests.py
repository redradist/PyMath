import unittest

from pymath.linear.algebra.vector import Vector, VectorT


class Testing_LinearVector(unittest.TestCase):
    def setUp(self):
        """Currently nothing to do. Use it for initialization data before test"""
        pass

    def tearDown(self):
        """Currently nothing to do. Use it for reinitialization data after test"""
        pass

    def test__LinearVector2__Valid(self):
        vec0 = Vector(0, 1)
        vec1 = Vector(1, 2)
        result = vec0 * vec1
        self.assertEqual(result, Vector(0, 2))

    def test__LinearVector22__Valid(self):
        vec0 = Vector(0, 1)
        vec1 = VectorT(1, 2)
        result = vec0 * vec1
        self.assertEqual(result, 2)

    def test__LinearVector3__Valid(self):
        vec0 = Vector(0, 1, 4)
        vec1 = Vector(1, 2, 8)
        result = vec0 * vec1
        self.assertEqual(result, Vector(0, 2, 32))

    def test__LinearVector4__Valid(self):
        vec0 = Vector(2, 1, 4, 1)
        vec1 = Vector(1, 2, 8, 10)
        result = vec0 * vec1
        self.assertEqual(result, Vector(2, 2, 32, 10))