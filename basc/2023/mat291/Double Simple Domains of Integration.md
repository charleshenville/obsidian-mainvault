## Simple Regions:
- $S\subseteq\mathbb{R}^2$ is a Simple Region if it is of one of these forms:
$$S=\{(x,y):a\leq x\leq b, \Phi(x)\leq y\leq\Psi(x)\}$$
$$S=\{(x,y):a\leq y\leq b, \Phi(y)\leq x\leq\Psi(y)\}$$
Where $\Phi, \Psi$ are continuous, single-variable functions.
![[IMG_568843B242B0-1.jpeg]]
## Fubini's Theorem for Simple Regions
- Provided $f$ displays [[Continuity]] in the Simple Region, $S$:

$$\iint_{S} f(x,y)dA=\int_{a}^{b}\int_{\Phi(x)}^{\Psi(x)}f(x,y)dydx\neq\int_{\Phi(x)}^{\Psi(x)}\int_{a}^{b}f(x,y)dxdy$$
The last integral does not make sense since we do not want $x$ in our final answer. We want a concrete volume. We can swap the order of the [[Double Integrals]] but it is not as easy as [[Double Rectangular Domains of Integration]].

## Swapping Order of Double Integrals' Integration:
1. Draw the function.
2. Swap the axes.
3. Compute your new integral bounds.

Example:
![[IMG_5907DCEB2B98-1.jpeg]]
$$\int_{-1}^1\int_0^{x^2} f(x,y)dydx=\int_0^1\int_{-1}^{-\sqrt y} f(x,y)dxdy+\int_0^1\int^{1}_{\sqrt y} f(x,y)dxdy$$
