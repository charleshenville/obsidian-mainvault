# Intuitively, a [[Convolution]] would exist if:
- $\tau\to v(t-\tau)w(t)$ via [[Signal Support and Size]], has finite duration $\forall t$
- $v, w\to0$ sufficiently quickly as $\tau\to\pm\infty$

# The following conditions should hold for the [[Convolution]] to exist:
### i) If $v,w$ are right-sided, $\exists$ a right-sided $v*w$.
### ii) If either of $v,w$ have finite duration, $\exists$ $v*w$. Moreover, If both $v,w$ have finite duration, $\exists$ a finite duration $v*w$.
### iii) If $v,w\in L_1,\space\exists(v*w)\in L_1$ and $||v*w||_1\leq||v||_1||w||_1$
### iv) If $v\in L_1, w\in L_2, \exists(v*w)\in L_2$ and $||v*w||_2\leq||v||_1||w||_2$
### v) If $v\in L_1, w\in L_\infty, \exists(v*w)\in L_\infty$ and $||v*w||_\infty\leq||v||_1||w||_\infty$

## Also, for cases i-iii, The [[Convolution]] is also **Associative**: $$x*(v*w)=(x*v)*w$$