Using [[Interferometers]].
# Fabry-Pérot Devices
Coatings are added to [[Two-Beam Thin-Film Interference]] and Multi to increase the reflectance of the interface. This comes with the side effect of having more absorbance. We have an étalon used for filtering. The wedge structure here is used as a spectrometer.
![[Pasted image 20250412145819.png]]
New **Airy Function**:
$$T_{F-P}=\left(\frac{1-R-A}{1-R}\right)^2\frac{1}{1+F\sin^2\left(\frac\delta2\right)}$$
Where if $A$ is absorbance, by conservation rules, $$A+R+T=1$$
We also have a new phase shift $(\phi)$ that is introduced but can be neglected during the calculation of $FWHM$ (Full Width Height Maxima):
$$\delta=\frac{2\pi}{\lambda_0}2n_fd\cos\theta_t+\phi$$
![[Pasted image 20250412152702.png]]
# Fabry-Pérot Spectrometers
We have any reflections internally for the scanning type. $2\pi n_fd=m\lambda$
![[Pasted image 20250412160243.png]]
![[Pasted image 20250412153001.png]]
### Resolving Power: 
This is like the resolution of the spectrum at the end detection. Sharper=better resolution and more Finesse.
$$\mathcal{R}\equiv\frac{\lambda_0}{\Delta\lambda_{RP}}=m\mathcal{F}$$
We have $$\Delta\lambda_{RP}=\Delta\lambda_{FWHM}=\frac{2n_fd\sin\theta_{tm}\Delta\theta_{FWHM}}{m}=\frac\lambda{m\mathcal{F}}$$
### Free Spectral Range:
As $\lambda_2$ becomes sufficiently different from $\lambda_1$, the $m^{th}$ order bright fringe of $\lambda_1$ will overlap with the $(m+1)^{th}$ order bright fringe of $\lambda_2$. $\Delta\lambda_{FRS}=\lambda_1-\lambda_2$ is defined as the wavelength difference when such overlap occurs.
![[Pasted image 20250412155105.png]]
We have:
$$\Delta\lambda_{FSR}=\lambda_1-\lambda_2=\frac{\lambda_2}{m}\approx\frac{\lambda_0}{m}=\frac{\lambda_0^2}{2n_fd}$$
We also have a frequency free spectral range:
$$\Delta v_{FSR}=\frac{c}{2n_fd}$$
# We can Create a new formulation for **Finesse**: $$\mathcal{F}=\frac{\Delta\lambda_{FSR}}{\Delta\lambda_{RP}}$$


