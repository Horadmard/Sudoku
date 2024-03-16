# The Sudoku game as AI Project using BackTrack Algorithm

To do:
- Use BackTrack Method
- Implant Tree and DFS(or smt better)
- The Sudoku table must be clarify as a matrix of matrices
- Algorithm Explanation
- Time Complexity?
- Space Complexity?


Tips:
- Starting with low number blocks could accelerate the program
- Node of the tree must know thair childs and surely thair value and position
- The navigated path must be stored(in a stack)
- Maybe DFS isn't the last answer(Think about other navigation methods)
- Do we have really need to Create all the tree? or just Create our navigating path

## Algorithm:

Phase 1 we navigate the Sudoku table and by table, i mean the matrix we produced befor. consider every blank part as a row or list of nodes in $Decision Tree$, where each node has 3 parts -> Value, Position and its Childs.

Then we make the tree completely set and start to navigate it with DFS method, to find the right answer. each branch who reach to a leaf or had right amount of nodes is the answer.