"""test_generate.py
"""

import unittest
import code.app as app
from code.matrix import Matrix


class TestGeneration(unittest.TestCase):
    def test_type(self):
        m = Matrix(0)
        expected = Matrix
        self.assertIsInstance(m, expected, f"type should be {expected}")


    def test_single_dimension(self):
        m = Matrix(1)
        expected = 1
        current = len(m)
        self.assertEqual(current, expected, f"length should be {expected}")

    def test_two_dimensions(self):
        m = Matrix(2)
        expected = 4
        current = len(m)
        self.assertEqual(current, expected, f"length should be {expected}")


if __name__ == "__main__":
    unittest.main()
