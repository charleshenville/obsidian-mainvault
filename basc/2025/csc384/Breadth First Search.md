Implemented with [[Queues]]

### With [[Greedy Algorithms]], we get Greedy Breadth First Search (GBFS)
- We just expand the node that seems closest to the goal first via some set of [[Heuristics]]
- We utilize a [[Priority Queue]] similar to [[Uniform Cost Search]] where we now just order by whatever seems closest to the goal.
- Note if we use this method, we could get stuck in a loop forever where all nodes in it seem too good to be true.

### Completeness and Optimality Counterexamples
![[Pasted image 20250131183000.png]]
![[Pasted image 20250131183008.png]]
- Note that if we have a zero heuristic function at every state/node here, we will have thew exact same algorithm as the [[Uniform Cost Search]] where our [[Priority Queue]] is based on only the raw costs.