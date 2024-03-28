import sys
sys.path.insert(0, '../services/')  # Replace with the actual path

from data import importData, number_of_empty_cells
from the_fullest_location import the_fullest_location
from update import update_with_value, update


stack = []
path = []


def solve_sudoku(*, sudoku: list, max:int) -> list:

    # Defin new_node loc, values
    loc, values = the_fullest_location(sudoku=sudoku)
    new_node = loc, values


    # If there is no choice return to previous state
    if values == None:
        update(sudoku=sudoku, location=stack[-1][0])
        stack.pop()
        solve_sudoku(sudoku=sudoku)
        return

    current_value = values.pop()

    stack.append(new_node)

    if stack.count() == max:
        print(path)

    # Solve the rest of sudoku
    update_with_value(sudoku=sudoku, location=loc, value=current_value)
    solve_sudoku(sudoku=sudoku)

    pass


if __name__ == "__main__":

    List = [1, 2, 3, 4, 5]
    List.append(1)
    List.pop()

    sudoku = sudoku=importData()
    max_stack = number_of_empty_cells(sudoku=sudoku)
    solve_sudoku(sudoku, max=max_stack)