For the following circuit:
![[IMG_B66D33029BDA-1.jpeg]]
$$V_c=\{natural\space response\}+\{forced\space response\}$$
$$V_c=\{transient\space response\}+\{steady\space state\}$$
## Strategy that Avoids and Disregards Transience so we do not have to worry about solving Second-Order [[Ordinary Differential Equations]]:

# Using [[Phasors]]:
## For Resistor Elements:
$$\vec I_R=\frac{1}{R}\vec V_R$$
## For [[Capacitors]]:
- Current leads voltage by $90^\circ$. makes sense since j is a rotational operator:
$$\vec I_C=j\omega C\vec V_C$$
## For [[Inductors]]:
- Voltage leads current by $90^\circ$:
$$\vec V_L=j\omega L\vec I_L$$
## General Methodology for Analysis:
1. Convert Voltages/Currents to [[Phasors]].
2. All other elements to [[Impedance]].
3. Use DC Strategies, most often:
	- Thevenin
	- Superposition
	- Source Transformation