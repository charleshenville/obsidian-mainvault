# From the Complex Exponential [[Fourier Series]]:
If $x(t)\in\mathbb{R}$, a [[Continuous Time Signals]] with fundamental period $T_0$ and $\omega_0=\frac{2\pi}{T_0}$ it can be represented via the [[Fourier Series]]:
$$\hat x(t)=\sum_{k=-\infty}^{\infty}\alpha_ke^{jk\omega_0t},\space \alpha_k\in\mathbb{C}$$
$$a_k=\frac{1}{T_0}\int_0^{T_0}x(t)e^{-jk\omega_0t}dt$$
## We can note that for any $m,l\in\mathbb{Z}$ we can employ **Orthogonality**:
$$\frac{1}{T_0}
\int_0^{T_0}e^{jm\omega_0t}e^{-jl\omega_0t}dt=\begin{cases}1\text{ if }m=l\\0\text{ else}\end{cases}$$

# Fourier Coefficients of Transformed Signals with Known Fourier Coefficients
### Example with $x(t)=\sum_{k=-\infty}^{\infty}\alpha_ke^{jk\omega_0t}$ Then:
$$x(t-t_0)=\sum_{k=-\infty}^{\infty}\alpha_ke^{jk\omega_0(t-t_0)}=\sum_{k=-\infty}^{\infty}(\alpha_ke^{-jk\omega_0t_0})e^{jk\omega_0t}$$
$$\text{Our new coefficients: }\beta_k=\alpha_ke^{-jk\omega_0t_0}$$
- We can use the following **table** to extrapolate new Fourier Coefficients
![[Pasted image 20240131235519.png]]

