# Analogous to [[Ordinary Differential Equations]] but for [[Discrete Time Systems]].

# Taking a look at LICC-DEs:
$$a_0y[k]+\dots+a_ny[k-n]=b_0x[k]+\dots+b_mx[k-m]$$
This must hold $\forall k\in\mathbb{Z}$. We can assume $a_0=1$ without loss of Generality.
$$D^ly[k]=y[k-l]$$$$Q(D)=\sum_{q=0}^n a_qD^q,\space P(D)=\sum_{p=0}^m b_pD^p$$$$Q(D)y[k]=P(D)x[k]\text{ is our }\textbf{LICC-DE}$$
![[IMG_B5196C85C481-1.jpeg]]

# If $x[n]=e^{j\omega_0n}$:$$y[n]=\sum_{k=-\infty}^\infty h[k]e^{j\omega_0 (n-k)}=[\sum_{k=-\infty}^\infty h[k]e^{-j\omega_0k}]e^{j\omega_0n}$$$$y[n]=\text{DTFT}\{h[n]\}|_{\omega=\omega_0}e^{j\omega_0n}=H(e^{j\omega_0})e^{j\omega_0n}$$$$y[n]=|H(e^{j\omega_0})|e^{j\angle H(e^{j\omega_0})}e^{j\omega_0n}$$
# DT Frequency Response:$$H(e^{j\omega})=\sum_{n=-\infty}^\infty h[n]e^{-j\omega n}$$
# Generalizing, we see that:$$y[n]=(h*x)[n]\to Y(e^{j\omega})=H(e^{j\omega})X(e^{j\omega})$$
