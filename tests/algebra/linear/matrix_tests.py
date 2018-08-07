import unittest

from pymath.algebra.linear.matrix import Matrix


class Testing_LinearMatrix(unittest.TestCase):
    def setUp(self):
        """Currently nothing to do. Use it for initialization data before test"""
        pass

    def tearDown(self):
        """Currently nothing to do. Use it for reinitialization data after test"""
        pass

    def test__LinearMatrix2x2_Add_Matrix2x2__Valid(self):
        mat0 = Matrix(2, 2, [1, 1,
                             1, 1])
        mat1 = Matrix(2, 2, [1, 1,
                             1, 1])
        result = mat0 + mat1
        self.assertEqual(result, Matrix(2, 2, [2, 2,
                                               2, 2]))

    def test__LinearMatrix2x2_Sub_Matrix2x2__Valid(self):
        mat0 = Matrix(2, 2, [1, 1,
                             1, 1])
        mat1 = Matrix(2, 2, [1, 1,
                             1, 1])
        result = mat0 - mat1
        self.assertEqual(result, Matrix(2, 2, [0, 0,
                                               0, 0]))

    def test__LinearMatrix2x2_Mult_Matrix2x2__Valid(self):
        mat0 = Matrix(2, 2, [1, 1,
                             1, 1])
        mat1 = Matrix(2, 2, [1, 1,
                             1, 1])
        result = mat0 * mat1
        self.assertEqual(result, Matrix(2, 2, [2, 2,
                                               2, 2]))

    def test__LinearMatrix2x3_Mult_Matrix3x2__Valid(self):
        mat0 = Matrix(2, 3, [1, 1, 2,
                             1, 1, 3])
        mat1 = Matrix(3, 2, [1, 1,
                             1, 1,
                             2, 5])
        result = mat0 * mat1
        self.assertEqual(result, Matrix(2, 2, [6, 12,
                                               8, 17]))

    def test__LinearMatrix3x3_Mult_Matrix2x3__Invalid(self):
        mat0 = Matrix(3, 3, [1, 1, 4,
                             1, 1, 4,
                             2, 5, 4])
        mat1 = Matrix(2, 3, [1, 1, 2,
                             1, 1, 3])
        with self.assertRaises(ValueError) as context:
            result = mat0 * mat1
