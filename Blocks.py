import numpy as np
import pandas as pn
import random as rand

df = pn.read_csv('../docs/sample.csv')
df[['Puzzle', 'Difficulty']].head()

col1 = df['Puzzle'][rand.randint(0, 19)]

# Convert the string to a list of integers
col1 = col1.replace('.', '0')
numbers = [int(x) for x in col1]

# Creating the 2D matrix
matrix = [numbers[i * 3:(i + 1) * 3] for i in range(3)]
numpy_array = np.array(matrix)

# Initialize an empty list to store the Blocks
Blocks = []

# Split the matrix into 9, 3x3 blocks
for i in range(3):
    for j in range(3):
        Block = numpy_array[i*3:(i+1)*3, j*3:(j+1)*3]
        Blocks.append(Block)

# Print the resulting Blocks
for idx, Block in enumerate(Blocks):
    print(f"Block {idx}:\n{Block}\n")