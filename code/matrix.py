"""matrix.py
"""

from random import randint


class Matrix:
    def __init__(self, dim: int) -> None:
        self._dim = dim  # matrix dimension
        self._matrix = [[randint(0, 9) for i in range(dim)] for j in range(dim)]

    @property
    def matrix(self) -> list:
        return list(self._matrix)

    @matrix.setter
    def matrix(self, matrix: list):
        self._matrix = matrix

    def __len__(self) -> int:
        return sum([len(line) for line in self._matrix])

    def __str__(self) -> str:
        """Return a reader-friendly string representation of our matrix"""
        return f"{self.__class__.__name__}"

    def __repr__(self) -> str:
        """Return a reader-friendly string representation of the object"""
        return f"{self.__name__}"
