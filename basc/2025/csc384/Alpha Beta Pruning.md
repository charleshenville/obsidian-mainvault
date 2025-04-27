For zero-sum games under [[Minimax Search]]es with [[Heuristics]]. We stop exploring branches that will not turn out well for us.

| Pruning **Max** Branches $@S$                                                                             | Pruning **Min** Branches $@S$                                                                          |
| --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| ![[Pasted image 20250411005244.png]]                                                                      | ![[Pasted image 20250411005302.png]]                                                                   |
| $\bf\beta=8$ : $\alpha=2\to4\to9$                                                                         | $\bf\alpha=7$ : $\beta = 9\to8\to3$                                                                    |
| If $α \geq β$, expanding other branches of $S$ can stop; indicates that $P$ has a better option than $S$. | If $β\leqα$ expanding other branches of $S$ can stop; indicates that $P$ has a better option than $S$. |
## Move Ordering
A strategy we can leverage to make alpha beta pruning more effective. We want to visit the best branch first.
- If we have perfect ordering, our Time Complexity for [[Minimax Search]] goes down to $\mathcal{O}(b^{d/2})$

| **Min** Nodes                                                                                                           | **Max** Nodes                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Best pruning occurs if optimal move for min (branch yielding lowest value) is explored first. (Trig $\beta\leq\alpha$). | Best pruning occurs if optimal move for max (branch yielding highest value) is explored first. (Trig $\alpha\geq\beta$) |
