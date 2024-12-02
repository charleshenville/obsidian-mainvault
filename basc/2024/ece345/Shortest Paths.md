Dijkstra's only applies to graphs for which all edges are positively weighted
- Relaxed Algorithm ensures we respect triangular inequalities

DFS/BFS can be employed -> becomes a non-[[NP Completeness]] problem in the case of TSP

# Bellman Ford Algorithm
looking at negative cycles in a graph: ==a cycle where the sum of the weights of its edges is negative==
- Reports negative cycles and `Relax()` all edges 

Given a ****weighted**** graph with ****V**** vertices and ****E**** edges, and a source vertex ****src****, find the ****shortest path**** from the source vertex to all vertices in the given graph. If a vertex cannot be reached from source vertex, mark its distance as 108.

*Note*: If a graph contains negative weight cycle, return -1.

**Examples:**

***Input**: V = 5, edges = ([1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]), src = 0
> 
> ![bellman_ford_input_images](https://media.geeksforgeeks.org/wp-content/uploads/20241018163210610023/bellman_ford_input_images.webp)
> 
> **Output**: [0, 5, 6, 6, 7]
> 
> **Input**: V = 4, edges = ([0, 1, 4], [1, 2, -6], [2, 3, 5], [3, 1, -2]), src = 0
> 
> ![input-2](https://media.geeksforgeeks.org/wp-content/uploads/20241016175549040804/input-2.webp)
> 
> ****Output****: [-1]  
> ****Explanation:**** The graph contains negative weight cycle