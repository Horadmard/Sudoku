import pandas as pn
import random as rand

# Difficulty must be aded
def importData() -> list:
    df = pn.read_csv('../docs/sample.csv')

    random_col = df['Puzzle'][rand.randint(0, 19)]
    random_col = random_col.replace('.', '0')

    numbers = [int(x) for x in random_col]
    matrix = [numbers[i * 9:(i + 1) * 9] for i in range(9)]

    # for row in matrix:
    #     print(row)

    return matrix


def number_of_empty_cells(sudoku: list):
    number = 0
    for row in sudoku:
        for cell in row:
            if cell == 0:
                number += 1
    return number
