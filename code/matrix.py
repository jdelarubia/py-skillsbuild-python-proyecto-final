"""matrix.py
"""

from random import randint


class Matrix:
    def __init__(self, n: int) -> None:
        self._matrix = [[randint(0, 9) for i in range(n)] for j in range(n)]

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
        # for _ in ...
        return f"{self.__name__}"

    def __repr__(self) -> str:
        """Return a reader-friendly string representation of the object"""
        return f"{self.__name__}"
