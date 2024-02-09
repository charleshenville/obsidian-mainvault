# Not all periodic functions will have a defined [[Continuous Time Fourier Series]]:
### If $x$ has **finite action** i.e: $x\in L^{per}_1$, the familiar Fourier coefficients, $a_k=\frac{1}{T_0}\int_{0}^{T_0}x(t)e^{jk\omega_0t}dt$ exist and are well-defined and above all:
$$\lim\limits_{k\to\pm\infty}|a_k|=0$$

# Convergence
### Idea/Goal is to prove or determine if
$$x(t)=\lim\limits_{K\to\infty}\sum_{k=-K}^K\alpha_ke^{jk\omega_0t}$$
## We can Define, alongside [[Signal Support and Size]]:
Let $e_K = \hat x_K − x$ denote the error between the approximation and the signal $x$. We say $\hat x_K$ **converges** to $x$

**Pointwise at time $t_0 ∈ \mathbb{R}$** if $$\lim_{K→∞}e_K(t_0) = 0$$
**Uniformly (amplitude of error goes to zero)** if $$\lim_{K→∞} ||e_K||_∞ = 0$$
**In energy (energy of error goes to zero)** if $$\lim_{K→∞}||e_K||_2 = 0$$
# More on Pointwise Convergence
### Suppose some signal $x(t)\in L_1^{\text{per}}$, then
- If $x's$ derivative at time $t_0 ∈ \mathbb{R}$ displays [[Continuity]], then $\hat x_K$ -> $x$ pointwise at $t_0$.
- If the left-side limits $x(t^-_0), \frac{dx}{dt}(t^−_0)$ and the right-side limits $x(t^+_0), \frac{dx}{dt}(t^+_0)$ exist $\forall\space t ∈ \mathbb{R}$:
$$\lim_{K\to\infty}\hat x_K(t_0)=\frac{1}{2}(x(t^-_0)+x(t^+_0))$$
- If x has a derivative which is continuous everywhere, then $\hat x_K$ converges to $x$ uniformly. This would not be true for a square wave for example.

# Convergence in Energy; Parseval's Relation
### Suppose some signal $x(t)\in L_2^{\text{per}}$, then
- $\hat x_K$ converges to $x$ with increasing $K$ in energy.
- the [[Continuous Time Fourier Series]] coefficients $$\{α_k\}^∞_{k=−∞}$$ have finite energy, i.e., $α ∈ l_2$.
- the signal and the coefficients satisfy $$\frac{1}{T_0}\int_0^{T_0}|x(t)|^2dt=\sum_{k=-\infty}^{\infty}|\alpha_k|^2$$$$\frac{1}{T_0}||x||_2^2=||\alpha||_2^2$$
