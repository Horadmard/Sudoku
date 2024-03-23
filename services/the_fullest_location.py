# import numpy as np
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
    #----------------------------------------------------------------
    # Position of any item in block is equal to [i * 3 + index / 3][j * 3 + index % 3]
    frow, fcol = [0] * 9, [0] * 9
    fpos = []
    sudoku_T = [[sudoku[j][i] for j in range(len(sudoku))] for i in range(len(sudoku[0]))]
    print(fbi)
    print(fblock)
    for i in range(len(fblock)):
        if fblock[i] == 0:
            indexr = 3 * fbi[0] + int(i / 3)
            indexc = 3 * fbi[1] + int(i % 3)
            currow = sudoku[indexr]
            curcol = sudoku_T[indexc]
            if currow.count(0) < frow.count(0) and curcol.count(0) < fcol.count(0):
                frow = currow
                fcol = curcol
                pos = [indexr, indexc]
            # sudoku[3*fbi[0]+fblock.index(item)/3][3*fbi[1]+fblock.index(item)%3]
    print(frow, fcol, pos)
    print(f'number of block: {9 - fblock.count(0)}\n number of row: {9 - frow.count(0)}\n number of col: {9 - fcol.count(0)}')
    #----------------------------------------------------------------
    return pos


    # for i in range(3):
    #     for j in range(3):
    #         curblock = sudoku[i*3:(i+1)*3, j*3:(j+1)*3]
    #     if curblock.count(0) < fblock.count(0):
    #         fblock = curblock


    # for i in range(3):
    #     for j in range(3):
    #         curblock = sudoku[i*3:(i+1)*3, j*3:(j+1)*3]
    #         if curblock.count(0) < fblock.count(0):
    #             fblock = curblock

    print("\n fblock:\n",fblock)

    # Now we find the most full block
    # All we have to do is search rows and columns to find the_fullest_location

    # Find the fullest row(in block)
    frow = sudoku[0]

    for row in sudoku[3*fbi[0]:3*(fbi[0]+1)]:
        if row.count(0) < frow.count(0):
            frow = row

    print(frow)

    # Find the fullest column
    sudoku_T = [[sudoku[j][i] for j in range(len(sudoku))] for i in range(len(sudoku[0]))]
    fcol = sudoku_T[0]

    for col in sudoku_T[3*fbi[1]:3*(fbi[1]+1)]: # Actually this is a row in sudoku_T
        if col.count(0) < fcol.count(0):
            fcol = col
    
    print(fcol)

    # Return the position of most busy location
    return [sudoku.index(frow), sudoku_T.index(fcol)]


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