## For Series [[Inductors]]-R-[[Capacitors]] (LRC) Circuits:
- We establish the following set of guidelines similar to the [[Step-by-step Approach]]:
![[IMG_F887C3177F5B-1.jpeg]]
1. Finding initial conditions:$$i_L(0_-)=i_L(0_+),\space v_C(0_-)=v_C(0_+)$$
2. Finding the governing equation:$$i=C\frac{dv_c}{dt}\to v_C=\frac{1}{C}\int_{0_+}^{t}idt+v_C(0_+)$$
3. [[Mesh Analysis]] (KVL @ $i$) For $t\geq0$:$$iR+L\frac{di}{dt}+\frac{1}{C}\int_{0_+}^{t}idt+v_C(0_+)=0$$
4. Differentiate wrt $t$ and put into [[Ordinary Differential Equations]] Standard Form:$$\frac{d^2i}{dt^2}+\frac{R}{L}\frac{di}{dt}+\frac{1}{LC}i=0$$
5. Solve with the Characteristic Equation from [[Solutions to Homogenous Linear DEs]]:$$m_{1,2}=\frac{-\frac{R}{L}\pm\sqrt{\frac{R^2}{L^2}-\frac{4}{LC}}}{2}$$$$\therefore i(t)=c_1e^{m_1t}+c_2e^{m_2t}$$
6. Use 2 initial conditions to solve; In this case with the identity:$$L\frac{dI}{dt}=V_L$$
## For Parallel [[Inductors]]-R-[[Capacitors]] (LRC) Circuits:
- Similar process as before, but different [[Ordinary Differential Equations]].
![[IMG_E68957D2D2C8-1.jpeg]]
1. Derive ODE for $t\geq0$ By [[Nodal Analysis]] (KCL @ $A$):$$\frac{1}{L}\int_{0+}^{t}v_Cdt+v_C(0_+)+\frac{v_C}{R}+C\frac{dv_c}{dt}=0$$
2. Differentiate and standardize:$$\frac{d^2v_C}{dt}+\frac{1}{RC}\frac{dv_C}{dt}+\frac{v_C}{LC}=0$$
3. By Characteristic Equation and properties of [[Homogenous Linear DEs]]:$$m_{1,2}=\frac{-\frac{1}{RC}\pm\sqrt{\frac{1}{R^2C^2}-\frac{4}{LC}}}{2}$$$$\therefore i(t)=c_1e^{m_1t}+c_2e^{m_2t}$$
4. Use 2 initial conditions to solve; In this case with the identity:$$C\frac{dV}{dt}=i_C$$

