
import random as rand
import copy

def generate_new_solution(*, org_sudoku: list, cur_sudoku: list) -> list:

    new_solution = copy.deepcopy(cur_sudoku)

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

    # print(actual_row_one, actual_col_one)
    # print(actual_row_two, actual_col_two)
    
    a = cur_sudoku[actual_row_two][actual_col_two]
    b = cur_sudoku[actual_row_one][actual_col_one]

    new_solution[actual_row_one][actual_col_one] = a
    new_solution[actual_row_two][actual_col_two] = b



    return new_solution
