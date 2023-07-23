"""test_matrix.py
Ejecuta los tests unitarios para la clase Matrix
"""

import unittest
from code.matrix import Matrix


class TestMatrixFunctionality(unittest.TestCase):
    def setUp(self) -> None:
        self.test_matrix = Matrix(2)
        self.test_matrix.matrix = [[1, 2], [3, 4]]

    def test_empty_matrix_should_return_length_zero(self):
        """len is 0 for empty matrix"""
        m = Matrix(0)
        expected = 0
        current = len(m)
        self.assertEqual(current, expected, f"length should be {expected}")

    def test_multiple_length_of_matrices(self):
        """len is n*n for n-dimension matrix"""
        for dim in range(1, 7):
            m = Matrix(dim)
            expected = dim * dim
            current = len(m)
            self.assertEqual(current, expected, f"length should be {expected}")

    def test_sum_of_all_rows_property(self):
        """test sum_all_rows property"""
        expected = 10
        current = self.test_matrix.sum_all_rows
        self.assertIsInstance(current, int)
        self.assertEqual(current, expected, f"sum should be {expected}")

    def test_sum_of_all_columns_property(self):
        """test sum_all_columns property"""
        expected = 10
        current = self.test_matrix.sum_all_columns
        self.assertIsInstance(current, int)
        self.assertEqual(current, expected, f"sum should be {expected}")

    def test_sum_rows_property(self):
        """test sum_rows property"""
        expected = 3
        current = self.test_matrix.sum_row(1)
        self.assertIsInstance(current, int)
        self.assertEqual(current, expected, f"sum should be {expected}")
        expected = 7
        current = self.test_matrix.sum_row(2)
        self.assertEqual(current, expected, f"sum should be {expected}")

    def test_sum_columns_property(self):
        """test sum_columns property"""
        expected = 4
        current = self.test_matrix.sum_col(1)
        self.assertIsInstance(current, int)
        self.assertEqual(current, expected, f"sum should be {expected}")
        expected = 6
        current = self.test_matrix.sum_col(2)
        self.assertEqual(current, expected, f"sum should be {expected}")


class TestMatrixIntegration(unittest.TestCase):
    def setUp(self) -> None:
        self.test_matrix = Matrix(5)

    def test_object_should_return_type_matrix(self):
        """m is instance of Matrix"""
        m = Matrix(0)
        expected = Matrix
        self.assertIsInstance(m, expected, f"type should be {expected}")
        self.assertIsInstance(self.test_matrix, Matrix, f"type should be {expected}")

    def test_sum_of_a_single_row(self):
        """test sum_row method"""
        row = 1
        expected = sum(self.test_matrix.matrix[row - 1])
        current = self.test_matrix.sum_row(row)
        self.assertEqual(
            current, expected, f"the sum of row {row} should be {expected}"
        )

    def test_sum_of_a_single_col(self):
        col = 1
        expected = sum(
            [
                self.test_matrix.matrix[row][col - 1]
                for row in range(self.test_matrix.dim)
            ]
        )
        current = self.test_matrix.sum_col(col)
        self.assertEqual(
            current, expected, f"the sum of col {col} should be {expected}"
        )

    def test_non_integer_dimension_throws_typeerror(self):
        with self.assertRaises(TypeError):
            Matrix("a")


if __name__ == "__main__":
    unittest.main()
