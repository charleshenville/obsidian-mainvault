**Definition:** How light propagates after a modification (obstacle, modulator, aperture, etc.) to it's wavefront.
![[Pasted image 20250412165615.png]]
#### Assumptions
- Scalar $E$-field, no polarization dependence. Justified with small apertures and near normal incidences.
- **Coherent Illumination**; Coherence over the aperture region. Justified by laser illumination.
- Far-Field: $E$-distribution of interest is located far away from aperture.
- Only concerned with relative intensity.
- Field at the aperture is treated as an ensemble of secondary point sources, each emitting spherical waves.
- Field at the screen is the coherent superposition of all $E$ field contributions from the secondary point sources at the aperture.

# Fresnel-Kirchhoff Diffraction Formula
$$E_i(x_i,y_i)=\iint_{-\infty}^\infty C\frac{E_o(x_o,y_o)}{r}e^{ikr}dx_ody_o$$
![[Pasted image 20250412170624.png]]
Mapping an object, $o$ to an image, $i$ that is far $(z_i)$ away.
#### Further Assumptions In This Context: $$r=\sqrt{z_i^2+(x_i-x_o)^2+(y_i-y_o)^2}\approx z_i$$
In the Phase Context: $$r\approx z_i+\frac{x_i^2+y_i^2}{2z_i}-\frac{x_ix_o+y_iy_o}{z_i}+\frac{x_o^2+y_o^2}{2z_i}$$![[Pasted image 20250412171514.png]]

# Far Field (Fraunhofer) Condition (Further Assumption): $$k\frac{x_o^2+y_o^2}{2z_i}<<2\pi\quad\text{or}\quad z_i>>\frac{x_o^2+y_o^2}{2\lambda}$$
- Since $k=\frac{2\pi}{\lambda}$.
### To satisfy these conditions, we can do **Fraunhofer Diffraction with [[Lenses]]**:
![[Pasted image 20250412172249.png]]
The Phase difference here can be expressed as follows:
$$\phi_{BF}-\phi_{B_oF}=-k(OPL_{BF}-OPL_{B_oF})=-k\frac{(x_0^2+y_0^2)}{2f}$$
# Spatial version of [[Continuous Time Fourier Transform]] for Far-Field Diffraction: 
$$E_i(x_i,y_i)=\frac{C}{z_i}e^{ik\left(z_i+\frac{x_i^2+y_i^2}{2z_i}\right)}\iint_{-\infty}^\infty E_o(x_o,y_o)\exp\left[-ik\left(\frac{x_i}{z_i}x_o+\frac{y_i}{z_i}y_o\right)\right]dx_ody_o$$
### We can Quantify Spatial Frequencies for this: $$\begin{cases}f_x=\frac{k_x}{2\pi}=\frac{x_i}{\lambda z_i}=\frac{k\sin\theta}{2\pi}\\f_y=\frac{k_y}{2\pi}=\frac{y_i}{\lambda z_i}=\frac{k\sin\varphi}{2\pi}\end{cases}$$![[Pasted image 20250412202134.png]]
Therefore, Far-Field (Fraunhofer) Diffraction is proportional to a Fourier Transform of the Aperture Function. A lens performs the Fourier transform at its focal plane.
![[Pasted image 20250412202402.png]]

# Common Spatial Fourier Transforms
### Rectangle Function
$$\Pi(x)=\begin{cases}1&|x|\leq1/2\\0&|x|>1/2\end{cases}$$
$$\mathcal{F}\left\{\Pi(x)\right\}=\frac{\sin(\pi f)}{\pi f}\equiv \text{sinc}f$$
$$\mathcal{F}\left\{\Pi\left(\frac{x}{a}\right)\right\}=\frac{\sin(\pi f)}{\pi f}\equiv \text{sinc}f$$
![[Pasted image 20250412214439.png]]
![[Pasted image 20250412214445.png]]
### Circle Function
With the **Bessel functions ($J_n(x)$)** of the first kind.
$$\text{circ}(\rho)\equiv\begin{cases}1&\rho\leq1\\0&\rho>1\end{cases}$$
$$\mathcal{F}=\{ \text{circ}(\rho) \}=\frac{J_1(2\pi f)}f$$
![[Pasted image 20250412214526.png]]
![[Pasted image 20250412214844.png]]
### Delta Function
$$\lim_{\varepsilon\to0}\int_{-\varepsilon}^{+\varepsilon}\delta(x)dx=1$$
$$\mathcal{F}\{\delta(x)\}=1$$
$$\mathcal{F}\{\delta(x-a)\}=e^{-i2\pi fa}$$
![[Pasted image 20250412215110.png]]
$$\mathcal{F}\{g(x)⊗\delta(x-a)\}=e^{-i2\pi fa}\mathcal{F}\{g(x)\}$$
![[Pasted image 20250412215407.png]]
### Impulse Train (Shah) Function
$$Ш(x)=\sum_{n=-\infty}^\infty\delta(x-n)$$
$$\mathcal{F}\{Ш(x)\}=Ш(f)$$
$$\frac{Ш(x/a)}a\equiv\sum_{n=-\infty}^\infty\delta(x-na)$$
$$\mathcal{F}\left\{\frac{Ш(x/a)}{a}\right\}=Ш(af)$$
![[Pasted image 20250412225758.png]]

# Diffraction Limit & Resolution Power
$$2w_o\approx1.22\frac{\lambda f}{D}$$
$$\theta_{RP}\approx1.22\frac{\lambda}{D}$$
