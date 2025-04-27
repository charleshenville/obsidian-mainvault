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



.
## Min Fill Heuristic
- Fairly effective, just get rid of the variable that results in the smallest factor size next. We want to get large reductions in factor scope as soon as possible. 
