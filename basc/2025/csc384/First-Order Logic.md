The most-expressive logical language which has an (somewhat) "appropriate" automated inference procedure.
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
$$A\to B\iff\neg A\lor B$$
$$\neg\neg A\iff A$$
$$\neg(A\land B)\iff \neg A\vee\neg B$$
$$\neg(A\lor B)\iff \neg A\land\neg B$$
$$\neg\forall xA\iff \exists x\neg A$$
$$\neg\exists xA\iff \forall x\neg A$$

