
import copy


def fitness(sudoku2: list):
    cost = 0
    sudoku = copy.deepcopy(sudoku2)
    for row in range(9):
        for item in range(1, 10):

            num = sudoku[row].count(item)

            if num > 1:
                cost += num - 1


    tra = [[sudoku[j][i] for j in range(len(sudoku))] for i in range(len(sudoku[0]))]

    for row in range(9):
        for item in range(1, 10):

            num = tra[row].count(item)

            if num > 1:
                cost += num - 1

    return cost
    