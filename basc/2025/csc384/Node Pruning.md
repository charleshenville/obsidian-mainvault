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