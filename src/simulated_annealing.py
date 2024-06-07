import random as rand
import math
from initial import *
from data import importData
from new_solutions import new_solution

def solve(*, T, crate, org_sudoku, initial_solution, iter):

    cur_solution = initial_solution(org_sudoku=org_sudoku)

    while T > .1 or cost_func(cur_solution) > 0:

        new_solution = new_solution()

        delta_energy = cost_func(new_solution) - cost_func(cur_solution)

        if delta_energy < 0 or rand.uniform(0, 1) < math.exp(-delta_energy / T):
            cur_solution = new_solution
        
        T *= crate
    

    return cur_solution


if __name__ == "__main__":

    inital_temp = 1000
    cooling_rate = .99
    iteration = 100

    sudoku = importData()

    print(solve(T=inital_temp, crate=cooling_rate, iter=iteration, org_sudoku=sudoku))
