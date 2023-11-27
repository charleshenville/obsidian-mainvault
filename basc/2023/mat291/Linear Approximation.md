## If we have $f: \mathbb{R}^n\to\mathbb{R}^m$ we can find a linear approximation:
$$L(\vec x)=M\vec x+\vec b$$
Where M is some $m$ x $n$ matrix.

Suppose we want to find $M,\vec b$ for an approximation of $f(\vec a)$:
$$L(\vec x)=M(\vec x-\vec a)+f(\vec a)$$
$$M=\begin{bmatrix}
    m_{11} &  m_{12} & \dots &m_{1n} \\
    m_{21} &  m_{22} & \dots &m_{2n} \\
    \vdots &  \vdots & \ddots &\vdots \\
    m_{m1} &  m_{m2} & \dots &m_{mn} \\
\end{bmatrix}$$
Making the following assumption similar to the [[Taylor Series]] in Dimension where $h_o(\vec x)$ represents some amount of higher-order terms:

$$f(\vec x)=L(\vec x)+h_o(\vec x-\vec a)$$
$$L(\vec x)=f(\vec a)+M(\vec x-\vec a) +h_o(\vec x - \vec a)$$

$$\begin{bmatrix}
f_1(\vec x)\\\vdots\\f_m(\vec x)
\end{bmatrix}
=
\begin{bmatrix}
f_1(\vec a)\\\vdots\\f_m(\vec a)
\end{bmatrix}
+
\begin{bmatrix}
    m_{11} &  m_{12} & \dots &m_{1n} \\
    m_{21} &  m_{22} & \dots &m_{2n} \\
    \vdots &  \vdots & \ddots &\vdots \\
    m_{m1} &  m_{m2} & \dots &m_{mn} \\
\end{bmatrix}
\cdot
\begin{bmatrix}
x_1-a_1\\\vdots\\\vdots\\x_n-a_n
\end{bmatrix}+h_o(\vec x-\vec a)$$
And subsequently:

$$f_m(\vec x)=f_m(\vec a)+m_{m1}(x_1-a_1)+\dots+m_{mn}(x_n-a_n)+h_o(\vec x-\vec a)$$
By taking the [[Partial Derivative]] $\frac{\partial f_m}{\partial x_n}$ of both sides and subbing $\vec x=\vec a$ we arrive at the general formula:
$$m_{ij}=\frac{\partial f_i}{\partial x_j}(\vec a)$$
Using this We can define the [[Jacobian]] and we have the formula for the Linear approximation for $f: \mathbb{R}^n\to\mathbb{R}^m$ around $\vec a$:
$$L(\vec x)=f(\vec a)+J_f\cdot(\vec x-\vec a)$$
