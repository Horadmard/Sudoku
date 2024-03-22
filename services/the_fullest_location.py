import numpy as np

def the_fullest_location(*, sudoku: list) -> list:

    # Fint the fullest block
    m_block = sudoku[0]

    for block in sudoku:

        if np.count_nonzero(block == 0) < np.count_nonzero(m_block == 0):
            m_block = block

    print(m_block)

    # Find the fullest row
    
    idx = 0
    for idx in range(2):

        

    pass