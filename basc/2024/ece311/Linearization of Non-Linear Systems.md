### See [[Linear Approximation]]

![[IMG_C35151FA1170-1.jpeg]]
$$\Delta y=(\frac{df(x)}{dx})|_{x_0}^{\Delta x}$$
# For the vector case: $$\bf{y}=f(\bf{x})$$$f'(\bf{x})$ is our [[Jacobian]] Matrix.

# See this Example of a Linearization with a Jacobian Matrix:
$$y=f(x),\space x=\left(\begin{matrix}x_1\\x_2\\x_3\end{matrix}\right), \space y=\left(\begin{matrix}x_1x_2-1\\x_3^2-2x_1x_2\end{matrix}\right)$$
Then the linearization is defined as $\Delta y=A\Delta x$ where A is the Jacobian matrix $f'(x_0)$, $x_0=\left(\begin{matrix}1\\-1\\2\end{matrix}\right)$:
$$f'(x_0)=\begin{bmatrix}\frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} & \frac{\partial f_1}{\partial x_3}\\\frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} & \frac{\partial f_2}{\partial x_3}\end{bmatrix}|_{x_0}$$$$=\begin{bmatrix}x_2 & x_1 & 0 \\ -2x_3 & 0 & 2x_3-2x_1\end{bmatrix}|_{x_0}$$$$A=\begin{bmatrix}-1&1&0\\-4&0&2\end{bmatrix}$$
![[IMG_ADFE50453F45-1.jpeg]]

## More generally, when we have a state $\bf{x}\to\dim(x)=m$ and an input $\bf{u}\to\dim(u)=n$:
$$v_o=\begin{bmatrix}x_0\\u_0\end{bmatrix}\to\dim(v)=n+m$$
$$f'(v_0)=[A|B]$$$$\Delta y=f'(v_0)\Delta v=A\Delta x+B\Delta y$$
