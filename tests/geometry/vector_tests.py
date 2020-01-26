import unittest

from pymath.geometry.vector import Vector2D


class Testing_GeometryVector(unittest.TestCase):
    def setUp(self):
        """Currently nothing to do. Use it for initialization data before test"""
        pass

    def tearDown(self):
        """Currently nothing to do. Use it for reinitialization data after test"""
        pass

    def test__GeometryVector2_Mult_GeometryVector2__Valid(self):
        vec0 = Vector2D(0, 1)
        vec1 = Vector2D(1, 2)
        result = vec0 * vec1
        self.assertEqual(2, result)

    def test__GeometryVector3_Mult_GeometryVector3__Valid(self):
        vec0 = Vector2D(1, 2)
        vec1 = Vector2D(1, 2)
        result = vec0 * vec1
        self.assertEqual(5, result)

    def test__GeometryVector4_Mult_GeometryVector4__Valid(self):
        vec0 = Vector2D(2, 3)
        vec1 = Vector2D(1, 2)
        result = vec0 * vec1
        self.assertEqual(8, result)

    def test__GeometryVector4_Mult_GeometryVector5__Invalid(self):
        with self.assertRaises(ValueError) as context:
            vec0 = Vector2D(0, 1, 2, 8)
            vec1 = Vector2D(1, 2, 2, 8, 14)

    def test__GeometryVector5_Mult_GeometryVector4__Invalid(self):
        with self.assertRaises(ValueError) as context:
            vec0 = Vector2D(0, 1, 2, 8, 14)
            vec1 = Vector2D(1, 2, 2, 8)