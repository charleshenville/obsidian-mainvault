In the context of Far-Field [[Diffraction]]:
# Single-Slit
Of dimension $b\times l$:
![[Pasted image 20250412232234.png]]
$$E_o(x_o,y_o)=\Pi\left(\frac{x_o}{b}\right)\Pi\left(\frac{y_o}{l}\right)$$
Remembering that: $$E_i(x_i,y_i)∝\mathcal{F}\{E_o(x_o,y_o)\}|_{f_x=\frac{x_i}{\lambda z_i},f_y=\frac{y_i}{\lambda z_i}}$$
With Fourier Transform with subbed value (as x and y are independent variables, we don't need [[Convolution Theorem]]):
$$bl\text{sinc}\left(\frac{bx_i}{\lambda z_i}\right)\text{sinc}\left(\frac{ly_i}{\lambda z_i}\right)$$
Since we only care about relative changes to $I$:
$$I_i(\theta,\varphi)∝E_i^2(x_i,y_i)∝\text{sinc}^2\left(\frac{kb\sin\theta}{2\pi}\right)\text{sinc}^2\left(\frac{kl\sin\varphi}{2\pi}\right)$$
![[Pasted image 20250413130051.png]]

# Double Slit
![[Pasted image 20250413130425.png]]
$$E_o(x_o,y_o)=\Pi\left(\frac{x_o}{b}\right)\Pi\left(\frac{y_o}{l}\right)*\left[\delta\left(x+\frac a2\right)+\delta\left(x-\frac a2\right)\right]$$
$$I_i(\theta,\varphi)∝\cos^2\left(\frac{ka\sin\theta}2\right)\text{sinc}^2\left(\frac{kb\sin\theta}{2\pi}\right)\text{sinc}^2\left(\frac{kl\sin\varphi}{2\pi}\right)$$
![[Pasted image 20250413130913.png]]

# Circular
![[Pasted image 20250413132125.png]]
$$E_o(\rho_o)=\text{circ}\left(\frac{\rho_o}{a}\right)$$
$$I_i(\theta)∝E_i^2(\theta)∝4\pi^2a^2\left(\frac{J_1(ka\sin\theta)}{ka\sin\theta}\right)^2∝\left(\frac{J_1(ka\sin\theta)}{ka\sin\theta}\right)^2$$
This gives us the **Airy Disk**:
![[Pasted image 20250413132937.png]]

# Multi-Slit
![[Pasted image 20250413134026.png]]
$$E_o(x_o)=\sum_{n=0}^{N-1}\delta\left(x_o-\frac{N-1}{2}a+na\right)*\Pi\left(\frac{x_o}{b}\right)$$
$$I_i(\theta)∝E_i^2(\theta)∝\frac{\sin^2\left(N\frac{ka\sin\theta}{2}\right)}{\sin^2\left(\frac{ka\sin\theta}{2}\right)}\text{sinc}^2\left(\frac{kb\sin\theta}{2\pi}\right)$$
Note that $\frac{\sin^2\left(N\frac{ka\sin\theta}{2}\right)}{\sin^2\left(\frac{ka\sin\theta}{2}\right)}$ maxes out at $N^2$ when $ka\sin\theta=2m\pi$ or $a\sin\theta=m\lambda$ and mins at $0$ when $ka\sin\theta=2(p/N)\pi \cap ka\sin\theta\neq2m\pi$ or $a\sin\theta=p\lambda/N\cap a\sin\theta\neq m\lambda$.
![[Pasted image 20250413135428.png]]
![[Pasted image 20250413135447.png]]
