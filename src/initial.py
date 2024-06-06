import random as rand

def value_of_location(*, sudoku: list, block: int) -> list:


    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    row = location[0]
    col = location[1]

    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3) :
        for j in range(3) :
            number = sudoku[i + start_row][j + start_col]
            if number in numbers :
                numbers.remove(number)

    return numbers



def random_generate(*, org_sudoku):

    initial_sudoku = org_sudoku
    for i in range(9):
        values = value_of_location(org_sudoku, block = i)

        for i in range(3) :
            for j in range(3) :
                if org_sudoku[i][j] == 0:
                    index = rand.randint(len(values))
                    initial_sudoku[i][j] = values[index]
        
    
    # code

    pass



def cost_func(*, sudoku):

    # code 

    pass



