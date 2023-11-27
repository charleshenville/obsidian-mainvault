We can use [[Laplace Analysis of Linear Circuits]] in circuits that include [[Inductors]] and [[Capacitors]]:

Resistor Circuit:
![[Pasted image 20231108203835.png]]

[[Inductors]] ([[Capacitors]] are similar):
![[Pasted image 20231108203956.png]]
Using the s-domain identity for $V_L$:
$$V_L(s)=sLI(s)-Li_L(0^+)$$
$$V_L(s)=V_1(s)+V_2(s)$$
We can attain:
![[Pasted image 20231108204929.png]]

Using Source Transformation, we can attain:
![[Pasted image 20231108205030.png]]

Note we could have attained this from the equivalent s-domain transition process for $i_L(t)$ / $I_L(s)$:
$$i_L(t)=\frac{1}{L}\int_0^tv_L(t)dt+i_L(0^+)$$
$$I_L(s)=\frac{1}{sL}V_S(s)+\frac{i_L(0^+)}{s}$$

We can note that $j\omega=s$ and use our [[Impedance]] formulas to compute the s-domain equivalent circuit.