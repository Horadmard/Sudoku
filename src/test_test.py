import random
import math
import pandas as pn
import random as rand
# import random as rand

# Difficulty must be aded
def importData() -> list:
    df = pn.read_csv('docs/sample.csv')

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

# print(importData())



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


def solve(*, sudoku, initial_temp=1000.0, cooling_rate=0.995, min_temp=0.1) -> list:

    T = initial_temp
    cur_solution = generate_initial_solution(org_sudoku=sudoku)
    cur_energy = cost_func(sudoku=cur_solution)

    while T > min_temp and cur_energy > 0:

        new_solution = generate_new_solution(org_sudoku=sudoku, cur_sudoku=cur_solution)
        
        new_energy = cost_func(sudoku=new_solution)
      
        cur_energy = cost_func(sudoku=cur_solution)

        delta_energy = new_energy - cur_energy
        
        if delta_energy < 0 or random.uniform(0, 1) < math.exp(-delta_energy / T):
            cur_solution = new_solution
            cur_energy = new_energy
  
        T = T * cooling_rate
    

    return cur_solution


ans = solve(sudoku=importData())
for row in ans:
    print(ans)