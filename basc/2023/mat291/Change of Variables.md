For [[Double Integrals]] or [[Triple Integrals]], we must scale the integrand to compensate for a linear mapping of one variable to another:
$$(x,y)=>(g_1(u,v), g_2(u,v))$$
![[IMG_796999A81946-1 1.jpeg]]
We can note that we can scale by the determinant of the [[Jacobian]]:
$$\iint_Rf(x,y)dxdy=\iint_Tf(u,v)|\det(J_g)|dudv$$
Where:
$$J_g=\begin{bmatrix} 
\frac{\partial g_1}{\partial u} \frac{\partial g_1}{\partial v} \\ \frac{\partial g_2}{\partial u} \frac{\partial g_2}{\partial v}
\end{bmatrix}$$

## Triple change:
$$(s,t,u)\to(x,y,z)$$
$$\iiint_Rf(x,y,z)dxdydz=\iiint_\tilde{R}f(s,t,u)|\det(J_g)|dsdtdu$$
$$\iiint_Rf(x,y,z)dV=\iiint_\tilde{R}f\circ g(s,t,u)dV$$
Where:
$$J_g=\begin{bmatrix} 
\frac{\partial x}{\partial s} \frac{\partial x}{\partial t} \frac{\partial x}{\partial u} \\ \frac{\partial y}{\partial s} \frac{\partial y}{\partial t} \frac{\partial y}{\partial u} \\ \frac{\partial z}{\partial s} \frac{\partial z}{\partial t} \frac{\partial z}{\partial u}
\end{bmatrix}$$
