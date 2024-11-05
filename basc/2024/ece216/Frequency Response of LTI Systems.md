# Considering [[Linear Time-Invariant Systems]], $T\{x(t)\}=\int_{-\infty}^\infty h(t-\tau)x(\tau)d\tau$
- We can note that for a complex exponential input $x(t)=e^{j\omega_0 t}$ then 
$$y(t)=\int_{-\infty}^\infty h(\tau)e^{j\omega_0(t-\tau)}d\tau=[\int_{-\infty}^\infty h(\tau)e^{-j\omega_0\tau}d\tau]e^{j\omega_0 t}=[\mathcal{F}\{h\}|_{\omega=\omega_0}]e^{j\omega_0 t}$$

# Defining the Frequency Response as:$$H(\textbf{j}\omega)=\int_{-\infty}^\infty h(t)e^{-j\omega t}dt$$
$$H(j\omega)\in\mathbb{C}=|H(j\omega)|e^{j\angle H(j\omega)}$$$$x(t)=e^{j\omega_0t}\to y(t)=H(j\omega_0)e^{j\omega_0t}=|H(j\omega_0)|e^{j\angle H(j\omega_0)}e^{j\omega_0t}$$
# Observe the following properties:
i) **Eigenfunction Property**: $x(t)=e^{j\omega_0t}\to y(t)\propto e^{j\omega_0t}$
ii) **Amplitude Scaling**: Output amplitude is scaled by $|H(j\omega_0)|$
iii) **Phase Shifting**: Output phase is shifted by $\angle H(j\omega_0)$

# LTI Systems and Periodic Inputs
Using the fact that
$$x(t)=\sum_{k=-\infty}^\infty\alpha_ke^{j\omega_0t}\to X(j\omega)=2\pi\sum_{k=-\infty}^\infty\alpha_k\delta(\omega-k\omega_0)$$
We can compute the output of the LTI System as $$Y(j\omega)=H(j\omega)X(j\omega)=2\pi\sum_{k=-\infty}^\infty\alpha_kH(jk\omega_0)\delta(\omega-k\omega_0)$$$$\mathcal{F}^{-1}\to y(t)=\sum_{k=-\infty}^\infty\alpha_kH(jk\omega_0)e^{jk\omega_0t}$$
Where we used the shifting property of CT Impulses.
![[IMG_1D3E9350B87F-1.jpeg]]
