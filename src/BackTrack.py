import sys
sys.path.insert(0, '../services/')  # Replace with the actual path

from data import importData
from the_fullest_location import the_fullest_location
from update import update_with_value, update


stack = []
# stack.append()
# stack.pop()
path = []


def solve_sudoku(*, sudoku: list) -> list:

    # defin node
    # loc, values
    loc, values = the_fullest_location(sudoku=sudoku)
    node = loc, values

    # if there is no choice return to previous state
    if values == None: 
        stack.pop()
        return 0
    
    stack.append(node)

    # check if problem solved
    # if stack.count() == max:
    #     pass

    # solve the rest of sudoku
    update_with_value(sudoku=sudoku, location=loc, value=values.pop())

    solve_sudoku(sudoku=sudoku)

    pass


if __name__ == "__main__":

    List = [1, 2, 3, 4, 5]
    List.append(1)
    List.pop()

    solve_sudoku(sudoku=importData())
