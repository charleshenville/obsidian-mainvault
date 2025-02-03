UCS Using [[Searching]] and a type of [[Uninformed Search]]
# Expand the cheapest node on the Frontier.
- nodes on the Frontier will be organized by cost in a [[Priority Queue]]

![[Pasted image 20250115163126.png]]

# Properties
![[Pasted image 20250115163530.png]]
- This algorithm is optimal because of this lemma - ie it is guaranteed to find the optimal path **first** as it would be the cheapest.
![[Pasted image 20250115165140.png]]
- Note we need a minimum cost per operation here since otherwise we could potentially traverse an infinitely long path like 1->0.5->0.25->0.125->...
- We say the min cost is $\geq\epsilon\gt0$

Note - this is **just Dijkstra's algorithm** - and is identical to Breadth First search in the case that all edge weights are equal/ we have all costs across all actions to be the same.