"""app.py
Código de ejemplo para probar la funcionalidad de la clase Matrix.
"""

from matrix import Matrix


def print_matrix(m: Matrix):
    print(f"representación de una matriz de {n}x{n}")
    print(repr(m))


def print_given_row(m: Matrix, row: int = 1):
    print(f"suma de la fila {row}:", m.sum_row(row))


def print_given_column(m: Matrix, col: int):
    print(f"suma de la columna {col}:", m.sum_col(col))


def print_sum_all_rows(m: Matrix):
    print(f"suma de los elementos de todas las filas: {m.sum_all_rows}")


def print_sum_all_columns(m: Matrix):
    print(f"suma de los elementos de todas las columnas: {m.sum_all_columns}")


def print_list_of_sums_all_rows(m: Matrix):
    print(f"lista de sumas por filas: {m.sum_rows}")


def print_list_of_sums_all_columns(m: Matrix):
    print(f"lista de sumas por columnas: {m.sum_columns}")


def get_matrix_dimension_from_user() -> int:
    try:
        dim = input("Introduce la dimensión de la matriz (sólo enteros): ")
        assert isinstance(int(dim), int)
        assert type(int(dim)) == int
        return int(dim)
    except (ValueError, TypeError):
        print("Por favor, introduce sólo números enteros")


if __name__ == "__main__":
    n = get_matrix_dimension_from_user()
    # 1. Generar la matriz
    # 2. Rellena la matriz con números aleatorios
    # 4. Calcula las sumas de las filas y columnas
    m = Matrix(n)

    # 3. Imprime la matriz utilizando el método incorporado __repr__
    print_matrix(m)

    # 4. Imprime las sumas de filas o columnas dadas
    row = 2
    print_given_row(m, row)

    col = 3
    print_given_column(m, col)

    # Imprime las sumas de todos los elementos de las filas y de todas los elementos de las columnas
    print()
    print_sum_all_rows(m)
    print_sum_all_columns(m)

    # 5. Imprime las listas de las sumas de todas las filas y todas las columnas
    print()
    print_list_of_sums_all_rows(m)
    print_list_of_sums_all_columns(m)
