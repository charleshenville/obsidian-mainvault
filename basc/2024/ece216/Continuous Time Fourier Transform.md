## A special case of the [[Laplace Transform]] where:
$$s=j\omega$$
We derive the following expression for the Fourier Transform by periodizing a windowed/finite duration aperiodic signal and employing the [[Fourier Series]]. with the substitution:
$$X_T(j\omega)=\int_{-T}^{T}x(t)e^{-j\omega t}dt$$ Where the CTFS coefficients, $\alpha_k$ are simply samples of it:
$$\alpha_k=\frac{1}{2T}X_T(jk\omega_0),\space k\in\{-\infty,\dots,\infty\}$$

# Main Definition is as Follows:
$$X(j\omega)=\int_{-\infty}^{\infty}x(t)e^{-jk\omega t}dt$$
**Where $X_T(j\omega)$ is the Fourier Transform, or spectrum of $x(t)$**

# Inverse CTFT (i-CTFT):
$$x(t)=\frac{1}{2\pi}\int_{-\infty}^{\infty}X(j\omega)e^{j\omega t}d\omega$$
# General principle for determining variance in the Frequency domain:
- if $x(t)$ is very concentrated in the time domain, the spectrum $X(j\omega)$ will be very spread out in the frequency domain.

### To compute i-CTFTs, we can employ a similar strategy involving [[Partial Fraction Decomposition]] similar to when we solved for [[Inverse Laplace Transform]]s.

![[Pasted image 20240226221338.png]]
