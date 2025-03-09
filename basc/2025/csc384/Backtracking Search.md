A type of [[Depth First Search]] used to solve [[Constraint Satisfaction Problems]]:
- We Search through the space of *Partial (Variable) Assignments* and decide on suitable values variable by variable where assignment order does not matter.
- Immediately reject an assignment if it leads to a constraint falsification.

## [[Constraint Satisfaction Problems]] - Search [[Trees]] (They Illustrate How Backtracking Search Works):
- **Root:** Empty Assignment
- **Children of a Node:** All Possible Subsequent Variable assignments where we will only explore the ones that satisfy problem constraints (tree stops descending).
*For 4-Queens:*![[Pasted image 20250221152845.png]]
![[Pasted image 20250221153513.png]]
