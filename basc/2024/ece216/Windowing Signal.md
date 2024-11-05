# Example of [[Discrete Time Fourier Series]]

![[Pasted image 20240221140120.png]]

## We have
$$\alpha_0=\frac{1}{N_0}\sum_{n=-\frac{N_0-1}{2}}^{\frac{N_0-1}{2}}x[n]=\frac{1}{N_0}\sum_{n=-W}^{W}1=\frac{2W+1}{N_0}$$
## And for $k\neq0$:
$$\alpha_k=\frac{1}{N_0}\sum_{n=-\frac{N_0-1}{2}}^{\frac{N_0-1}{2}}x[n]e^{-jk\omega_0n}=\frac{1}{N_0}\sum_{m=0}^{2W}e^{-jk\omega_0 (m-W)}$$
