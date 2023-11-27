## We can employ [[Change of Variables]] to allow for translation of integrals to Polar Coordinates:
$$(x,y)\to(rcos\theta,rsin\theta)$$
$$\iint_Rf(x,y)dxdy=\iint_\tilde{R}f(r,\theta)|\det(
\begin{bmatrix} 
\frac{\partial x}{\partial r} \frac{\partial x}{\partial \theta} \\ \frac{\partial y}{\partial r} \frac{\partial y}{\partial\theta}
\end{bmatrix}
)|drd\theta$$
Finally, computing the determinant ($r$):
$$\iint_Rf(x,y)dxdy=\iint_\tilde{R}f(r,\theta)rdrd\theta$$
$$dA=rdrd\theta=rd\theta dr$$
