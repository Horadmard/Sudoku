from data import importData
from values_of_location import value_of_location

def the_fullest_location(*, sudoku: list) -> list:
    tfl = []
    tfl_len = 0


    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0 and len(value_of_location(sudoku=sudoku, location=[i, j])) > tfl_len: # ;)
                tfl = [i, j]
                tfl_len = len(value_of_location(sudoku=sudoku, location=tfl))


    print(value_of_location(sudoku=sudoku, location=tfl))
    # print(tfl_len)
    if tfl == []:
        return None
    return tfl


# if __name__ == "__main__":
#     sudoku = [[0, 0, 0, 0, 0, 0, 0, 8, 0],
#               [0, 6, 0, 0, 0, 4, 0, 0, 0],
#               [0, 0, 1, 0, 0, 0, 9, 0, 0],
#               [2, 1, 0, 0, 8, 0, 0, 0, 0],
#               [0, 0, 0, 0, 1, 7, 0, 0, 6],
#               [0, 0, 3, 0, 0, 0, 4, 0, 0],
#               [0, 0, 0, 0, 9, 0, 0, 0, 0],
#               [7, 0, 8, 0, 0, 0, 0, 2, 0],
#               [4, 0, 9, 6, 0, 0, 7, 0, 0]]

#     sudoku = importData()
#     print(the_fullest_location(sudoku=sudoku))