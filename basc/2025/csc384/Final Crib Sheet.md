## State-Space Model, Search Trees, State Graphs
- In this context is a representation of a problem and the space would be the set of all possible configurations.
- nodes include path (or alternatively parental pointers), state and cost data
- vertices are states and edges represent possible successor functions
## Properties
**Completeness**: Will the search always find a solution if a solution exists?  
**Optimality**: Will the search always find the least-cost solution?  
**Time Complexity**: What is the maximum number of nodes that we must visit?  
**Space Complexity**: What is the maximum number of nodes that we must store in memory?
##### ![[Pasted image 20250115161533.png]]
$b$: Branching factor.  
- Maximum number of successors of any state.  
$m$: Max depth of the search tree.  
- Length of the longest path.  
$d$: Depth of the shallowest goal node.  
- Length of the shortest solution.
## [[Breadth First Search]] (BFS)
Implemented with [[Queues]] (FIFO)
With [[Greedy Algorithms]], we get *Greedy Breadth First Search (GBFS)* ($h$-only)
- We just expand the node that seems closest to the goal first via some set of [[Heuristics]]
- We utilize a [[Priority Queue]] similar to [[Uniform Cost Search]] where we now just order by whatever seems closest to the goal.
- Note if we use this method, we could get stuck in a loop forever where all nodes in it seem too good to be true.
## [[Depth First Search]] (DFS)
- Implemented with [[Stacks]] (LIFO), bad time complexity but good space complexity.
## [[Iterative Depth Search]] (IDS)
The idea is to do depth-limited [[Depth First Search]]es and increase the limit every time we do not find a a goal state. In **Depth-Limited Search (DLS)**, the work done for a depth limit $l - 1$ *cannot be reused* when performing DLS for depth limit $l$. This is because DLS explores the search tree up to the specified depth $l$, and each new search starts from the root node and explores all branches to the new depth limit.
## [[Uniform Cost Search]] (UCS/Dijkstra)
- Expand the cheapest node on the Frontier.
- nodes on the Frontier will be organized by cost in a [[Priority Queue]]

| UCS Cost Contours                    | UCS Length                           | Search Tree                          |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| ![[Pasted image 20250115163126.png]] | ![[Pasted image 20250224095903.png]] | ![[Pasted image 20250115161718.png]] |

$\epsilon$: Minimum unit Cost considered, $C^*$: Cost to goal
## A*
A combination of [[Greedy Algorithms]] + [[Breadth First Search]] ($h(n)$) and [[Uniform Cost Search]] ($g(n)$). We order a [[Priority Queue]] based of their sum (f-score): $$f(n)=g(n)+h(n)$$Where we expand the node with the LOWEST ***f-value*** first.

| Completeness                         | Optimality                           |
| ------------------------------------ | ------------------------------------ |
| ![[Pasted image 20250131201319.png]] | ![[Pasted image 20250131202029.png]] |
## Node Pruning
- This is to eliminate identical states that come about in different ways
### **Path Checking**: Remembering states visited on one branch
Ensuring that a final state $s_k$ is not equal to any states along the path we took to get there.
$$s_k\not\in\{s_0,s_1,\cdots,s_{k-1}\}$$
This does *not increase time or space complexities*, but this *doesn't prune ALL redundant states*.
### **Cycle Checking**: Remembering all visited states
Now we do additional *checks whenever we encounter a node we want to add to the frontier*:
We check if it is a node that we have *already expanded*, and if it is, we will *not add it to the frontier*.
- in many ways this has the inverse effect of node pruning in terms of time/space complexity and completeness: $\mathcal{O}(b^d)$ space complexity with BFS and could be even worse with DFS.
## Heuristics
- If we modify them we should compare it to the original if we know certain properties of it alr.
### Properties
- Returns non-negative values
- $h(n)=0$ for goal nodes/states
- Computation of result is efficient without searches
#### Admissibility: $h(n)\leq h^*(n)$
#### Consistency (Monotonicity)
- continuing the idea of [[Admissibility]] (Optimism)
- we ensure that the heuristic action cost $\leq$ the actual cost for each action: $$h(A)-h(C)\leq\text{cost}(A\to C)$$This has consequences in [[A-Star]] since the f-value along a path never decreases. 
- This implies [[Admissibility]].
##### ![[Pasted image 20250131203944.png]]
## Constraint Satisfaction Problems
 - **Features:** $\text{Size}\{F\}=k\text{ Variables}$
	- Each Variable has a domain of values
- **State Representation:** An explicit assignment of values to all variables.
- **Goal:** Variable values that satisfy the given constraints of the problem.
- **Variable Degree**: no. constraints a variable is involved in
#### ![[Pasted image 20250221141635.png]]
- **Unary:** ex. $C(X):X<2$
- **Binary:** ex. $C(X,Y): X+Y < 6$
- Higher-Order: ex where no variables can be equal. $$ALL-Diff(V_1,\dots ,V_n): V_1\neq V_2, V_1\neq V_3, \dots$$

| V. BT                                | FC/C-P                               | GAC-P                                |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| ![[Pasted image 20250221152845.png]] | ![[Pasted image 20250224123718.png]] | ![[Pasted image 20250224124102.png]] |
## Dynamically Calculated CSP Heuristics
#### Degree Heuristic (For Variable Choice)
 - Using [[Greedy Algorithms]], select the Variable that is involved in the most constraints imposed on other unassigned variables.
#### Minimum Remaining Values Heuristics (MRV, for Variable Choice):
- To break ties imposed by the first constraint, we should branch off of Variables that have the fewest number of available values, ie they have the smallest domain.
#### Least Constraining Value (For Value Choice)
- Choose a value in the current domain of the selected variable that rules out the least domain values of other neighboring/dependent variables within the constraint set.
## Generalized Arc Consistency
Relating to [[Constraint Satisfaction Problems]] and [[Backtracking Search]].
- This is essentially a more powerful version of Forward Checking:
#### ![[Pasted image 20250223164847.png]]
### Support to an Assignment $V=d$
- An assignment $A$ to a all other variables (within the scope of $C$ but can be more) st. when both are used together - they satisfy $C$.

A Constraint $C$ is said to be **Generally Arc Consistent** **(GAC)**$\iff\forall V_i\in\text{scope}(C)\space\exists\space A_i\in C\space\forall d_i\in\text{CurDom}(V_i)$
A binary constraint, $C(X,Y)$ is arc consistent over X and Y if, for each value in the domain of X there is a corresponding value in the domain of Y that will satisfy the constraint; and vv.
#### We then say [[Constraint Satisfaction Problems]] are GAC $\iff$ all of its unique constraint sets are themselves GAC.

## Propagation in CSPs
### Forward Checking/ Constraint Prop.
- Modest propagation strategy
- When we instantiate a variable $V$ during our search, we check every possible constraint-violating value of another unassigned variable $X$ that appear after the instantiation.
##### ![[Pasted image 20250223122258.png]]
### GAC-Prop.
Using [[Generalized Arc Consistency]] Properties to do [[Constraint Propagation]].
- We may have to re-achieve GAC for some constraints after pruning values that made other constraints arc inconsistent.
- We say that [[Constraint Satisfaction Problems]] must be GAC at every node of the search space.
- In our implementations, have a s.[[Queues]] of constraints that are arc inconsistent and try to empty it for every step in the search. A constraint is added back to the queue if the domains of any variables within it's scope are modified. It can be removed again if it still displays [[Generalized Arc Consistency]].
- Bookkeeping for backtracking still here too like [[Constraint Propagation]]
#### Time Complexity for this process on a CSP with $c$ $k$-ary constraints (`len(scope(Ci))=k`), maximum size of a variable domain $d$:
$$\mathcal{O}(kcd^{k+1})\because\text{ consistency check for one constraint}=\mathcal{O}(d^k),\space\text{do this }\mathcal{O}(kcd)\text{ times}$$
# General Minimax Strategy
**Assumption:** The other player always plays its best move. Strategy is optimal $\iff$ opponent is playing optimally. If the opponent isn’t optimal, can develop a better strategy that exploits weaknesses.
**Decision:** Play a move that minimizes the payoff that could be gained by other player.
**Time Complexity:** $\mathcal{O}(b^d)$ (Exhaustive [[Depth First Search]])
$b\to$ number of legal moves at each state.
$d\to$ total number of turns for both players.
$1 + b + b^2 + … + b^{d-1} ∈ \mathcal{O}(b^d)$.

![[Pasted image 20250411002915.png]]

## The Eval Function
We can stop minimax+alpha beta early and guess which move we should make by taking the value of an evaluation function. Could be the number of max pieces minus the number of min pieces for orthello.

# Alpha-Beta Pruning

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
The most-expressive logical language which has an (somewhat) "appropriate" automated inference procedure.

# Logical Representation
### Logical Entitlement
Sentences $P_1,\dots, P_n$ entail $P\iff$ $P$'s truth is implicit in the truth of sequences ($P_1,\dots, P_n\to P$).
### Logic & Logical Inference
Study of entailment relations/ truth conditions, rules of inference. Inference is just Calculating Entailments.
### The Following Components are Required:
- A set of $V$ **variables**
- A set of $F$ **function** symbols
- A set of $P$ **predicate (relation)** symbols
- Functions and Variables comprise **Terms** denoting elements of domain.
- **Predicates** are defined over terms; atomic formulas denoting properties/relations.

A formula $A$ is a **logical consequence** of $Φ$ (denoted by $Φ \space|\!\!\!= A$) iff for every truth assignment $τ$, if $τ$ satisfies $Φ$, then $τ$ satisfies $A$.
### First-Order Vocabulary
$\mathcal{L}=\{\}$ containing functions & predicate symbols. Every variable is a term.
If $f\to n$-ary function symbol $\in\mathcal{L}$ and $t_1, t_2, \dots,t_n$ are $\mathcal{L}$-terms, then $f(t_1, t_2, \dots,t_n)$ is an $\mathcal{L}$-term.
## Logical Satisfiability
- $\mathcal{M}$ satisfies $\Phi$ ($\mathcal{M} \space|\!\!\!= \Phi$) if $\forall A\in\Phi, \mathcal{M}\space|\!\!\!=A$.
- If the above is true, $\mathcal{M}$ is a **model** of $\Phi$.
- If $\exists\mathcal{M}:\mathcal{M}\space|\!\!\!= \Phi$, $\Phi$ is said to be **satisfiable**.

## Clausal Formation
| $A\to B\iff\neg A\lor B$             | $\neg\neg A\iff A$                   | $\neg(A\land B)\iff \neg A\vee\neg B$ |
| ------------------------------------ | ------------------------------------ | ------------------------------------- |
| $\neg\exists xA\iff \forall x\neg A$ | $\neg\forall xA\iff \exists x\neg A$ | $\neg(A\lor B)\iff \neg A\land\neg B$ |

# Reasoning Under Uncertainty
- Reason with [[Cumulative Distribution Function]]s
![[Pasted image 20250418163751.png]]
## Probability Rules

| **Rule**                                 | **Formula**                                                                                                                                                  |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| *Bayes Rule*                             | $\Pr(A \mid B) = \frac{\Pr(B \mid A)\Pr(A)}{\Pr(B)}$                                                                                                         |
| *Chain Rule*                             | $\Pr(A_1 \land A_2 \cdots \land A_n)$$= \Pr(A_n \mid A_1 \cdots \land A_{n-1}) \Pr(A_{n-1} \mid A_1 \cdots \land A_{n-2})$$\cdots \Pr(A_2 \mid A_1)\Pr(A_1)$ |
| *Independence*                           | $\Pr(A \mid B) = \Pr(A)$                                                                                                                                     |
| *Definition of Independence*             | $\Pr(A \land B) = \Pr(A) \Pr(B)$                                                                                                                             |
| *Conditional Independence*               | $\Pr(A \mid B \land C) = \Pr(A \mid C)$                                                                                                                      |
| *Definition of Conditional Independence* | $\Pr(A \land B \mid C) = \Pr(A \mid C) \Pr(B \mid C)$                                                                                                        |
| *General Dependence*                     | $\text{Pr}(A\mid B)=\frac{\text{Pr}(A,B)}{\text{Pr}(B)}$                                                                                                     |
# Bayesian Networks
We have conditional probability tables for all variables in the scope of this Directed Acyclic [[Graphs]] for [[Reasoning Under Uncertainty]].
At the root: $Pr(X1,…,Xn) = Pr(Xn|X1,…,Xn-1)Pr(Xn-1|X1,…,Xn-2)…Pr(X1)$

![[Pasted image 20250418171520.png]]
## Cond. Prob. Tables and Factored Distributions
$$h(X,Y,Z)=f(X,Y)g(Y,Z)$$
![[Pasted image 20250418171729.png]]
## Independence In A Bayesian Net
$$P(X_i|S\cup \text{Parent}(X_i))=P(X_i|\text{Parent}(X_i)):S\subseteq \text{NonDescendents}(X_i)$$
- We can also use the **D-Seperation** (no paths existing between) Graphical Property to determine Independence here.
- $(X,Y|E)$ are independent if the evidence $E$ **d-seperates** $X$ and $Y$.
![[Pasted image 20250424161425.png]]
## Variable Elimination Example
![[Pasted image 20250418183602.png]]
$$F=f_1(A)f_2(B)f_3(A,B,C)f_4(C,D)$$
$$F'=f_1(A)f_2(B)f_3(A,B,C)f_4(C)|_{D=d}$$
$$F''=f_1(A)f_2(B)g_1(A,B): g_1(A,B)=\sum _{c_i\in C}f_3(A,B,c_i)f_4(c_i)$$
$$F'''(A)=f_1(A)g_2(A): g_2(A)=\sum _{b_i\in B}f_2(b_i)g_1(A,b_i)$$
$$P(A|D=d)=\frac{f_1(A)g_2(A)}{\sum_{a_i\in A}f_1(a_i)g_2(a_i)}$$

## Min Fill Heuristic
- Fairly effective, just get rid of the variable that results in the smallest factor size next. We want to get large reductions in factor scope as soon as possible. 
