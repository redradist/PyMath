import unittest

from pymath.algebra.linear.vector import Vector, VectorT


class Testing_LinearVector(unittest.TestCase):
    def setUp(self):
        """Currently nothing to do. Use it for initialization data before test"""
        pass

    def tearDown(self):
        """Currently nothing to do. Use it for reinitialization data after test"""
        pass

    def test__LinearVector2_Mult_LinearVectorT2__Valid(self):
        vec0 = Vector(0, 1)
        vec1 = VectorT(1, 2)
        result = vec0 * vec1
        self.assertEqual(result, 2)

    def test__LinearVector3_Mult_LinearVectorT3__Valid(self):
        vec0 = Vector(0, 1, 9)
        vec1 = VectorT(1, 2, 8)
        result = vec0 * vec1
        self.assertEqual(result, 74)

    def test__LinearVector2_Mult_LinearVector2__Invalid(self):
        vec0 = Vector(0, 1)
        vec1 = Vector(1, 2)
        with self.assertRaises(ValueError) as context:
            result = vec0 * vec1

    def test__LinearVector3_Mult_LinearVector3__Invalid(self):
        vec0 = Vector(0, 1, 4)
        vec1 = Vector(1, 2, 8)
        with self.assertRaises(ValueError) as context:
            result = vec0 * vec1

    def test__LinearVector4_Mult_LinearVector4__Invalid(self):
        vec0 = Vector(2, 1, 4, 1)
        vec1 = Vector(1, 2, 8, 10)
        with self.assertRaises(ValueError) as context:
            result = vec0 * vec1