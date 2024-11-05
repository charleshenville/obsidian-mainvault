# Transfer Function with the [[Laplace Transform]] Defined As:$$H(s)=\int_{-\infty}^\infty h(\tau)e^{s(t-\tau)}d\tau$$
# We can use [[Existence of Laplace]] to classify signals:

# Exponential Order / Class$$|x(t)|\leq Me^{\sigma t}, M>0, \sigma\in\mathbb{R}\space\forall\space t\geq0$$
We say our smallest possible $\sigma$ is:$$\sigma^*(x)$$ Which is like the sharpest bound on growth rate of $x$:

# Right-Sided [[Laplace Transform]]:
If $x$ is of exponential class, $\mathcal{R}_x=\{s\in\mathbb{C}|\text{Re}(s)>\sigma^*(x)\}$ The Laplace Transform maps this subspace:$$X(s)=\int_{0^-}^\infty x(t)e^{-st}dt$$
Where $X(s)$ is defined only for $s\in\mathcal{R}_x$ **(Region of Convergence)**
![[IMG_9CD61EEFEAD4-1.jpeg]]

# Finding [[Continuous Time Fourier Transform]]s:
- When $\text{Imaginary Axis }\in\mathcal{R}_x$: We can directly obtain the CTFT form the Laplace transform by making the substitution: $$s=\textbf{j}\omega$$
- Otherwise, we can't and it isn't even guaranteed that the CTFT Exists.!
![[IMG_FF39355B66E1-1.jpeg]]
![[IMG_6DB72A9522C7-1.jpeg]]

# For [[Linear Time-Invariant Systems]], we have:$$y(t)=h(t)*x(t)$$$$Y(s)=H(s)X(s),\space\{\mathcal{R}_h\cap\mathcal{R}_x\}\subseteq\mathcal{R}_y$$
![[IMG_4A1BC306A592-1.jpeg]]

# Transfer Function of a LTI System Defined by [[Differential Equations and CT Systems]]: $$\frac{Y(s)}{X(s)}=H(s)=\frac{P(s)}{Q(s)}$$
# Frequency Response Steady State Interpretation, Assuming $h\in L_1\therefore T \to\text{BIBO S.}$!$$|y(t)|=[\int_{-\infty}^\infty h(\tau)e^{j\omega_0(t-\tau)}u(t-\tau)d\tau]u(t)$$$$=[\int_{-\infty}^t h(\tau)e^{-j\omega_0 \tau}d\tau]e^{j\omega_0t}u(t)$$
And since $x(t) = e^{j\omega_0t}u(t)$ ,$H(j\omega_0)=\int_{-\infty}^\infty h(\tau)e^{-j\omega_0 \tau}d\tau$ 
# $$y(t)=H(j\omega_0)x(t)-F(t)x(t)$$
Where $$F(t)≜\int_{t}^\infty h(\tau)e^{-j\omega_0 \tau}d\tau$$
$$y_{\text{SS}}(t)≜H(j\omega_0)x(t)=|H(j\omega_0)|e^{j\angle H(j\omega_0)}x(t)\to\lim_{t\to\infty}[y(t)-y_{\text{SS}}(t)]=0$$
![[IMG_864FE07B3B5B-1.jpeg]]
