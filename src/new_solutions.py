
import random as rand



def generate_new_solution(*, org_sudoku: list, cur_sudoku: list) -> list:

    new_solution = cur_sudoku

    block_row, block_col = rand.randint(0, 2), rand.randint(0, 2)

    element_row_one, element_col_one = rand.randint(0, 2), rand.randint(0, 2)
    element_row_two, element_col_two = rand.randint(0, 2), rand.randint(0, 2)

    while element_row_one == element_row_two and element_col_one == element_col_two:
        
        block_row, block_col = rand.randint(0, 2), rand.randint(0, 2)

        element_row_one, element_col_one = rand.randint(0, 2), rand.randint(0, 2)
        element_row_two, element_col_two = rand.randint(0, 2), rand.randint(0, 2)

    actual_row_one = block_row * 3 + element_row_one
    actual_col_one = block_col * 3 + element_col_one

    actual_row_two = block_row * 3 + element_row_two
    actual_col_two = block_col * 3 + element_col_two


    while org_sudoku[actual_row_one][actual_col_one] != 0 or org_sudoku[actual_row_two][actual_col_two] != 0:

        block_row, block_col = rand.randint(0, 2), rand.randint(0, 2)

        element_row_one, element_col_one = rand.randint(0, 2), rand.randint(0, 2)
        element_row_two, element_col_two = rand.randint(0, 2), rand.randint(0, 2)

        while element_row_one == element_row_two and element_col_one == element_col_two:
            
            block_row, block_col = rand.randint(0, 2), rand.randint(0, 2)

            element_row_one, element_col_one = rand.randint(0, 2), rand.randint(0, 2)
            element_row_two, element_col_two = rand.randint(0, 2), rand.randint(0, 2)

        actual_row_one = block_row * 3 + element_row_one
        actual_col_one = block_col * 3 + element_col_one

        actual_row_two = block_row * 3 + element_row_two
        actual_col_two = block_col * 3 + element_col_two

    print(actual_row_one, actual_col_one)
    print(actual_row_two, actual_col_two)
    
    a = cur_sudoku[actual_row_two][actual_col_two]
    b = cur_sudoku[actual_row_one][actual_col_one]

    new_solution[actual_row_one][actual_col_one] = a
    new_solution[actual_row_two][actual_col_two] = b



    return new_solution


# ------------------------------------------------------------------


def generate_new_solution_rec(*, org_sudoku: list, cur_sudoku: list) -> list:

    new_sudoku = cur_sudoku

    block_row, block_col = rand.randint(0, 2), rand.randint(0, 2)

    element_row, element_col = rand.randint(0, 2), rand.randint(0, 2)
    element_row_new, element_col_new = rand.randint(0, 2), rand.randint(0, 2)

    # print(block_row, block_col)
    # print(element_row, '-',element_col)
    # print(element_row_new, '-',element_col_new)


    if element_row == element_row_new and element_col == element_col_new:
        return generate_new_solution_rec(org_sudoku=org_sudoku, cur_sudoku=cur_sudoku)
    

    actual_row = block_row * 3 + element_row
    actual_col = block_col * 3 + element_col

    actual_row_new = block_row * 3 + element_row_new
    actual_col_new = block_col * 3 + element_col_new
    
    if org_sudoku[actual_row][actual_col] != 0 or org_sudoku[actual_row_new][actual_col_new] != 0:
        return generate_new_solution_rec(org_sudoku=org_sudoku, cur_sudoku=cur_sudoku)
    
    a = cur_sudoku[actual_row_new][actual_col_new]
    b = cur_sudoku[actual_row][actual_col]

    new_sudoku[actual_row][actual_col] = a
    new_sudoku[actual_row_new][actual_col_new] = b
    

    
    return new_sudoku
