from data import importData
from values_of_location import value_of_location


def the_fullest_location(*, sudoku: list) -> list:
    tfl = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tfl_len = len(tfl)


    for i in range(9):
        for j in range(9):
            curitem_len = len(value_of_location(
                sudoku=sudoku, location=[i, j]))
            if sudoku[i][j] == 0 and curitem_len < tfl_len:  # ;)
                tfl = [i, j]
                tfl_len = curitem_len


    print(value_of_location(sudoku=sudoku, location=tfl))
    # print(tfl_len)
    if tfl == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return None
    return tfl



if __name__ == "__main__":
    sudoku = [[0, 0, 0, 0, 0, 0, 0, 8, 0],
              [0, 6, 0, 0, 0, 4, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 9, 0, 0],
              [2, 1, 0, 0, 8, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 7, 0, 0, 6],
              [0, 0, 3, 0, 0, 0, 4, 0, 0],
              [0, 0, 0, 0, 9, 0, 0, 0, 0],
              [7, 0, 8, 0, 0, 0, 0, 2, 0],
              [4, 0, 9, 6, 0, 0, 7, 0, 0]]

    # sudoku = importData()
    print(the_fullest_location(sudoku=sudoku))
