# Let $x(t)$ be periodic with fund. period $T_0$, $\omega_0\frac{2\pi}{T_0}$
Via [[Continuous Time Fourier Series]]:
$$x(t)=\sum_{k=-\infty}^\infty\alpha_ke^{\textbf{j}k\omega_0t}$$
Then if we apply the [[Continuous Time Fourier Transform]] to each term in the sum with the knowledge of $$\text{CTFT}\{e^{\textbf{j}\omega_0 t}\}=2\pi\delta(\omega-\omega_0)$$We attain:
$$X(\textbf{j}\omega)=2\pi\sum_{k=-\infty}^\infty\alpha_k\delta(\omega-k\omega_0)$$
## Note then, that the CTFT of a periodic signal is itself a "discrete" distribution, where we have unit impulses at multiples of the fundamental frequency, $\omega_0$.

![[Pasted image 20240226214258.png]]

# Conjugate Symmetry
## If $x(t)\in\mathbb{R}\space\forall t\in\mathbb{R}$ then:$$X(\textbf{j}\omega)^*=X(-\textbf{j}\omega)\space\forall\omega\in\mathbb{R}$$$$X(\textbf{j}\omega)=\int_{-\infty}^{\infty}x(t)^*(e^{-\textbf{j}\omega t})^*dt=\int_{-\infty}^\infty x(t)e^{\textbf{j}\omega t}=X(-\textbf{j}\omega)$$
# Multiplication -> [[Convolution Theorem]]

If $$y(t)=x(t)\tilde x(t)$$
Then:$$Y(\textbf{j}\omega)=\frac{1}{2\pi}\int_{-\infty}^\infty\tilde X(\textbf{j}\upsilon)X(\textbf{j}(\omega-\upsilon))d\upsilon$$
If:$$y(t)=\int_{-\infty}^{\infty}x(\tau)\tilde x(t-\tau)d\tau$$
Then:$$Y(\textbf{j}\omega)=X(\textbf{j}\omega)\tilde X(\textbf{j}\omega)$$
