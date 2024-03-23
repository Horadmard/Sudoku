import pandas as pn
import random as rand


def importData():
    df = pn.read_csv('../docs/sample.csv')


    random_col = df['Puzzle'][rand.randint(0, 19)]
    random_col = random_col.replace('.', '0')


    numbers = [int(x) for x in random_col]
    matrix = [numbers[i * 9:(i + 1) * 9] for i in range(9)]


    # for row in matrix:
    #     print(row)
    
    return matrix

