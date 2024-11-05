# $$y(t)=(h*x)(t)=\int_{-\infty}^\infty h(t-\tau)x(\tau)d\tau$$
# Observe
- Not a pointwise operation, $\forall t\in\mathbb{R}$ we have that $y(t)\!\perp\!\!\!\perp x(t), h(t)$.
- Computing $y(t)$ can be thought about as follows:
	- time-reversal of $h$
	- shifting result forward by $t$ seconds
	- pointwise multiplication of this signal with $x$
	- integration finally over all possible $\tau$