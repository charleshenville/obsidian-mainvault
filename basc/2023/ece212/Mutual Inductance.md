## Self
$$V_L(t)=L\frac{di_L}{dt}=>L=\frac{\Phi}{i_L}$$
![[IMG_4893F5A91A68-1.jpeg]]

## Mutual (Two Coils)
![[IMG_83AD5E9D30F1-1.jpeg]]
![[IMG_BE4845C273AD-1.jpeg]]

## Time Domain Analysis and Dot Convention
$$V_2(t)=\frac{d\Phi_{12}}{dt}=L_{12}\frac{di_1}{dt}$$
We define; so:
$$L_{12}=L_{21}=M$$
$$V_2(t)=M\frac{di_1}{dt}$$
![[IMG_E53561D26C4C-1.jpeg]]
![[IMG_1BF53513B2B2-1.jpeg]]
If First seen end of inductor agrees in all meshes then the Mutual Inductance term is Positive. Else it is negative.
$$V_2(t)=\pm M\frac{di_1}{dt}$$
For [[AC-Steady State]]:
$$\bar V_2 = ZI =j\omega M\bar I_1$$

Power Analysis and restricting M:
$$p(t)=\frac{1}{2}L_1\frac{d(i_1^2)}{dt}+\frac{1}{2}L_2\frac{d(i_2^2)}{dt}
+M\frac{d(i_1i_2)}{dt}=\frac{d\omega}{dt}$$
$$\omega(t)=\frac{1}{2}L_1i_1^2+\frac{1}{2}L_2i_2^2\pm Mi_1i_2\geq 0$$
Via further manipulation, we get the restriction:
$$M\leq\sqrt{L_1L_2}$$
Using the Geometric Mean For the Independent Inductances.
If the above restriction applies, we can define a certain Coupling Coefficient, $\kappa$:
$$\kappa=\frac{M}{\sqrt{L_1L_2}}\leq 1$$
