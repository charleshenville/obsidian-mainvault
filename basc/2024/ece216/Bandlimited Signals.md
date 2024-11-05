# Sampling Bandlimited Signals
- $x(t)\to X(\textbf{j}\omega)$ is band limited with bandwidth $B>0$ if $X(\textbf{j}\omega)=0$ outside the interval $[-2\pi B, 2\pi B]$, having lots of low frequency content and less high frequency ones.

## [[Sampling]] a Bandlimited signal
![[Pasted image 20240305091944.png]]

### Computing $X_s(\textbf{j}\omega)$
- With the knowledge that multiplication in time is a convolution in frequency.
$$X_s(\textbf{j}\omega)=\frac{1}{2\pi}\int_{-\infty}^\infty S(\textbf{j}\nu)X(\textbf{j}(\omega-\nu))d\nu$$ $$X_s(\textbf{j}\omega)=\frac{1}{2\pi}\int_{-\infty}^\infty[\frac{2\pi}{T_s}\sum^\infty_{k=-\infty} \delta(\nu-k\omega_s)]X(\textbf{j}(\omega-\nu))d\nu$$$$X_s(\textbf{j}\omega)=\frac{1}{2\pi}\frac{2\pi}{T_s}\sum^\infty_{k=-\infty} \int_{-\infty}^\infty\delta(\nu-k\omega_s)X(\textbf{j}(\omega-\nu))d\nu$$ $$X_s(\textbf{j}\omega)=\frac{1}{T_S}\sum^\infty_{k=-\infty}X(\textbf{j}(\omega-k\omega_s))$$
Thus the spectrum of this sampled signal $x_s(t)=x(t)s(t)$ is a shifted version of the original spectrum. It is a periodized version of that spectrum with period $\omega_s$. 

## If $\omega_s\geq 4\pi B\space\to\space T_s\leq\frac{1}{2\pi B}$ : The "?" represents Sinc Interpolation.
![[Pasted image 20240305093101.png]]
## Then by the Nyquist-Shannon Sampling Theorem:
- If $x$ is sampled with sampling period $T_s$ satisfying $Ts ≤ \frac{1}{2B}$ , then $x$ can be exactly recovered from the samples.
- The Nyquist frequency is $\omega_s=4\pi B$
- For Audio Sampling, we choose a standard Nyquist frequency of $44.1\text{kHz}$

## If we do not have a sufficient $\omega_s$, see [[Bandlimited Aliasing]].