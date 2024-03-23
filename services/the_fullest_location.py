from data import importData
from values_of_location import value_of_location


def the_fullest_location(*, sudoku: list) -> list:

    tfl = []
    ltfl = 9

    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0 and len(value_of_location(sudoku=sudoku, location=[i, j])) > ltfl:
                tfl = [i, j]
                ltfl = len(value_of_location(sudoku=sudoku, location=tfl))

    return tfl

    # Find the fullest Block
#     fblock = [0] * 9
#     curblock = []
#     fbi = [0, 0]

#     for i in range(3):
#         for j in range(3):
#             for k in range(3):
#                 for item in sudoku[3*i + k][3*j:3*j + 3]:
#                     curblock.append(item)
#             curblock_info = number_of_zeros(sudoku, curblock, [i, j])
#             if curblock_info[0] < number_of_zeros(sudoku, fblock, fbi)[0] and curblock.count(0) != 0:
#                 print(curblock, curblock_info)
#                 fblock = curblock
#                 fbi = [i, j]
#             curblock = []

#     # Position of any item in block is equal to [i * 3 + index / 3][j * 3 + index % 3]
#     pos = [3 * fbi[0] + int(i / 3), 3 * fbi[1] + int(i % 3)]
#     print(pos, fblock, fbi, number_of_zeros(sudoku, fblock, fbi)[0])
#     return pos


# def number_of_zeros(sudoku, block, index):
#     frow, fcol = [0] * 9, [0] * 9
#     sudoku_T = [[sudoku[j][i]
#                  for j in range(len(sudoku))] for i in range(len(sudoku[0]))]
#     for i in range(len(block)):
#         if block[i] == 0:
#             indexr = 3 * index[0] + int(i / 3)
#             indexc = 3 * index[1] + int(i % 3)
#             currow = sudoku[indexr]
#             curcol = sudoku_T[indexc]
#             if currow.count(0) < frow.count(0) and curcol.count(0) < fcol.count(0):
#                 frow = currow
#                 fcol = curcol
#     print(frow, fcol)
#     noz = frow.count(0) + fcol.count(0) + block.count(0)
#     return [noz, [indexr, indexc]]


if __name__ == "__main__":

    # the_fullest_location(importData())

    sudoku = [[0, 0, 0, 0, 0, 0, 0, 8, 0],
              [0, 6, 0, 0, 0, 4, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 9, 0, 0],
              [2, 1, 0, 0, 8, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 7, 0, 0, 6],
              [0, 0, 3, 0, 0, 0, 4, 0, 0],
              [0, 0, 0, 0, 9, 0, 0, 0, 0],
              [7, 0, 8, 0, 0, 0, 0, 2, 0],
              [4, 0, 9, 6, 0, 0, 7, 0, 0]]

    for row in sudoku:
        print(row)
    print('\n')
    print(the_fullest_location(sudoku=sudoku))
