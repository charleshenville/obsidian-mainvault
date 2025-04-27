For gauging [[Interference]].
# Michelson

| $\Delta\text{OPL}$ | $\delta$                     |
| ------------------ | ---------------------------- |
| $2d\cos\theta$     | $k\cdot\Delta\text{OPL}+\pi$ |
![[Pasted image 20250412132223.png]]
## The Center Bright Fringe Occurs Here With Order $m$ $(\cos\theta_{bt_m}=1)$:$$\delta_{bt_m}=2m\pi\quad2d\cos\theta_{bt_m}=\left(m-\frac{1}{2}\right)\lambda$$![[Pasted image 20250412133328.png]]
## Fringe Radii
$$r_{bt_m}=f\theta_{bt_m}=f\sqrt\frac{N\lambda}d$$
- Where f here is the focal length of the lens in the interferometer
## Fringe Spacing
$$\Delta r_{bt_N}=f(\theta_{bt_{N+1}}-\theta_{bt_{N}})=f\sqrt\frac{\lambda}{d}\left(\sqrt{N+1}-\sqrt N\right)$$
# Fabry-Pérot Interference & Interferometers
Using many [[Two-Beam Thin-Film Interference]]:
![[Pasted image 20250412141609.png]]
- We can bar different [[Polarization Types]] (TE/TM, assume just TE):
$$r=-r'$$
$$r^2=(r')^2=R$$
$$tt'=T=1-R$$
![[Pasted image 20250412142915.png]]
## $$\delta=\frac{2\pi}{\lambda_0}2n_fd\cos\theta_t$$
# Transmittance of the Thin-Film Structure: 
We define the total transmitted $E_t$ as the sum of everything exiting here (infinite, we can get it with the [[Fresnel Coefficients]]).
We get the following, called an **Airy Function** with the coefficient of Finesse, $F$:
$$T_{F-P}=\frac{E_t^2}{E_o^2}=\frac{1}{1+F\sin^2\left(\frac\delta2\right)},\quad F=\frac{4R}{(1-R)^2}$$
![[Pasted image 20250412143918.png]]
# Michelson vs Fabry-Pérot
![[Pasted image 20250412143944.png]]

# More on Finesse, $\mathcal{F}$
Meant to quantify resonance sharpness or narrowness of transmission peaks. Broadly defines as follows:
$$\mathcal{F} = \frac{\text{Fringe Spacing}}{\text{FWHM Fringe Width at Resonance}}$$
![[Pasted image 20250412144817.png]]
- We measure the fringe width at exactly half of it's peak value. In the case-of-interest where $\mathcal{F}>>1$:
$$\boxed{\mathcal{F}=\frac{2\pi}{\Delta\delta_{FWHM}}=\frac{2\pi}{4/\sqrt F}=\frac{\pi\sqrt{F}}{2}}$$
