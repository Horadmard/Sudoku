
import random as rand



def new_solution_maker(*, org_sudoku: list, cur_sudoku: list) -> list:

    new_sudoku = cur_sudoku

    block_row, block_col = rand.randint(0, 2), rand.randint(0, 2)

    element_row, element_col = rand.randint(0, 2), rand.randint(0, 2)
    element_row_new, element_col_new = rand.randint(0, 2), rand.randint(0, 2)
    
    # print(block_row, block_col)
    # print(element_row, '-',element_col)
    # print(element_row_new, '-',element_col_new)


    if element_row == element_row_new and element_col == element_col_new:
        return new_solution_maker(org_sudoku=org_sudoku, cur_sudoku=cur_sudoku)
    

    actual_row = block_row * 3 + element_row
    actual_col = block_col * 3 + element_col

    actual_row_new = block_row * 3 + element_row_new
    actual_col_new = block_col * 3 + element_col_new
    
    if org_sudoku[actual_row][actual_col] != 0 or org_sudoku[actual_row_new][actual_col_new] != 0:
        return new_solution_maker(org_sudoku=org_sudoku, cur_sudoku=cur_sudoku)
    
    a = cur_sudoku[actual_row_new][actual_col_new]
    b = cur_sudoku[actual_row][actual_col]

    new_sudoku[actual_row][actual_col] = a
    new_sudoku[actual_row_new][actual_col_new] = b
    

    
    return new_sudoku



