![[Lecture Mosfet Feb7.pdf]]
# Channel-Length Modulation
- Increasing $V_D$ past pinching (still in saturation region) to affect out channel length directly. Note Triode region is similar to [[Diode Circuits]].
- Parameter $\lambda [\text{V}^{-1}]$ will adjust saturation region to look again like a resistor.

# Saturation DS/Overdrive Voltage relation
$$V_{DS}=V_{OV}\text{ @Saturation}$$

# Example with NMOS
$$\text{NMOS L=0.18µm W=2µm Cox=8.6}\frac{\text{fF}}{µ\text{m}^2 }\space µ_n=450\frac{cm^2}{Vs}\space V_{tn}=0.5V$$
### Q: Find $V_{GS}$ and $V_{DS}$ for $I_D=100µA$ at edge of saturation
$$V_{OV}=0.22V=V_{DS_{sat}}$$
$$V_{GS}=0.72V$$
We will oftentimes get two Quadratic results, we must select the one that lies within the correct region (according to our analysis from assumptions made at the beginning of the problem).