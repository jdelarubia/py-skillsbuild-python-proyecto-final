"""app.py
Sample code to test our Matrix general functionality.
"""

from matrix import Matrix

if __name__ == "__main__":
    m = Matrix(3)

    print("representación de la matriz")
    print(repr(m))

    row = 2
    print(f"suma de la fila {row}:", m.sum_row(row))

    col = 3
    print(f"suma de la columna {col}:", m.sum_col(col))

    print()
    print(f"sumas de todas las filas: {m._sum_rows}")
    print(f"sumas de todas las columnas: {m._sum_columns}")

    print()
    print(f"suma de todas las filas: {m.sum_rows}")
    print(f"suma de todas las columnas: {m.sum_columns}")
