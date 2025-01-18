Used In Generic Approaches
# [[State-Space Model]]
- In this context is a representation of a problem and the space would be the set of all possible configurations, see [[Powersets]]
### Restrictions
- Dedicated **Actions/Successor Functions**
- **Costs**
- **Heuristic** Functions
- Goal States

# Search [[Trees]]
- nodes include path (or alternatively parental pointers), state and cost data

# State [[Graphs]]
- vertices are states and edges represent possible successor functions
# All [[Searching]] Algos we will use
![[Pasted image 20250115161533.png]]
- [[Breadth First Search]] (BFS)
- [[Depth First Search]] (DFS)
- [[Iterative Depth Search]] (IDS)
- [[Uniform Cost Search]] (UCS)
# Aspects of a Search Tree
![[Pasted image 20250115161718.png]]

# Properties
**Completeness**: Will the search always find a solution if a solution exists?  

**Optimality**: Will the search always find the least-cost solution?  

**[[Time Complexity Analysis]]**: What is the maximum number of nodes that we must visit?  

**Space Complexity**: What is the maximum number of nodes that we must store in memory?

# Quantities
$b$: Branching factor.  
- Maximum number of successors of any state.  
$m$: Max depth of the search tree.  
- Length of the longest path.  
$d$: Depth of the shallowest goal node.  
- Length of the shortest solution.