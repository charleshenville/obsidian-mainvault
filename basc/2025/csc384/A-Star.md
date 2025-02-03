### A combination of [[Greedy Algorithms]] + [[Breadth First Search]] ($h(n)$) and [[Uniform Cost Search]] ($g(n)$). We order a [[Priority Queue]] based of their sum (f-score): $$f(n)=g(n)+h(n)$$
- Where we expand the node with the LOWEST ***f-value*** first.
![[Pasted image 20250131201319.png]]
### Optimality of A* - We must have [[Heuristics]] that display [[Admissibility]]:
![[Pasted image 20250131202029.png]]
