import numpy as np
from data import importData

def the_fullest_location(sudoku: list) -> list:

    pos = []

    # Find the fullest row
    frow = sudoku[0]

    for row in sudoku:
        if row.count(0) < frow.count(0):
            frow = row

    # Find the fullest column
    sudoku_T = [[sudoku[j][i] for j in range(len(sudoku))] for i in range(len(sudoku[0]))]
    fcol = sudoku_T[0]

    for col in sudoku_T:
        if col.count(0) < fcol.count(0):
            fcol = col
    
    # Find the fullest Block
    fblock = []
    curblock = []

    for i in range(3):
        for j in range(3):
            for k in range(3):
                for item in sudoku[3*i + k][3*j:3*j + 3]:
                    curblock.append(item)
            if curblock.count(0) < fblock.count(0):
                fblock = curblock
            curblock = []

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
            
    
    # Define the position of most busy location
    pos = [sudoku.index(frow), sudoku_T.index(fcol)]
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