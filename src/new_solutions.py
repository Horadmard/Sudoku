
import random as rand



def new_solution_maker(*, org_sudoku: list, cur_sudoku: list) -> list:

    new_sudoku = cur_sudoku

    block_row, block_col = rand.randint(0, 2), rand.randint(0, 2)
    block_row_new, block_col_new = rand.randint(0, 2), rand.randint(0, 2)

    element_row, element_col = rand.randint(0, 2), rand.randint(0, 2)
    element_row_new, element_col_new = rand.randint(0, 2), rand.randint(0, 2)

    actual_row = block_row * 3 + element_row
    actual_col = block_col * 3 + element_col

    actual_row_new = block_row_new * 3 + element_row_new
    actual_col_new = block_col_new * 3 + element_col_new

    while org_sudoku[actual_row][actual_col] == 0 and org_sudoku[actual_row_new][actual_col_new] == 0:
        block_row, block_col = rand.randint(0, 2), rand.randint(0, 2)
        block_row_new, block_col_new = rand.randint(0, 2), rand.randint(0, 2)

        element_row, element_col = rand.randint(0, 2), rand.randint(0, 2)
        element_row_new, element_col_new = rand.randint(0, 2), rand.randint(0, 2)

        actual_row = block_row * 3 + element_row
        actual_col = block_col * 3 + element_col

        actual_row_new = block_row_new * 3 + element_row_new
        actual_col_new = block_col_new * 3 + element_col_new

    new_sudoku[actual_row][actual_col] = cur_sudoku[actual_row_new][actual_col_new]
    new_sudoku[actual_row_new][actual_col_new] = cur_sudoku[actual_row][actual_col]

    return new_sudoku