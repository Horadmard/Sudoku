from data import importData

def the_fullest_location(sudoku: list) -> list:

    # Find the fullest Block
    fblock = [0] * 9
    curblock = []
    fbi = []

    for i in range(3):
        for j in range(3):
            for k in range(3):
                for item in sudoku[3*i + k][3*j:3*j + 3]:
                    curblock.append(item)
            print(curblock, i, j)
            if curblock.count(0) < fblock.count(0) and curblock.count(0) != 0:
                fblock = curblock
                fbi = [i, j]
            curblock = []
    # ----------------------------------------------------------------
    # Position of any item in block is equal to [i * 3 + index / 3][j * 3 + index % 3]
    sudoku_T = [[sudoku[j][i]
                 for j in range(len(sudoku))] for i in range(len(sudoku[0]))]
    print(fbi)
    print(fblock)

    def number_of_not_blanks(sudoku, block, index):
        frow, fcol = [0] * 9, [0] * 9
        for i in range(len(block)):
            if block[i] == 0:
                indexr = 3 * index[0] + int(i / 3)
                indexc = 3 * index[1] + int(i % 3)
                currow = sudoku[indexr]
                curcol = sudoku_T[indexc]
                if currow.count(0) < frow.count(0) and curcol.count(0) < fcol.count(0):
                    frow = currow
                    fcol = curcol
        return [frow.count(0) + fcol.count(0) + block.count(0), [indexr, indexc]]

    # ----------------------------------------------------------------
    return pos


if __name__ == "__main__":

    the_fullest_location(importData())

    # sudoku =[[0, 0, 0, 0, 0, 0, 0, 8, 0],
    #          [0, 6, 0, 0, 0, 4, 0, 0, 0],
    #          [0, 0, 1, 0, 0, 0, 9, 0, 0],
    #          [2, 1, 0, 0, 8, 0, 0, 0, 0],
    #          [0, 0, 0, 0, 1, 7, 0, 0, 6],
    #          [0, 0, 3, 0, 0, 0, 4, 0, 0],
    #          [0, 0, 0, 0, 9, 0, 0, 0, 0],
    #          [7, 0, 8, 0, 0, 0, 0, 2, 0],
    #          [4, 0, 9, 6, 0, 0, 7, 0, 0]]

    # print(the_fullest_location(sudoku))
