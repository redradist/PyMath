import unittest

from pymath.geometry.vector import Vector


class Testing_GeometryVector(unittest.TestCase):
    def setUp(self):
        """Currently nothing to do. Use it for initialization data before test"""
        pass

    def tearDown(self):
        """Currently nothing to do. Use it for reinitialization data after test"""
        pass

    def test__GeometryVector2_Mult_GeometryVector2__Valid(self):
        vec0 = Vector(0, 1)
        vec1 = Vector(1, 2)
        result = vec0 * vec1
        self.assertEqual(result, Vector(0, 2))

    def test__GeometryVector3_Mult_GeometryVector3__Valid(self):
        vec0 = Vector(0, 1, 2)
        vec1 = Vector(1, 2, 2)
        result = vec0 * vec1
        self.assertEqual(result, Vector(0, 2, 4))

    def test__GeometryVector4_Mult_GeometryVector4__Valid(self):
        vec0 = Vector(0, 1, 2, 8)
        vec1 = Vector(1, 2, 2, 8)
        result = vec0 * vec1
        self.assertEqual(result, Vector(0, 2, 4, 64))

    def test__GeometryVector4_Mult_GeometryVector5__Invalid(self):
        vec0 = Vector(0, 1, 2, 8)
        vec1 = Vector(1, 2, 2, 8, 14)
        with self.assertRaises(ValueError) as context:
            result = vec0 * vec1

    def test__GeometryVector5_Mult_GeometryVector4__Invalid(self):
        vec0 = Vector(0, 1, 2, 8, 14)
        vec1 = Vector(1, 2, 2, 8)
        with self.assertRaises(ValueError) as context:
            result = vec0 * vec1