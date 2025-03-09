Addressing shortcomings with Plain [[Backtracking Search]].
- This Involves Domain Pruning/Filtering of Certain variables for which they are easy to detect faults for (ie no possible value that yields constraint satisfaction)
![[Pasted image 20250223120625.png]]
- This is applied (potentially) at every node of the search tree *during* the search.
### Forward Checking
- Modest propagation strategy
- When we instantiate a variable $V$ during our search, we check every possible constraint-violating value of another unassigned variable $X$ that appear after the instantiation.
![[Pasted image 20250223122258.png]]
``` python
def FCCheck(problem, x)
	for d in x.currentDomain:
		x.value = d
		if !problem.satisfiesConstraints:
			x.currentDomain.remove(d)
		x = None
	if x.currentDomain == {}:
		return DWO # Domain Wipe Out
	return OK
```
- We need to bookkeep to remember which FCCheck invocation resulted in which prunes (since we may have to recover them).
### Variable and Value Ordering [[Heuristics]]:
- Using Heuristics to try and form an educated guess on which variables should be assigned first. `PickUnassignedVariable()`
- Can also be used to determine which values we should try first for a particular variable
- These orderings are dynamically chosen and are previous-assignment-dependent
#### Degree Heuristic (For Variable Choice)
 - Using [[Greedy Algorithms]], select the Variable that is involved in the most constraints imposed on other unassigned variables.
#### Minimum Remaining Values Heuristics (MRV, for Variable Choice):
- To break ties imposed by the first constraint, we should branch off of Variables that have the fewest number of available values, ie they have the smallest domain.
#### Least Constraining Value (For Value Choice)
- Choose a value in the current domain of the selected variable that rules out the least domain values of other neighboring/dependent variables within the constraint set.
![[Pasted image 20250223133903.png]]

FC on its own is on average ~100x faster than regular [[Backtracking Search]], but with MRV, it can be ~10000x faster or better.
