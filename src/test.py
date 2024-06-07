import random as rand
import math
from initial import *
from data import importData
from new_solutions import new_solution_maker



sudoku = importData()
cur_sudoku = initial_solution(org_sudoku=sudoku)

for row in cur_sudoku:
    print(row)

print('---------------------------------')

cur_sudoku = new_solution_maker(org_sudoku=sudoku, cur_sudoku=cur_sudoku)


for row in cur_sudoku:
    print(row)