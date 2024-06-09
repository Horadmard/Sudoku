

import random as rand
import copy


def value_of_location(*, sudoku: list, block_index: list) -> list:


    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


    block_row, block_col = block_index

    for row in range(3):
        for col in range(3):
            
            actual_row = block_row * 3 + row
            actual_col = block_col * 3 + col

            number = sudoku[actual_row][actual_col]

            if number in numbers:
                numbers.remove(number)

    return numbers



def generate_initial_solution(*, org_sudoku: list) -> list:

    initial_sudoku = copy.deepcopy(org_sudoku)

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
            # print(item , '-', num)
            
            if num:
                cost += num - 1

    
    tra = [[sudoku[j][i] for j in range(len(sudoku))] for i in range(len(sudoku[0]))]


    for row in range(9):
        for item in range(1, 9):

            num = tra[row].count(item)
            
            if num:
                cost += num - 1


    return cost



