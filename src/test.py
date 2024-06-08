import random as rand
import math
from initial import *
from data import importData
from new_solutions import new_solution_maker



# sudoku = importData()
# cur_sudoku = initial_solution(org_sudoku=sudoku)

# for row in cur_sudoku:
#     print(row)

# print('---------------------------------')

# cur_sudoku = new_solution_maker(org_sudoku=sudoku, cur_sudoku=cur_sudoku)


# for row in cur_sudoku:
#     print(row)




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

cur = [
    [5, 3, 1, 8, 7, 3, 1, 4, 9], #2
    [6, 4, 7, 1, 9, 5, 2, 8, 7], #1
    [2, 9, 8, 4, 2, 6, 3, 6, 5], #2
    [8, 3, 1, 1, 6, 4, 8, 4, 3], #4
    [4, 9, 2, 8, 5, 3, 2, 9, 1], #2
    [7, 6, 5, 9, 2, 7, 5, 7, 6],
    [4, 6, 8, 5, 7, 6, 2, 8, 1],
    [2, 5, 3, 4, 1, 9, 4, 6, 5],
    [7, 9, 1, 3, 8, 2, 3, 7, 9]

]


# cur = initial_solution(org_sudoku=matrix)


mat = new_solution_maker(org_sudoku=matrix, cur_sudoku=cur)

for row in mat:
    print(row)

# print(cost_func(sudoku = cur))
