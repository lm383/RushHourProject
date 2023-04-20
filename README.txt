# DISCLAIMER
This project uses code from other repositories code in the RushhourLevelGenerator found:
https://github.com/0x1f440/RushhourLevelGenerator
The changes made where adding the converter.py and some code in the main.py was changed. 
code in rush-hour-solver1 can be found here:
https://github.com/marvingfx/rush-hour-solver
The changes made where to the solver.py in the main function and the added solver2 function.


The code has been edited slightly to better fit this experiment.
The experiment is to see how the input size effects the time and space used to compute a descicion problem, in this case the Rush Hour Puzzle.
From this experiment we can also see how different algorithms handle the increased input sizes as well.

#Step 1: Generate the Boards
In the RushhourLevelGenerator folder main.py you can change the line_size variable in the main fuction to change the size of the board e.g line_size=6 will give you 6x6 sized boards.
The number_of_levels variable in the generate function controls how many boards it will generate (Default is 10).
Once the progam is run it will place the boards in the boards folder they will be named according to their size and id number.

#Step 2: Solving the Boards
Move the boards generated into the boards folder in the rush-hour-solver1 folder. 
To solve a board go to solver.py main function and put the name and path of the board in the board variable. The alo variable is for the algotithm you wish to use the options are as follows:
    -   'astar' for a A-Star search algorithm 
    -   'beam' for a Beam search algorithm
    -   'bfs' for a Breadth First search algorithm
    -   'dfs' for a Depth First search algorithm

When solve.py is then run it will print out the steps, states explored and the time it took in seconds.