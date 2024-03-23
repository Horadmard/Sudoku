import pandas as pn
import random as rand


def importData():
    df = pn.read_csv('../docs/sample.csv')


    col1 = df['Puzzle'][rand.randint(0, 19)]
    col1 = col1.replace('.', '0')

    numbers = [int(x) for x in col1]
    matrix = [numbers[i * 9:(i + 1) * 9] for i in range(9)]

    # for row in matrix:
    #     print(row)
    
    return matrix