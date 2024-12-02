# $$X_1, X_2, \cdots, X_n$$
Note that if Pairwise [[Independence]] is displayed we can create expressions for [[Expected Values]] and [[Variance]]s: $$E[\sum_iX_i]=\sum_iE[X_i]$$$$\text{Var}(\sum_i X_i)=E[(\sum_i X_i-E[\sum_i X_i])^2]$$ We can leverage the expression we found above as well as the [[Correlation and Covariance]] (Some are Zero due to the independent nature, so the only covariances that matter are the ones where we have $COV(X_i, X_i)$) for the [[Random Variables]] $X_i$:
$$\text{Var}(\sum_i X_i)=\sum_i \text{Var}(X_i)$$
Note then if we have IID Xs (**Independent and Identically Distributed**):
$$E[\sum_iX_i]=nE[X],\quad \text{Var}(\sum_i X_i)=n\text{Var}(X)$$
Something to note here, if we increase the amount of IIDs towards $\infty$:
- We get Gaussian [[Random Variables]]
