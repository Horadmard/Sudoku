
from data import importData, number_of_empty_cells
from the_fullest_location import the_fullest_location
from update import update_with_value, update
from node import Node


stack = []
path = []


def solve_sudoku(*, sudoku: list, max:int) -> list:

    # Defin new_node loc, values
    # loc, values = the_fullest_location(sudoku=sudoku)
    loc, values = the_fullest_location(sudoku=sudoku)
    new_node = Node(loc, values)

    # If there is no choice return to previous state
    while new_node.values == []:
        if stack:
            new_node = stack.pop()
            path.pop()
            update(sudoku=sudoku, location=new_node.loc)
        else:
            return None

    if new_node.values:
        current_value = new_node.values.pop()
    else:
        return None

    stack.append(new_node)
    path.append(current_value)
    update_with_value(sudoku=sudoku, location=new_node.loc, value=current_value)


    if len(stack) == max:
        # print(path)
        return None

    # Solve the rest of sudoku
    solve_sudoku(sudoku=sudoku, max=max)


if __name__ == "__main__":

    sudoku = importData()
    max_stack = number_of_empty_cells(sudoku=sudoku)

    for row in sudoku:
        print(row)
    
    print('Solved pazzel ----------------------------------')
    solve_sudoku(sudoku=sudoku, max=max_stack)

    for row in sudoku:
        print(row)