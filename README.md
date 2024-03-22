# Start Over

For Solving this problem we consider Fuctionality Programming.

## Definition of Solve_function is as below:

 1. Find the most_busy blank in the Sudoku Table
 2. Give me a list of valid numbes that can be placed in blank
 3. Try to Solve new Sudoku Table
 4. If Algorithm reach a Deadend back to a previous level and try another valid number
 5. If Sudoku table was full(most_busy function couldn't find anything), the problem is solved and print the answer




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
