For [[Uninformed Search]]
# This is to eliminate identical states that come about in different ways

# Approaches
- **Path Checking**: Remembering states visited on one branch
- **Cycle Checking**: Remembering all visited states

# Path Checking
- Ensuring that a final state $s_k$ is not equal to any states along the path we took to get there.
$$s_k\not\in\{s_0,s_1,\cdots,s_{k-1}\}$$
- This does not increase time or space complexities.
- This doesn't prune ALL redundant states.

# Cycle Checking 
- Now we do additional checks whenever w2e encounter a node4 we want to add to the frontier
	- We check if it is a node that we have already expanded, and if it is, we will not add it to the frontier.
![[Pasted image 20250131180440.png]]
- in many ways this has the inverse effect of node pruning in terms of time/space complexity and completeness
	- $\mathcal{O}(b^d)$ space complexity with BFS and could be even worse with DFS
	