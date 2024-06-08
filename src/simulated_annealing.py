import random as rand
import math
from initial import *
from data import importData
from new_solutions import new_solution_maker



def solve(*, T, crate, org_sudoku, iter):

    cur_solution = initial_solution(org_sudoku=org_sudoku)

    while iter > 0 and cost_func(sudoku=cur_solution) > 0:

        new_solution = new_solution_maker(org_sudoku=org_sudoku, cur_sudoku=cur_solution)

        delta_energy = cost_func(sudoku=new_solution) - cost_func(sudoku=cur_solution)

        if delta_energy < 0 or rand.uniform(0, 1) < math.exp(-delta_energy / T):
            cur_solution = new_solution
        
        T *= crate

        iter -= 1
    

    return cur_solution


if __name__ == "__main__":

    inital_temp = 1000
    cooling_rate = .99
    iteration = 100

    sudoku = importData()

    initial_sudoku = initial_solution(org_sudoku=sudoku)

    # print(cost_func(sudoku=initial_sudoku))


    answer = solve(T=inital_temp, crate=cooling_rate, iter=iteration, org_sudoku=sudoku)

    for row in answer:
        print(row)
