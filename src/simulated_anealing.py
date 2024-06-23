

import math
import random

from cost_function import fitness
from functions import empty, fill_missing_numbers
from generator import generate_new_solution


def simulated_anealing(sudoku):
    max_iteration = 1000
    iteration = 0

    max_temp = 40
    min_temp = .01
    T = max_temp

    n = 1000


    # file_name = f'data_plot_{max_iteration}_{max_temp}_{n}.csv'

    # with open(file_name, 'w') as f:
    #     f.write('Iteration,Temp,Cost\n')

    # cooling_rate = .95

    # b = (max_temp-min_temp)/(max_iteration*max_temp*min_temp)

    empty_cells = empty(sudoku)
    cur_solution = fill_missing_numbers(sudoku)
    cur_energy = fitness(cur_solution)



    while T > min_temp and cur_energy > 0 and iteration <= max_iteration:

        new_solution = generate_new_solution(empty_cells, cur_solution)
        new_energy = fitness(new_solution)

        for i in range(n-1):
            new_solution = generate_new_solution(empty_cells, cur_solution)
            new_energy = fitness(new_solution)
            delta_energy = new_energy - cur_energy
            
            if new_energy < cur_energy or random.uniform(0, 1) < math.exp(-delta_energy / T):

                cur_solution = new_solution
                cur_energy = new_energy
                break
            
        # delta_energy = new_energy - cur_energy

        # if delta_energy <= 0 or random.uniform(0, 1) < math.exp(-delta_energy / T):
        #     cur_solution = new_solution
        #     cur_energy = new_energy

        print(f'Iteration: {iteration}')
        print(f'Temp: {T}')
        print(f'Cost: {cur_energy}')

        # with open(file_name, 'a') as f:
        #     f.write(f'{iteration},{T},{cur_energy}\n')
        
        # T *= cooling_rate**iteration
        # T /= 1 + b*T
        T = (max_iteration - iteration) ** 5 / max_iteration ** 5 * (max_temp - min_temp) + min_temp
        iteration += 1

        # if T < min_temp + .01 and cur_energy != 0:
        #     T += 1



    return cur_solution
