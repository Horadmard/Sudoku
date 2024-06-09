
from data import *
from initial import *
from new_func import *
from new_solutions import *
from simulated_annealing import *

import math
import random


# if __name__ == "__main__":

#     original = importData()
#     initial = generate_initial_solution(org_sudoku=original)
    # sudoku = generate_new_solution(org_sudoku=original, cur_sudoku=initial)

    # for row in sudoku:
    #     print(row)
    
    # print()

    # for row in initial:
    #     print(row)

    # print()

    # for row in original:
    #     print(row)

# matrix = [

#     [1, 3, 2, 6, 9, 4, 5, 7, 8],
#     [6, 5, 7, 8, 1, 3, 4, 9, 2],
#     [9, 4, 8, 7, 2, 5, 1, 6, 3],
#     [4, 2, 1, 9, 5, 8, 7, 3, 6],
#     [7, 6, 9, 1, 3, 2, 8, 5, 4],
#     [3, 8, 5, 4, 6, 7, 9, 2, 1],
#     [8, 7, 4, 2, 9, 6, 3, 1, 5],
#     [2, 9, 3, 5, 8, 1, 6, 4, 7],
#     [5, 1, 6, 3, 7, 4, 2, 8, 9]


# ]

# print (cost_func(sudoku=matrix))

c = 0

orginal = importData()

mat = copy.deepcopy(orginal)
fill_missing_numbers(mat)

for row in mat:
    print(row)

num = cost_func(sudoku=mat)


