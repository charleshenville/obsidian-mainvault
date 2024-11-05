1. I/O Model -> nth order [[Ordinary Differential Equations]]
	- Easier -> we have [[Linear Time-Invariant Systems]]
	- Single Input, Single Output (SISO)
2. [[State-Space Model]] for [[Linear Time-Invariant Systems]]
	- $\dot x(t)=Ax(t)+Bu(t)$
	- $y(t)=Cx(t)+Du(t)$
	- $\begin{bmatrix}\dot x_1\\ \dot x_2\\\dots\\ \dot x_n\end{bmatrix}=\begin{bmatrix}a_{11}x_1+a_{12}x_2+\dots+ a_{1n}x_n\\ a_{21}x_1+a_{22}x_2+\dots+ a_{2n}x_n \\\dots\\ a_{n1}x_1+a_{n2}x_2+\dots+ a_{nn}x_n\end{bmatrix}$
3. [[State-Space Model]] for Non-[[Linear Time-Invariant Systems]]
	- $\dot x(t)=f(x,u)$
	- $\dot y(t)=h(x,u)$
	- $\begin{bmatrix}\dot x_1\\ \dot x_2\\\dots\\ \dot x_n\end{bmatrix}=\begin{bmatrix}f_1(x_1, \dots , x_n)\\ f_2(x_1, \dots , x_n)\\\dots\\ f_n(x_1, \dots , x_n)\end{bmatrix}$
