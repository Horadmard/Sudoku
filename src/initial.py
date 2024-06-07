import random as rand
# import numpy as np

def value_of_location(*, sudoku: list, block_index: list) -> list:


    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


    block_row, block_col = block_index

    for row in range(3):
        for col in range(3):
            
            actual_row = block_row * 3 + row
            actual_col = block_col * 3 + col
            number = matrix[actual_row][actual_col]
            if number in numbers:
                numbers.remove(number)

    return numbers



def random_generate(*, org_sudoku: list) -> list:

    initial_sudoku = org_sudoku

    for block_row in range(3):
        for block_col in range(3):
            values = value_of_location(sudoku=org_sudoku, block_index=[block_row, block_col])

            for row in range(3):
                for col in range(3):
                    if len(values):

                        actual_row = block_row * 3 + row
                        actual_col = block_col * 3 + col
                        
                        if initial_sudoku[actual_row][actual_col] == 0:

                            index = rand.randint(0, len(values) - 1)
                            num = values[index]
                            values.remove(values[index])

                            initial_sudoku[actual_row][actual_col] = num
                        

                        
                    else:
                        pass
    

    return initial_sudoku



def cost_func(*, sudoku: list):

    cost = 0

    for row in range(9):
        for item in range(1, 9):

            num = sudoku[row].count(item)
            if num:
                cost += num - 1


    for row in range(9):
        for item in range(1, 9):

            num = sudoku.T[row].count(item)
            if num:
                cost += num - 1


    return cost



# Sample 9x9 matrix (Sudoku grid)
matrix = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

mat = random_generate(org_sudoku=matrix)

for row in mat:
    print(row)


