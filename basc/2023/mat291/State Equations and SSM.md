## We have the system or Small Signal Model:

Where $x_i$ describes the state of the system at a given time, $t$.

## Output function(s) depend on State/Input variables. We have, mathematically:
$$y_i=g_i(x_1,\dots,x_n,u_1,\dots,u_m)$$
Also, assuming System variables evolve as a First-Order [[Ordinary Differential Equations]]:
$$\frac{\partial x_i}{\partial t}=f_i(x_1,\dots,x_n,u_1,\dots,u_m)$$
We can use [[Linear Approximation]] for $x_i$ or $u_i$ within a short range described by a small perturbation, $\hat u_i$, around a given Equilibrium, $U_i$:
$$u_i=U_i+\hat u_i$$
We then have by [[Linear Approximation]]:

$$\frac{dx}{dt}=f(x_1,\dots,x_n,u_1,\dots,u_m)$$
$$\frac{d\hat x}{dt}=f(\dots)+\begin{bmatrix}
    \frac{\partial f_1}{\partial x_1}(\vec a) &  \dots &\frac{\partial f_1}{\partial x_n}(\vec a) &
    \frac{\partial f_1}{\partial u_1}(\vec a) &  \dots &\frac{\partial f_1}{\partial u_n}(\vec a) 
    \\
    \vdots & \ddots &\vdots &\vdots & \ddots &\vdots 
    \\
    \frac{\partial f_m}{\partial x_1}(\vec a) & \dots &\frac{\partial f_m}{\partial x_n}(\vec a) & \frac{\partial f_m}{\partial x_1}(\vec a) & \dots &\frac{\partial f_m}{\partial x_n}(\vec a)
\end{bmatrix}\cdot
\begin{bmatrix}
x_1-X_1\\
\vdots\\
x_n-X_n\\
u_1-U_1\\
\vdots\\
u_n-U_n
\end{bmatrix}$$
But since we are evaluating this at Equilibrium, $\frac{dx}{dt}=f(x_1,\dots,x_n,u_1,\dots,u_m)=0$ and we have:
$$\frac{d\hat x}{dt}=\begin{bmatrix}
    \frac{\partial f_1}{\partial x_1}(\vec a) &  \dots &\frac{\partial f_1}{\partial x_n}(\vec a) &
    \frac{\partial f_1}{\partial u_1}(\vec a) &  \dots &\frac{\partial f_1}{\partial u_n}(\vec a) 
    \\
    \vdots & \ddots &\vdots &\vdots & \ddots &\vdots 
    \\
    \frac{\partial f_m}{\partial x_1}(\vec a) & \dots &\frac{\partial f_m}{\partial x_n}(\vec a) & \frac{\partial f_m}{\partial x_1}(\vec a) & \dots &\frac{\partial f_m}{\partial x_n}(\vec a)
\end{bmatrix}\cdot
\begin{bmatrix}
\hat x_1\\
\vdots\\
\hat x_n\\
\hat u_1\\
\vdots\\
\hat u_n\\
\end{bmatrix}$$
And by properties of matrix multiplication we get an identity in terms of smaller [[Jacobian]]s of $f$ or $g$ with respect to $\hat x$ and $\hat u$:
$$\frac{d\hat x}{dt}=J_f\hat x+B_f\hat u$$
$$\hat y=J_g\hat x+B_g\hat u$$
