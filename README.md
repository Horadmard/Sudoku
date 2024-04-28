# Start Over

For Solving this problem we consider Modular Programming.

## Contributing

After installing required packages such as 
1. pandas
2. random

run codes below:

```
$ git clone https://github.com/Horadmard/Sudoku.git
$ cd Sudoku/src
$ python3 solve.py
```

send us PRs thanks (;

## New Algorithm and Definition of Solve_function is as below:

 1. Find the the_fullest_location of empty cells in the Sudoku Table
 2. Get a list of values that can be placed in that empty cell(tfl).
 3. Create a node with location and values.

 3. While node.values have no value, then:
        If stack atleast have one value, then:
            pop from stack and path untill one of the nodes.values have atleast one element. update the sudoku table by every stack pop with zero and location.
        else: the problem is unsolvable(deadend)

 6. Next, pop an element from node.values, push it into path and push node into stack. 
        update the sudoku table with value and location.

 7. If stack.length reached to number of empty cells, then: 
        problem is solved.
 8. else:
        Try to Solve the updated Sudoku Table


Also this Alghorithm needs to store navigated path, so defining a proper structure is necessary.
In this situation it's Stack.




# The Sudoku game as AI Project using $BackTrack$ Algorithm

To do:
- Use $BackTrack$ Method
- Implant Tree and DFS(or smt better)
- The Sudoku table must be clarify as a $9\times9$ block matrics that every block is a $9\times9$ matrics
- Algorithm Explanation
- Time Complexity?
- Space Complexity?


Tips:
- Starting with low number blocks could accelerate the program
- $Node$ of the tree must know thair childs and surely thair value and position
- The navigated path must be stored(in a stack)
- Maybe DFS isn't the last answer(Think about other navigation methods)
- Do we have really need to Create all the tree? or just Create our navigating path
- In the next project phase we can use the release option of github

## Algorithm(expired):

Phase 1 we navigate the Sudoku table and by table, i mean the matrix we produced befor. consider every blank part as a row or list of $Nodes$ in $Decision Tree$, where each $Node$ has 3 parts -> Value, Position and its Childs.

Then we make the tree completely set and start to navigate it with DFS method, to find the right answer. each $branch$ who reach to a $leaf$ or had right amount of $Nodes$ is the answer.

${
    c|c|c
    c|c|c
    c|c|c
}$
