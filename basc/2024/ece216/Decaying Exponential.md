# Considering a right-sided  $x(t)=e^{-at}u(t)$:
![[Pasted image 20240226184700.png]]

## The computed spectrum from the [[Continuous Time Fourier Transform]] is as follows:
$$X(j\omega)=\int_{-\infty}^{\infty}e^{-at}u(t)e^{-j\omega t}dt=\int_0^{\infty}e^{-(a+j\omega)t}dt=\frac{1}{a+j\omega}$$
With magnitude and phase:
$$|X(\textbf{j}\omega)|=\frac{1}{\sqrt{\omega^2+a^2}}$$
$$\angle X(\textbf{j}\omega)=\tan^{-1}(\omega/a)$$
![[Pasted image 20240226192205.png]]

### Take note of the symmetry in either case. This is important for real-valued signals.

# Considering the Two-Sided $x(t)=e^{-a|t|}$:
![[Pasted image 20240226192355.png]]
## The computed spectrum from the [[Continuous Time Fourier Transform]] is as follows:
$$X(j\omega)=\int_{-\infty}^{\infty}e^{-a|t|}e^{-j\omega t}dt=\int_{-\infty}^0e^{(a-j\omega)t}dt+\int_0^{\infty}e^{-(a+j\omega)t}dt=\frac{2a}{a^2+\omega^2}$$
