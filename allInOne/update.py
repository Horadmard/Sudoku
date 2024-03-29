

def update_with_value(*, sudoku: list, location: list, value: int) -> list :
    row = location[0]
    col = location[1]

    sudoku[row][col] = value

    return sudoku




def update(*, sudoku: list, location: list) -> list :
    row = location[0]
    col = location[1]

    sudoku[row][col] = 0

    return sudoku
