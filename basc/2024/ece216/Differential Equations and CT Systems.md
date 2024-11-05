# Linear, Inhomogeneous, Constant-Coefficient (LICC) [[Ordinary Differential Equations]]
- We will look at defining [[Continuous Time Systems]] with these: 
$$a_n\frac{d^ny(t)}{dt^n}+a_{n-1}\frac{d^{n-1}y(t)}{dt^{n-1}}+\dots+a_0y(t)=b_m\frac{d^mx(t)}{dt^m}+b_{m-1}\frac{d^{m-1}x(t)}{dt^{m-1}}+\dots+b_0x(t)$$$$Q(D)y(t)=P(D)x(t)$$
## $\forall t\in\mathbb{R}$:
- $x(t)$ is a CT Signal (Given)
- $y(t)$ is a CT Signal (Unknown)
- $n,m\in\mathbb{Z}:n,m\geq0$
- $\{a\}_0^n, \{b\}_0^m\subset\mathbb{R}$
- Assume $a_n = 1$ without loss of generality

# Notation:
$$D^ky(t)=\frac{d^ky(t)}{dt^k}$$$$Q(D)=a_nD^n+a_{n-1}D^{n-1}+\dots+a_1D+a_0$$$$P(D)=a_mD^m+b_{m-1}b^{m-1}+\dots+b_1D+b_0$$

# Potential Issues

i) **Multiple Solutions:** For $n=0,\space m=0$, with in: $x(t)=\delta(t), \text{i.e.}\frac{dy(t)}{dt}=\delta(t)$ We have infinitely many solutions of the form $y(t)=u(t)+C,\space C\in\mathbb{R}$. However by def'n, systems must produce just one output for each input (one-to-one).

ii) **Initial Conditions**: Example: using $t=0$ for the non-uniqueness issue. This works most of the time except in rare cases where $y(0)$ is not well defined if at all.

iii) **Causality**: We should not expect Causality since nothing in the above ODE Stipulates that $y(t)\not\!\perp\!\!\!\perp\{x(\tau)\}_{\tau\leq t}$.

# Solution for these Issues:
i) Restrict out attention to **right-sided inputs** $x(t)$
ii) Restrict out attention to **right-sided solutions** $y(t)$

# Very Important Theorem for This
- Can help us determine [[Properties of CT Systems]].
![[IMG_821E2E9D2084-1.jpeg]]

# RC Circuit Example
![[IMG_4A4D795A8D76-1.jpeg]]

We know for a fact then that a right-sided $v_s(t)$ will lead to a right-sided $v_c(t)$. 
We have via the [[Laplace Transform]] that: $$Q(s)=s+\frac{1}{RC}$$ has a root of $s=-\frac{1}{RC}$. This always has a negative real part and since 1>0 we have BIBO Stability.

# Series RLC Example
![[IMG_72701333083A-1.jpeg]]
We have roots of $$Q(s)=s^2+\frac{R}{L}s+\frac{1}{LC}$$ as $s=-\frac{R}{2L}\pm\frac{1}{2LC}\sqrt{R^2C^2-4LC}=-\frac{R}{2L}\pm\frac{R}{2L}\sqrt{1-\frac{4L}{R^2C}}$
Via a trivial analysis, we can see that we will always have a negative real component and will thus always have BIBO stability. Note that this is true besides having an imaginary component.
