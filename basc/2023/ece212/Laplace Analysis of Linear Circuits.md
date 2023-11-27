Use case of [[Laplace Transform]] in Circuit analysis:
1. It takes Equations with integrals and differentials and converts it to arithmetic or algebraic operations.
2. Like a Power Series:$$\sum_{n=0}^\infty a_nx^n = g(x)$$
## Assertion:
- A [[Laplace Transform]] is essentially a form of a [[Taylor Series]].$$\sum_{n=0}^\infty a_nx^n\to\int_0^\infty f(t)(e^{-s})^tdt$$
## Initial and Final Value Theorem

Initial: $$\lim\limits_{t\to0^+}f(t)=\lim\limits_{s\to\infty}sF(s)$$
Final:
$$\lim\limits_{t\to\infty}f(t)=\lim\limits_{s\to0}sF(s)$$
We can use [[Differential Laplace Transforms]] to prove these Lemma.

Using [[Laplace Transform]] to solve a Series LR Circuit:
$$v=L\frac{di}{dt}+iR$$
$$\mathcal{L}\{v(t)\}=V(s)=L(sI(s)-i(0))+RI(s)$$
$$I(s)=\frac{V(s)}{sL+R}$$$$\frac{1}{s(sL+R)}=:PFD[\frac{1}{s(sL+R)}]$$
Practically,
$$F(s)=\frac{P(s)}{Q(s)}=K\frac{(s-z_1)(s-z_2)...(s-z_m)}{(s-p_1)(s-p_2)...(s-p_n)}$$
where $n\geq m$
Gives rise to:
## Simple Poles Method of Decomposition / Heaviside / Cover-Up (Zeros of the Denominator, $Q(s)$.):
$$F(s)=\frac{P(s)}{Q(s)}=\frac{k_0}{s-p_1}+\frac{k_1}{s-p_2}+...$$
$$k_i=F(s)(s-p_i)|_{s=p_i}$$
## Simple Complex Roots
$$F(s)=\frac{P(s)}{Q(s)}$$
$$\frac{P(s)}{Q_1(s)(s+\alpha-j\beta)(s+\alpha+j\beta)}=\frac{k_1}{s+\alpha-j\beta}+\frac{k_2^{=k_1^*}}{s+\alpha+j\beta}+\dots$$
Through some derivation, and taking the [[Inverse Laplace Transform]]:
$$f(t)=e^{-p_1t}(k_{11}+k_{12}t+\dots+\frac{k_{1r}t^{r-1}}{(r-1)!})$$
## Multiple Roots
$$F(s)=\frac{P(s)}{Q_1(s)(s+p_1)^r}$$
$$=\frac{k_{11}}{(s+p_1)}+\frac{k_{12}}{(s+p_1)^2}+\dots+\frac{k_{1(r-1)}}{(s+p_1)^{r-1}}+\frac{k_{1r}}{(s+p_1)^r}$$

## A neat relation that we can use to make translating back into the t-domain easier:
If we are given: $$H(s)=\frac{k}{s+\alpha+j\beta}+\frac{k^*}{s+\alpha-j\beta }$$
Where $k=|k|\angle\theta$
$$h(t)=\mathcal{L}^{-1}\{H(s)\}=2|k|e^{-\alpha t}\cos(\beta t+\theta)u(t)$$
