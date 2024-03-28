# Start Over

For Solving this problem we consider Fuctionality Programming.

## New Algorithm and Definition of Solve_function is as below:

 1. Find the the_fullest_location of empty cells in the Sudoku Table
 2. Get a list of valid numbers that can be placed in that empty cell and place it
 4. Try to Solve the new Sudoku Table
 5. If Algorithm reach a Deadend back to a previous level(acording to stored data) and try another valid number
 6. If Sudoku table was full(the_fullest_location function couldn't find anything), the problem is solved and print the answer

*Two last condition must be implanted in right place.*

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

## Algorithm:

Phase 1 we navigate the Sudoku table and by table, i mean the matrix we produced befor. consider every blank part as a row or list of $Nodes$ in $Decision Tree$, where each $Node$ has 3 parts -> Value, Position and its Childs.

Then we make the tree completely set and start to navigate it with DFS method, to find the right answer. each $branch$ who reach to a $leaf$ or had right amount of $Nodes$ is the answer.

${
    c|c|c
    c|c|c
    c|c|c
}$
