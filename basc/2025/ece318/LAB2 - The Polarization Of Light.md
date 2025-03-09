# Charles Henville (1009293694)
# Preparation
1. The polarization state of light refers to the direction of the electric field oscillation.  We can have light that is linearly or circularly polarized for example.
![[Pasted image 20250210213946.png]]
2. A linear polarizer analyzes the polarization state of light - it has a transmission axis and when the light polarization is aligned with this, power transmission is maximized.
3. You would likely notice your surrounding to be less darker as your polarized goggles will reduce the power transmission of light that is not aligned with its transmission axis.
4. Pass linearly polarized light through goggles to determine if it is polarized or not - if you rotate your goggles and the brightness of the linearly polarized light changes we know we have a polarized pair of goggles.
5. $$\text{Extinction Ratio}=\frac{\text{Principal Transmittance (Max W)}}{\text{Minor Transmittance (Min W)}}=\frac{k_1}{k_2}$$
6. Calcite, a common birefringent material, is a material that essentially refracts twice via splitting of electromagnetic waves into perpendicular components (o and e waves). The birefringence is quantified as:$$\Delta n=n_e-n_o$$
7. A Quarter wave plate (QWP) has a fast and slow axis - when an incident ray of light with components that are both aligned with the slow and fast axes, the quarter wave plate (retarder) introduces a phase shift between these on the egress ray: $$\Delta\Phi=\Phi_s-\Phi_f=m\pi+\frac\pi2\quad(2m\pi+\pi\text{ for half wave plates (HWPs)}):m\in\mathbb{Z}$$ where $m$ is the order
8. Passing Circularly polarized light through a QWP results in linear egress light somewhere between the fast and slow axes of the QWP, however if it was random, it likely remains random and non-linear at the egress.
9. If you pass linear light through a QWP, you'll be able to generate circularly polarized light if you are not directly aligned/orthogonal to the fast axis. With a HWP, you can't generate circular polarization this way and will only end up rotation your polarization state.
10. This can be done by constructing the following (this is maximum efficiency). Illustration credit: https://ophysics.com/l3.html ![[Pasted image 20250211010353.png]]      This is supported by [[Malus' Law]]:$$I_1=I_0\cos^2\theta$$We know that the last polarizer must be at $90^o$ but to find the intermediate angle that maximizes the efficiency, we will have to use Malus' Law in cascade: $$I_2=I_1\cos^2(90-\theta)=I_0\cos^2\theta\cos^2(90-\theta)$$We can now use the first derivative test or a graphing tool to see that this is at a maximum when $\theta=45^o$. Here it is with $I_0=1$ and we can see that we've reduced irradiance by $75\%$:![[Pasted image 20250211011736.png]]
11. We can leverage the fact that a HWP acts as a rotator. We need to find an angle $\theta$ relative to the vertical light that yields horizontal light at the egress. We can split our ingress light into slow and fast axis components. $$(I_0\cos\theta) \hat s+(I_0\sin\theta) \hat f$$ Since we are dealing with a HWP, $180^o$ phase shift will be introduced between the two components at the egress. Suppose we assign $\Phi_s=0^o,\Phi_f=180^o$ (assuming $0^{\text{th}}$ order) we know we want it to have a polarization of $90^o$ at egress, so at the end the vertical components should be subtractive and the horizontal ones additive: $$\text{Vertical Magnitude: }(I_0\cos^2\theta)_s,(I_0\sin^2\theta)_f$$ we can see that under the conditions that these components are offset by a $180^o$ phase shift, they cancel out when we set theta to $45^o$ for any arbitrary $\alpha$.
 ![[Pasted image 20250211015619.png]]![[Pasted image 20250211015644.png]]
 - We can also see this holds for out additive property in the horizontal direction. To compare efficiency, this method has 100% whilst the other has 25%.
12. We could simply add a QWP to the egress of our screen at the correct $\theta$ to yield circular polarized light.
13. The Brewster angle ($\theta_B$​) is the angle where reflected light is completely polarized perpendicular to the plane of incidence. ie we have no reflection, only refraction in the case of linearly polarized light. $$\theta_B = \tan^{-1} \left(\frac{n_2}{n_1}\right)$$$n_1 = 1.0$, $n_2 = 1.5$$$\theta_B = \tan^{-1} \left(\frac{1.5}{1.0}\right)\approx56.309932474^o$$
# Part I
1. 
	1. A minimum and maximum irradiance is observable when the polarizer is rotated - this confirms that the light coming out of the laser is Linearly polarized 
	2. The irradiance is no longer variant with respect to the rotation of the polarizer after we depolarized the light first
	3. When we add another polarizer with a vertical transmission axis - the irradiance is again variant with respect to the transmission axis angle of the first polarizer in the system
2. $$P_1=0.24\text{mW}$$$$P_0=0.42\text{mW}$$$$k_1=10\log(\frac{P_1}{P_0})=-2.43\text{dB}$$$$P_2=0.005\text{mW}$$$$k_2=10\log(\frac{P_2}{P_0})=-19.243\text{dB}$$$$\text{Linear k-values should be used here: }\frac{k_1+k_2}{2}=0.292$$$$\text{Exinction Ratio, get via linear values and then take dB}=\frac{k_1}{k_2}=10\log(48)=16.81\text{dB}$$

Measured $I_0=0.43\text{mW}$

| $\theta (\text{deg})$                | 0     | 20    | 40    | 60    | 80    | 100   | 120    | 140   | 160   | 180   |
| ------------------------------------ | ----- | ----- | ----- | ----- | ----- | ----- | ------ | ----- | ----- | ----- |
| $I(\theta)$                          | 0.250 | 0.223 | 0.164 | 0.069 | 0.014 | 0.012 | 0.065  | 0.146 | 0.220 | 0.250 |
| $I(θ)/I_0$                           | 0.581 | 0.518 | 0.381 | 0.160 | 0.033 | 0.028 | 0.1512 | 0.340 | 0.512 | 0.581 |
| $Norm. I(θ)/I_0$                     | 1     | 0.892 | 0.656 | 0.276 | 0.056 | 0.048 | 0.260  | 0.584 | 0.881 | 1     |
| $\cos^2\theta$ (shown in plot below) |       |       |       |       |       |       |        |       |       |       |
![[Pasted image 20250211101031.png]]

# Part II
$$\text{Sep}=0.5\text{cm}$$
When a polarizer is placed after the beam displacer and $\theta$ is varied, we observe that the two beams vary out of phase with each-other - this is because their polarization states are not the same but they are both linear (just rotated)

# Part III
- We have measured $2\theta$ here to be $130^o$
$$f\to305^o$$
$$s\to35^o$$

| $\lambda/2$                                                               | $0^o$   | $30^o$ | $45^o$ | $60^o$ | $90^o$  |
| ------------------------------------------------------------------------- | ------- | ------ | ------ | ------ | ------- |
| Output polarization (-30 offset likely due to output polarizer inacuracy) | $-30^o$ | $30^o$ | $60^o$ | $90^o$ | $150^o$ |
|                                                                           |         |        |        |        |         |
|                                                                           |         |        |        |        |         |
|                                                                           |         |        |        |        |         |
|                                                                           |         |        |        |        |         |
$$f_1\to-25^o$$
$$s_1\to65^o$$
$$f_2\to-30^o$$
$$s_2\to60^o$$

| $\lambda/4$                                                    | $0^o$                                  | $30^o$                                      | $45^o$                                      | $90^o$                                  |     |
| -------------------------------------------------------------- | -------------------------------------- | ------------------------------------------- | ------------------------------------------- | --------------------------------------- | --- |
| Output polarization (likely due to output polarizer inacuracy) | almost linear (max 0.14mW, min 0.02mW) | Elliptical (max 0.13mW, min 0.05mW)         | Almost Circular (max 0.1mW, min 0.08mW)     | Almost Linear (max 0.18mW, min 0.005mW) |     |
| $\lambda/4$,$\lambda/4$                                        | $0^o$,$0^o$                            | $30^o$,$30^o$                               | $45^o$,$45^o$                               |                                         |     |
| Output polarization (likely due to output polarizer inacuracy) | Linear at measured vertical            | Linear with 60 degree shift in polarization | Linear with 90 degree shift in polarization |                                         |     |
