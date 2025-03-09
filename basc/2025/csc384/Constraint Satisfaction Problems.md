Can be formulated as an [[Uninformed Search]] problem or A search problem with [[Heuristics]].

### Key Idea
- Where Search Strategies focus of finding paths to some gal state through some unique state representation, CSPs are different as they only focus of the goal state and less about some sequence of steps to get there. Sudoku solutions are a good example where no explicit steps are required but we still have a unique solution to the problem.

## Definitions:
- **Features:** $\text{Size}\{F\}=k\text{ Variables}$
	- Each Variable has a domain of values
- **State Representation:** An explicit assignment of values to all variables.
- **Goal:** Variable values that satisfy the given constraints of the problem.
![[Pasted image 20250221141635.png]]
- A Solution to such a problem again is just a value assignment to all variables s.t. every constraint is satisfied. 

### Constraint Types:
- **Unary:** ex. $C(X):X<2$
- **Binary:** ex. $C(X,Y): X+Y < 6$
- Higher-Order: ex where no variables can be equal. $$ALL-Diff(V_1,\dots ,V_n): V_1\neq V_2, V_1\neq V_3, \dots$$
### Constraint tables:
- Outline Constraints on a set of variables over all variable domains, but can be compactly represented with logical expressions, ex: $$C(V_1,V_2,V_4)=(V_1==V_2+V_4)$$![[Pasted image 20250221143741.png]]

