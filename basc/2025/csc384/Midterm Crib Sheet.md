## State-Space Model, Search Trees, State Graphs
- In this context is a representation of a problem and the space would be the set of all possible configurations.
- nodes include path (or alternatively parental pointers), state and cost data
- vertices are states and edges represent possible successor functions
## Properties
**Completeness**: Will the search always find a solution if a solution exists?  
**Optimality**: Will the search always find the least-cost solution?  
**Time Complexity**: What is the maximum number of nodes that we must visit?  
**Space Complexity**: What is the maximum number of nodes that we must store in memory?
##### ![[Pasted image 20250115161533.png]]
$b$: Branching factor.  
- Maximum number of successors of any state.  
$m$: Max depth of the search tree.  
- Length of the longest path.  
$d$: Depth of the shallowest goal node.  
- Length of the shortest solution.
## [[Breadth First Search]] (BFS)
Implemented with [[Queues]] (FIFO)
With [[Greedy Algorithms]], we get *Greedy Breadth First Search (GBFS)* ($h$-only)
- We just expand the node that seems closest to the goal first via some set of [[Heuristics]]
- We utilize a [[Priority Queue]] similar to [[Uniform Cost Search]] where we now just order by whatever seems closest to the goal.
- Note if we use this method, we could get stuck in a loop forever where all nodes in it seem too good to be true.
## [[Depth First Search]] (DFS)
- Implemented with [[Stacks]] (LIFO), bad time complexity but good space complexity.
## [[Iterative Depth Search]] (IDS)
The idea is to do depth-limited [[Depth First Search]]es and increase the limit every time we do not find a a goal state. In **Depth-Limited Search (DLS)**, the work done for a depth limit $l - 1$ *cannot be reused* when performing DLS for depth limit $l$. This is because DLS explores the search tree up to the specified depth $l$, and each new search starts from the root node and explores all branches to the new depth limit.
## [[Uniform Cost Search]] (UCS/Dijkstra)
- Expand the cheapest node on the Frontier.
- nodes on the Frontier will be organized by cost in a [[Priority Queue]]

| UCS Cost Contours                    | UCS Length                           | Search Tree                          |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| ![[Pasted image 20250115163126.png]] | ![[Pasted image 20250224095903.png]] | ![[Pasted image 20250115161718.png]] |

$\epsilon$: Minimum unit Cost considered, $C^*$: Cost to goal
## A*
A combination of [[Greedy Algorithms]] + [[Breadth First Search]] ($h(n)$) and [[Uniform Cost Search]] ($g(n)$). We order a [[Priority Queue]] based of their sum (f-score): $$f(n)=g(n)+h(n)$$Where we expand the node with the LOWEST ***f-value*** first.

| Completeness                         | Optimality                           |
| ------------------------------------ | ------------------------------------ |
| ![[Pasted image 20250131201319.png]] | ![[Pasted image 20250131202029.png]] |
## Node Pruning
- This is to eliminate identical states that come about in different ways
### **Path Checking**: Remembering states visited on one branch
Ensuring that a final state $s_k$ is not equal to any states along the path we took to get there.
$$s_k\not\in\{s_0,s_1,\cdots,s_{k-1}\}$$
This does *not increase time or space complexities*, but this *doesn't prune ALL redundant states*.
### **Cycle Checking**: Remembering all visited states
Now we do additional *checks whenever we encounter a node we want to add to the frontier*:
We check if it is a node that we have *already expanded*, and if it is, we will *not add it to the frontier*.
- in many ways this has the inverse effect of node pruning in terms of time/space complexity and completeness: $\mathcal{O}(b^d)$ space complexity with BFS and could be even worse with DFS.
## Heuristics
- If we modify them we should compare it to the original if we know certain properties of it alr.
### Properties
- Returns non-negative values
- $h(n)=0$ for goal nodes/states
- Computation of result is efficient without searches
#### Admissibility: $h(n)\leq h^*(n)$
#### Consistency (Monotonicity)
- continuing the idea of [[Admissibility]] (Optimism)
- we ensure that the heuristic action cost $\leq$ the actual cost for each action: $$h(A)-h(C)\leq\text{cost}(A\to C)$$This has consequences in [[A-Star]] since the f-value along a path never decreases. 
- This implies [[Admissibility]].
##### ![[Pasted image 20250131203944.png]]
## Constraint Satisfaction Problems
 - **Features:** $\text{Size}\{F\}=k\text{ Variables}$
	- Each Variable has a domain of values
- **State Representation:** An explicit assignment of values to all variables.
- **Goal:** Variable values that satisfy the given constraints of the problem.
- **Variable Degree**: no. constraints a variable is involved in
#### ![[Pasted image 20250221141635.png]]
- **Unary:** ex. $C(X):X<2$
- **Binary:** ex. $C(X,Y): X+Y < 6$
- Higher-Order: ex where no variables can be equal. $$ALL-Diff(V_1,\dots ,V_n): V_1\neq V_2, V_1\neq V_3, \dots$$

| V. BT                                | FC/C-P                               | GAC-P                                |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| ![[Pasted image 20250221152845.png]] | ![[Pasted image 20250224123718.png]] | ![[Pasted image 20250224124102.png]] |
## Dynamically Calculated CSP Heuristics
#### Degree Heuristic (For Variable Choice)
 - Using [[Greedy Algorithms]], select the Variable that is involved in the most constraints imposed on other unassigned variables.
#### Minimum Remaining Values Heuristics (MRV, for Variable Choice):
- To break ties imposed by the first constraint, we should branch off of Variables that have the fewest number of available values, ie they have the smallest domain.
#### Least Constraining Value (For Value Choice)
- Choose a value in the current domain of the selected variable that rules out the least domain values of other neighboring/dependent variables within the constraint set.
## Generalized Arc Consistency
Relating to [[Constraint Satisfaction Problems]] and [[Backtracking Search]].
- This is essentially a more powerful version of Forward Checking:
#### ![[Pasted image 20250223164847.png]]
### Support to an Assignment $V=d$
- An assignment $A$ to a all other variables (within the scope of $C$ but can be more) st. when both are used together - they satisfy $C$.

A Constraint $C$ is said to be **Generally Arc Consistent** **(GAC)**$\iff\forall V_i\in\text{scope}(C)\space\exists\space A_i\in C\space\forall d_i\in\text{CurDom}(V_i)$
A binary constraint, $C(X,Y)$ is arc consistent over X and Y if, for each value in the domain of X there is a corresponding value in the domain of Y that will satisfy the constraint; and vv.
#### We then say [[Constraint Satisfaction Problems]] are GAC $\iff$ all of its unique constraint sets are themselves GAC.

## Propagation in CSPs
### Forward Checking/ Constraint Prop.
- Modest propagation strategy
- When we instantiate a variable $V$ during our search, we check every possible constraint-violating value of another unassigned variable $X$ that appear after the instantiation.
##### ![[Pasted image 20250223122258.png]]
### GAC-Prop.
Using [[Generalized Arc Consistency]] Properties to do [[Constraint Propagation]].
- We may have to re-achieve GAC for some constraints after pruning values that made other constraints arc inconsistent.
- We say that [[Constraint Satisfaction Problems]] must be GAC at every node of the search space.
- In our implementations, have a s.[[Queues]] of constraints that are arc inconsistent and try to empty it for every step in the search. A constraint is added back to the queue if the domains of any variables within it's scope are modified. It can be removed again if it still displays [[Generalized Arc Consistency]].
- Bookkeeping for backtracking still here too like [[Constraint Propagation]]
#### Time Complexity for this process on a CSP with $c$ $k$-ary constraints (`len(scope(Ci))=k`), maximum size of a variable domain $d$:
$$\mathcal{O}(kcd^{k+1})\because\text{ consistency check for one constraint}=\mathcal{O}(d^k),\space\text{do this }\mathcal{O}(kcd)\text{ times}$$