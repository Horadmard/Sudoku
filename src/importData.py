

import pandas
import random


def importData_csv(csvpath) -> list:
    
    df = pandas.read_csv(csvpath)

    index = random.randint(0, 9)
    random_row = df['Puzzle'][index]
    random_row = random_row.replace('.', '0')

    print(f"Difficulty: {df['Difficulty'][index]}")

    numbers = [int(x) for x in random_row]
    sudoku = [numbers[i * 9:(i + 1) * 9] for i in range(9)]

    return sudoku


def importInput():

    row = input()
    numbers = [int(x) for x in row]
    sudoku = [numbers[i * 9:(i + 1) * 9] for i in range(9)]

    return sudoku