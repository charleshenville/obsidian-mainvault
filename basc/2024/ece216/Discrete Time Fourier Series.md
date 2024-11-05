# Expressing as, similar to a normal [[Fourier Series]]:
$$x[n]=\sum_k\alpha_k\phi_k[n]$$
We will use [[Discrete Time Signals]] (Complex Exponentials in particular) $$\phi_k[n]=e^{jk\omega_0n}$$ Where $\omega_0=\frac{2\pi}{N_0}$. Note that the limits of our sum is **finite**.
Recalling these properties of DT Complex Exponentials: ALPHA BETA PRUNING
1. $e^{j\omega n}$ Periodic with period $N_0$ if 
$$\omega=k\frac{2\pi}{\omega_0}=k\omega_0\space \text{ for } k\in\mathbb{Z}$$
2. $2\pi$-periodic in frequency: $$e^{j(\omega+2\pi)n}=e^{j\omega n}$$ For a particular fixed k, if we increment by $N_0$:$$(k+N_0)\frac{2\pi}{N_0}=k\frac{2\pi}{N_0}+2\pi$$
### Thus, we conclude:
- For a given period $N_0$, there are only $N_0$ distinct DT Complex exponentials of period $N_0$, and they are:$$\phi_k[n]=e^{jk\omega_0n}, k\in\{0,1,2,\dots,N_0-1\}$$
## The Series can be expressed as follows:
$$x[n]=\sum_{k=0}^{N_0-1}\alpha_ke^{jk\omega_0n}, \omega_0=\frac{2\pi}{N_0}$$
# To compute our Fourier Coefficients:
- Set two sides equal and use our notion of Orthogonality to solve for $\alpha_k$

This Orthogonality notion for DT Complex exponentials:
$$\frac{1}{N_0}\sum_{n=0}^{N_0-1}e^{jm\omega_0n}e^{-jl\omega_0n}=\begin{cases}0\text{ else}\\1\text{ if }m=l+kN_0, \space k\in\mathbb{Z}\end{cases}$$
Using this to solve for the coefficients, one obtains:
$$\alpha_k=\frac{1}{N_0}\sum_{n=0}^{N_0-1}x[n]e^{-jk\omega_0n}$$ Being the coefficients in the above series: $$x[n]=\sum_{k=0}^{N_0-1}\alpha_ke^{jk\omega_0n}$$
Note that both sums are finite, and we need not integrate. It also does not matter if we take the sum from 0 to $N_0-1$ as long as we have full coverage of the period. It make be convenient in some cases to sum from $-\frac{N_0-1}{2}$ to $\frac{N_0-1}{2}$ if $N_0$ is odd.

# To solve for some of these sums we will have to employ Series Formulas. Geometric Series will prove to be especially useful:$$\sum_{k=0}^{N-1}a^k=\frac{1-a^{N-1}}{1-a}$$![[Pasted image 20240221142142.png]]