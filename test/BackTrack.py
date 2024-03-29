import sys
sys.path.insert(0, '../services/')  # Replace with the actual path

from data import importData, number_of_empty_cells
from the_fullest_location import the_fullest_location
from update import update_with_value, update


stack = []
path = []


def solve_sudoku(*, sudoku: list, max:int) -> list:

    # Defin new_node loc, values
    # loc, values = the_fullest_location(sudoku=sudoku)
    new_node = []
    new_node = the_fullest_location(sudoku=sudoku)
    loc, values = new_node[0], new_node[1]


    # If there is no choice return to previous state
    while values == None:
        new_node = stack.pop()
        loc, values = new_node[0], new_node[1]
        update(sudoku=sudoku, location=loc)


    current_value = values.pop()

    stack.append(new_node)
    path.append(current_value)
    update_with_value(sudoku=sudoku, location=loc, value=current_value)


    if len(stack) == max:
        print(path)
        return

    # Solve the rest of sudoku
    solve_sudoku(sudoku=sudoku, max=max)


if __name__ == "__main__":

    sudoku = sudoku=importData()
    max_stack = number_of_empty_cells(sudoku=sudoku)
    solve_sudoku(sudoku=sudoku, max=max_stack)