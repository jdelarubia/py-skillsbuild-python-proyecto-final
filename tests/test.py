"""test_generate.py
"""

import unittest
import code.app as app
from code.matrix import Matrix


class TestGeneration(unittest.TestCase):
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

    def test_two_dimensions(self):
        m = Matrix(2)
        expected = 4
        current = len(m)
        self.assertEqual(current, expected, f"length should be {expected}")


if __name__ == "__main__":
    unittest.main()
