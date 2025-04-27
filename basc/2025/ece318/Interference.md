We have two [[Electromagnetic Waves]] 
# For Planar
$${\bf E_1=E_{1o}}\cos({\bf k}_1\cdot{\bf r}-\omega_1t+\phi_1)$$
$${\bf E_2=E_{2o}}\cos({\bf k}_1\cdot{\bf r}-\omega_2t+\phi_1)$$
We can get the **Intensity** as follows with a time-average:
$$I_1=\langle{\bf E_1\times H_1}\rangle=\sqrt\frac{\varepsilon}{\mu}\langle{\bf E_1\cdot E_1}\rangle=\frac{1}{2}\sqrt\frac{\varepsilon}{\mu}|\bf E_{1o}|^2$$
$$I_2=\langle{\bf E_2\times H_2}\rangle=\sqrt\frac{\varepsilon}{\mu}\langle{\bf E_2\cdot E_2}\rangle=\frac{1}{2}\sqrt\frac{\varepsilon}{\mu}|\bf E_{2o}|^2$$ If these are overlapping in space, then we get a formula including an interference term at the end via the superposition of the two waves: 
### $$I=I_1+I_2+2\sqrt\frac{\varepsilon}{\mu}\langle{\bf E_1\cdot E_2}\rangle$$
# For Spherical
### $$\text{Interference term} = \sqrt{\frac{\varepsilon}{\mu}}\left(\frac{\mathbf{E}_{1o}}{r_1} \cdot \frac{\mathbf{E}_{2o}}{r_2}\right)\left\langle\cos\left[(k_1r_1-k_2r_2)-(\omega_1-\omega_2)t+(\phi_1-\phi_2)\right]\right\rangle$$
![[Pasted image 20250411163735.png]]

# Conditions for Interference
All of the following must be satisfied simultaneously.
$$(1) \quad \omega_1 = \omega_2 $$
$$(2) \quad \mathbf{E}_{1o} \perp \mathbf{E}_{2o} $$
$$
(3) \quad \phi_1 - \phi_2 \text{ is not time varying. (This is called the coherence condition.)}$$
# Generally,
$$I=I_1+I_2+2\sqrt{I_1I_2}\cos\delta$$
For Plane Waves:
$$\delta={\bf(k_1-k_2)}\cdot r+(\phi_1-\phi_2)$$
For Spherical Waves:
$$\delta=k(r_1-r_2)+(\phi_1-\phi_2)$$
Where we have terms due to the phase difference of $\Delta\text{OPL}$ and the phase difference of the source itself.

Conditions for total constructive interference (bright fringes): 
$$\delta =2m\pi, \quad I=I_1+I_2+2\sqrt{I_1I_2}$$
Conditions for total destructive interference (dark fringes): 
$$\delta =(2m+1)\pi, \quad I=I_1+I_2-2\sqrt{I_1I_2}$$
