
import random
import math


from initial import *
from data import importData
from new_solutions import generate_new_solution



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




if __name__ == "__main__":

    ans = solve(sudoku=importData())

    for row in ans:
        print(ans)
