"""test_matrix.py
Ejecuta los tests unitarios para la clase Matrix
"""

import unittest
from code.matrix import Matrix


class TestGeneration(unittest.TestCase):
    def setUp(self) -> None:
        self.test_matrix = Matrix(2)
        self.test_matrix.matrix = [[1, 2], [3, 4]]

    def test_type(self):
        """m is instance of Matrix"""
        m = Matrix(0)
        expected = Matrix
        self.assertIsInstance(m, expected, f"type should be {expected}")

    def test_empty_matrix(self):
        """len is 0 for empty matrix"""
        m = Matrix(0)
        expected = 0
        current = len(m)
        self.assertEqual(current, expected, f"length should be {expected}")

    def test_matrix_dimension(self):
        """len is n*n for n-dimension matrix"""
        for dim in range(1, 7):
            m = Matrix(dim)
            expected = dim * dim
            current = len(m)
            self.assertEqual(current, expected, f"length should be {expected}")

    def test_sum_rows(self):
        """test sum_rows"""
        expected = 3
        current = self.test_matrix.sum_row(1)
        self.assertEqual(current, expected, f"sum should be {expected}")
        expected = 7
        current = self.test_matrix.sum_row(2)
        self.assertEqual(current, expected, f"sum should be {expected}")

    def test_sum_columns(self):
        """test sum_columns"""
        expected = 4
        current = self.test_matrix.sum_col(1)
        self.assertEqual(current, expected, f"sum should be {expected}")
        expected = 6
        current = self.test_matrix.sum_col(2)
        self.assertEqual(current, expected, f"sum should be {expected}")


if __name__ == "__main__":
    unittest.main()
