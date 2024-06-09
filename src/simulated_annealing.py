import random as rand
import math
from initial import *
from data import importData
from new_solutions import generate_new_solution



def solve(*, sudoku, initial_temp=1000.0, cooling_rate=0.995, min_temp=0.1) -> list:

    T = initial_temp
    cur_solution = initial_solution(org_sudoku=sudoku)

    while T > min_temp and cost_func(sudoku=cur_solution) > 0:

        new_solution = generate_new_solution(org_sudoku=sudoku, cur_sudoku=cur_solution)

        delta_energy = cost_func(sudoku=new_solution) - cost_func(sudoku=cur_solution)

        if delta_energy < 0 or rand.uniform(0, 1) < math.exp(-delta_energy / T):
            cur_solution = new_solution
        
        T *= cooling_rate
    

    return cur_solution


if __name__ == "__main__":

    sudoku = importData()

    initial_sudoku = initial_solution(org_sudoku=sudoku)

    answer = solve(sudoku=sudoku)

    for row in answer:
        print(row)
