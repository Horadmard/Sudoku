

import random


def fill_missing_numbers(sudoku):
    for block_row in range(0, 9, 3):
        for block_col in range(0, 9, 3):
            fill_block(sudoku, block_row, block_col)

def fill_block(sudoku, block_row, block_col):
    empty_cells = []
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for r in range(block_row, block_row + 3):
        for c in range(block_col, block_col + 3):
            if sudoku[r][c] != 0:
                 numbers.remove(sudoku[r][c])
            else:
                empty_cells.append((r, c))
  
    random.shuffle(numbers)
    for (r, c), number in zip(empty_cells, numbers):
        sudoku[r][c] = number