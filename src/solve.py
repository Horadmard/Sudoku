
from timeit import default_timer as timer
from datetime import timedelta

from cost_function import fitness
from importData import importData_csv
from simulated_anealing import simulated_anealing



start = timer()
sudoku = importData_csv('samples/Any.csv')
for row in sudoku:
    print(row)

print()

solved = simulated_anealing(sudoku)
for row in solved:
    print(row)

print()
print(fitness(solved))

end = timer()
print(timedelta(seconds=end-start))


# for max_iteration in range(500, 1500, 500):
#         for max_temp in range(50, 200, 50):
#             for n in range(1000, 10000, 3000):
#                 solved = simulated_anealing(sudoku, max_iteration, max_temp, n)
#                 for row in solved:
#                     print(row)

#                 print()
#                 print(fitness(solved))