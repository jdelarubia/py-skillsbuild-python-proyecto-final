"""matrix.py
"""

from random import randint


class Matrix:
    def __init__(self, dim: int) -> None:
        self._dim = dim  # matrix dimension
        self._matrix = [[randint(0, 9) for i in range(dim)] for j in range(dim)]
        self._sum_rows = [self.sum_row(row + 1) for row in range(dim)]
    @property
    def sum_rows(self) -> int:
        return sum(self._sum_rows)


    @property
    def matrix(self) -> list:
        return list(self._matrix)

    @matrix.setter
    def matrix(self, matrix: list):
        self._matrix = matrix

    def sum_row(self, row: int) -> int:
        """Return the sum of a given row number.

        Args:
            row (int): row number between 1 and self._dim

        Returns:
            int: sum of the elements of a row
        """
        assert row in range(1, self._dim + 1), f"row has to be < {self._dim}"
        return sum(self._matrix[row - 1])

    def sum_col(self, col: int) -> int:
        """Return the sum of a given column number.

        Args:
            col (int): column number between 1 and self._dim
        Returns:
            int: sum of the elements of a column
        """
        assert col in range(1, self._dim + 1), f"row has to be < {self._dim}"
        return sum([self._matrix[row][col - 1] for row in range(self._dim)])

    def __len__(self) -> int:
        return sum([len(line) for line in self._matrix])

    def __str__(self) -> str:
        """Return a reader-friendly string representation of our matrix"""
        return f"{self.__class__.__name__}"

    def __repr__(self) -> str:
        """Return a reader-friendly string representation of the object"""
        s = ""
        for row in range(self._dim):
            s += (
                "".join(f"{self._matrix[row][col]:<2d}" for col in range(self._dim))
                + "\n"
            )
        return s
