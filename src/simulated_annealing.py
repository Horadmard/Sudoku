
from initial import *
from data import importData
from new_solutions import new_solution

def solve(*, T, crate, org_sudoku, initial_solution, iter):

    cur_solution = initial_solution(org_sudoku=org_sudoku)

    while iter > 0 or cost_func(sudoku=cur_solution) != 0:

        new_sol = new_solution()

        if delta_energy < 0 or random.uniform(0, 1) < math.exp(-delta_energy / temp):
            cur_sol = new_sol
        
        T *= crate
    

    pass


if __name__ == "__main__":

    inital_temp = 1000
    cooling_rate = .99
    iteration = 100

    sudoku = importData()

    solve(T=inital_temp, crate=cooling_rate, iter=iteration, org_sudoku=sudoku)
