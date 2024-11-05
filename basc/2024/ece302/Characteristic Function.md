# Characteristic Function with [[Continuous Time Fourier Transform]] $$\Phi_X(\omega)=E[e^{j\omega X}]=\int_{-\infty}^\infty e^{j\omega X} f_X(x)dx$$ $$f_X(x)=\frac{1}{2\pi}\int_{-\infty}^\infty e^{-j\omega X} \Phi_X(\omega)d\omega$$
# For [[Discrete Time Fourier Transform]]: $$\Phi_X(\omega)=E[e^{j\omega X}]=\sum_{-\infty}^\infty e^{j\omega X} P_X(x)$$$$f_X(x)=\frac{1}{2\pi}\int_{0}^{2\pi} e^{-j\omega X} \Phi_X(\omega)d\omega$$
$$\frac{d\Phi_X(\omega)}{d\omega}=E[jXe^{j\omega X}]$$ Where $E[X]=\frac{1}{j}\frac{d\Phi_X(\omega)}{d\omega}|_{\omega=0}$ and 
# $$E[x^n]=\frac{1}{j^n}\frac{d^n\Phi_X(\omega)}{d\omega^n}|_{\omega=0}$$
# For a Geometric RV:$$\Phi_X(\omega)=\frac{p}{e^{-j\omega}-(1-p)}$$ $$E[x]=\frac{1}{p}$$
# For an Exponential RV: $$\Phi_X(\omega)=\frac{\lambda}{\lambda-j\omega}$$$$E[X]=\frac{1}{j}\frac{d\Phi_X(\omega)}{d\omega}|_{\omega=0}=\frac{1}{\lambda}$$
# For a Gaussian RV:$$\Phi_X(\omega)=\exp(j\omega\mu-\omega^2\sigma^2\frac{1}{2})\to E[x]=\mu=m$$
