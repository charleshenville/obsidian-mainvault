![[Pasted image 20241023153422.png]]
$$F=\frac{i^2}{y^2}$$
$g=9.8,\space M=1Kg,\space R=3\Omega,\space L=1H$
# Prep Questions
1. State Model: $$\dot x=f(x,u)=\begin{bmatrix}x_2\\g-\frac{x_3^2}{Mx_1^2}\\\frac{R}{L}x_3-\frac{u}{L}\end{bmatrix}$$$$y=x_1$$
2. $$A=\begin{bmatrix}0&1&0\\\frac{2g}{y^*}&0&2\sqrt\frac{g}{My^{*2}}\\0&0&\frac{R}{L}\end{bmatrix}$$$$B=\begin{bmatrix}0\\0\\-\frac{1}{L}\end{bmatrix}\quad C=\begin{bmatrix}1&0&0\end{bmatrix}\quad D=\begin{bmatrix}0\end{bmatrix}$$
3. $$G(s)=\frac{2\sqrt g}{(s+3)(s^2-2g)}$$
4. $$g(t)=-\frac{1}{\sqrt g}e^{-3t}+\sqrt 2(e^{-\sqrt{2g}t}-e^{\sqrt{2g}t})$$

