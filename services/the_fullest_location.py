import numpy as np

def the_fullest_location(*, sudoku: list) -> list:

    # Fint the fullest block
    m_block = sudoku[0]

    for block in sudoku:

        if np.count_nonzero(block == 0) < np.count_nonzero(m_block == 0) and np.count_nonzero(block == 0) != 0:
            m_block = block


    print(m_block)
    # fullest_block_index
    fbi = np.where(sudoku = m_block)[0][0]

    # Find the fullest row
    for item in m_block:
        if

        


    # Find the fullest column
        
    # position = [row, col]
    # return position
    pass