[[Ray Tracing]] is useful here - we represent light as distinct waves with an $\vec E$ and $\vec H$ component ([[Electric Field]], [[Divergence Operator]])
- We will use [[Continuous Time Fourier Transform]] and [[Maxwell's Equations]]
Mathematical Representation of [[Plane Waves]]: $${\bf E}({\bf r}, t)={\bf E_o}\cos(\omega t\pm{\bf k \cdot r}+\phi)$$$${\bf E}({\bf r}, t)={\bf E_o}\exp(i(\omega t\pm{\bf k \cdot r}+\phi))$$
Where: 
- ${\bf E_o}$ is the polarization vector and its magnitude the amplitude of oscillation.
- $\bf k$ is the propagation vector/constant and its magnitude is related to spatial frequency.

$$\frac{\omega}{k} = \frac{c}{n} \quad \omega = 2\pi\nu \quad k = \frac{2\pi n}{\lambda} \frac{|\mathbf{E}|}{|\mathbf{H}|} = \sqrt{\frac{\mu}{\varepsilon}} $$
### Irradiance $$ I = \frac{1}{2} c \epsilon_0 n |\mathbf{E}|^2 \quad \text{(for linear polarization)} $$
