# $$h(s)$$
An attempt to help us solve [[Uninformed Search]] Problems more effectively.
### Properties
- Returns non-negative values
- $h(n)=0$ for goal nodes/states
- Computation of result is efficient without searches
# Consistent (Monotone) Heuristics
- continuing the idea of [[Admissibility]]
- we ensure that the heuristic action cost $\leq$ the actual cost for each action: $$h(A)-h(C)\leq\text{cost}(A\to C)$$
	- This has consequences in [[A-Star]] since the f-value along a path never decreases.
	- This actually implies [[Admissibility]].
![[Pasted image 20250131203944.png]]
$$$$
