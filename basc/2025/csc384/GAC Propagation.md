Using [[Generalized Arc Consistency]] Properties to do [[Constraint Propagation]].
- We may have to re-achieve GAC for some constraints after pruning values that made other constraints arc inconsistent.
- We say that [[Constraint Satisfaction Problems]] must be GAC at every node of the search space.
- In our implementations, have a s.[[Queues]] of constraints that are arc inconsistent and try to empty it for every step in the search. A constraint is added back to the queue if the domains of any variables within it's scope are modified. It can be removed again if it still displays [[Generalized Arc Consistency]].
- Bookkeeping for backtracking still here too like [[Constraint Propagation]]
#### Time Complexity for this process on a CSP with $c$ $k$-ary constraints (`len(scope(Ci))=k`), maximum size of a variable domain $d$:$$\mathcal{O}(kcd^{k+1})\because\text{ consistency check for one constraint}=\mathcal{O}(d^k),\space\text{do this }\mathcal{O}(kcd)\text{ times}$$