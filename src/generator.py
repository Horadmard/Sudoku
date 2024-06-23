
import random
import copy

def generate_new_solution(empty_cells, sudoku) -> list:

    new_sudoku = copy.deepcopy(sudoku)
    choice = random.randint(0,8)

    block = empty_cells[choice]
    item1, item2 = random.sample(block, 2)
    new_sudoku[item1[0]][item1[1]], new_sudoku[item2[0]][item2[1]] = sudoku[item2[0]][item2[1]], sudoku[item1[0]][item1[1]]

    return new_sudoku