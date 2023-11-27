We can use [[Recursion]] to get the ducky to the end of the maze.

![[Untitled (3).png]]
## Writing a recursive function with boolean return type to solve this maze:

```cpp
bool solveMaze(int row, int col){
// Returns false if maze[row][col] is not a valid step towards the exit.
	if(row<0||row>=height||col<0||col>=width){
		return false; // Obvioudly not a valid step as we are stepping outside the maze.
	}
	if (maze[row][col]=='E')
		return true; // Our main base case.
	if (maze[row][col]!='')
		return false; // We have hit a wall or our own path.
	maze[row][col]='*'; // Mark our path

	//The following idea takes advantage of the fact that a step in one of the four
	//Possible directions could be one that brings us closer to 'E'.

	if(solveMaze(row+1, col)) return true;
	if(solveMaze(row-1, col)) return true;
	if(solveMaze(row, col+1)) return true;
	if(solveMaze(row, col-1)) return true;

	//If we arrive here, we are at a "dead end" and should explore the path no further.
	
	maze[row][col]='';
	return false;
}

//Note that at any given point in time, the quantity of * is the depth of recursion.

```