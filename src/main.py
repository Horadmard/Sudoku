

import math
import copy

import pandas
import random


def simulated_anealing(sudoku):


    max_temp = 200
    min_temp = .4
    T = max_temp

    max_iteration = 2500
    iteration = 0
    n = 100000

    # cooling_rate = .95

    # b = (max_temp-min_temp)/(max_iteration*max_temp*min_temp)

    empty_cells = empty(sudoku)
    cur_solution = fill_missing_numbers(sudoku)
    cur_energy = cost_func(cur_solution)



    while T > min_temp and cur_energy > 0 and iteration <= max_iteration:

        new_solution = generate_new_solution(empty_cells, cur_solution)
        new_energy = cost_func(new_solution)

        for i in range(n-1):
            temp_solution = generate_new_solution(empty_cells, cur_solution)
            temp_energy = cost_func(temp_solution)
            delta_energy = temp_energy - cur_energy
            
            if (random.uniform(0, 1) < math.exp(-delta_energy / T)):
                # (temp_energy < cur_energy) or 
                cur_solution = temp_solution
                cur_energy = temp_energy
                break
            
        # delta_energy = new_energy - cur_energy

        # if delta_energy <= 0 or random.uniform(0, 1) < math.exp(-delta_energy / T):
        #     cur_solution = new_solution
        #     cur_energy = new_energy

        print(f'Iteration: {iteration}')
        print(f'Temp: {T}')
        print(f'Cost: {cur_energy}')
        
        # T *= cooling_rate**iteration
        # T /= 1 + b*T
        T = (max_iteration - iteration) ** 5 / max_iteration ** 5 * (max_temp - min_temp) + min_temp
        iteration += 1



    return cur_solution


def importData() -> list:
    
    df = pandas.read_csv('sample/Any.csv')

    index = random.randint(0, 9)
    random_row = df['Puzzle'][index]
    random_row = random_row.replace('.', '0')

    print(f"Difficulty: {df['Difficulty'][index]}")

    numbers = [int(x) for x in random_row]
    sudoku = [numbers[i * 9:(i + 1) * 9] for i in range(9)]

    return sudoku



def fill_missing_numbers(sudoku):
    sudoku_2 = copy.deepcopy(sudoku)
    for block_row in range(0, 9, 3):
        for block_col in range(0, 9, 3):
            fill_block(sudoku_2, block_row, block_col)
    return sudoku_2


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


def empty(sudoku):
    empty_cells = []
    for block_row in range(0, 9, 3):
        for block_col in range(0, 9, 3):
            block_empty = []
            for r in range(block_row, block_row + 3):
                for c in range(block_col, block_col + 3):
                    if sudoku[r][c] == 0:
                        block_empty.append((r, c))
            empty_cells.append(block_empty)

    return empty_cells


def generate_new_solution(empty_cells, sudoku) -> list:

    new_sudoku = copy.deepcopy(sudoku)
    choice = random.randint(0,8)

    block = empty_cells[choice]
    item1, item2 = random.sample(block, 2)
    new_sudoku[item1[0]][item1[1]], new_sudoku[item2[0]][item2[1]] = sudoku[item2[0]][item2[1]], sudoku[item1[0]][item1[1]]

    return new_sudoku


def cost_func(sudoku2: list):
    cost = 0
    sudoku = copy.deepcopy(sudoku2)
    for row in range(9):
        for item in range(1, 10):

            num = sudoku[row].count(item)

            if num > 1:
                cost += num - 1


    tra = [[sudoku[j][i] for j in range(len(sudoku))] for i in range(len(sudoku[0]))]

    for row in range(9):
        for item in range(1, 10):

            num = tra[row].count(item)

            if num > 1:
                cost += num - 1

    return cost
        

sudoku = importData()
for row in sudoku:
    print(row)

print()

solved = simulated_anealing(sudoku)
for row in solved:
    print(row)

print()
print(cost_func(solved))