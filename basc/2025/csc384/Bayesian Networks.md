We have conditional probability tables for all variables in the scope of this Directed Acyclic [[Graphs]] for [[Reasoning Under Uncertainty]].
At the root: $$Pr(X1,…,Xn) = Pr(Xn|X1,…,Xn-1)Pr(Xn-1|X1,…,Xn-2)…Pr(X1)$$![[Pasted image 20250418171520.png]]
## Factored Distributions
$$h(X,Y,Z)=f(X,Y)g(Y,Z)$$
![[Pasted image 20250418171729.png]]
## Independence In A Bayesian Net
$$P(X_i|S\cup \text{Parent}(X_i))=P(X_i|\text{Parent}(X_i)):S\subseteq \text{NonDescendents}(X_i)$$
- We can also use the **D-Seperation** (no paths existing between) Graphical Property to determine Independence here.
- $(X,Y|E)$ are independent if the evidence $E$ d-seperates $X$ and $Y$.