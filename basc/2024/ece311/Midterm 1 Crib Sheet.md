### **Time-Invariance**; $x_\tau(t)=x(t)-\tau$ iff:$$y=T\{x\},\space y_\tau=T\{x_\tau\}\space\forall\space\tau\in\mathbb{R}$$
### Model Types
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
### Linearization (w 2x3 Jacobian)$$\Delta y = A\Delta x\to A= f'(x_0)=\begin{bmatrix}\frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} & \frac{\partial f_1}{\partial x_3}\\\frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} & \frac{\partial f_2}{\partial x_3}\end{bmatrix}|_{x_0}$$
### Transfer Function$$G(s)=\frac{Y(s)}{U(s)}=\frac{b_ms^m+\cdots+b_0}{a_ns^n+\cdots+a_0}$$$$G(s)=\frac{N(s)}{D(s)}=C(sI-A)^{-1}B+D$$$$(sI-A)^{-1}=\frac{1}{\det(sI-A)}\text{adj}(sI-A)$$$$\det(sI-A)=D(s)$$
### Adjugate
$$\begin{bmatrix} d & -b\\ -c & a \end{bmatrix}
\begin{bmatrix}
            +
            \begin{vmatrix}
                a_{22} & a_{23} \\
                a_{32} & a_{33}
            \end{vmatrix} &
            -
            \begin{vmatrix}
                a_{12} & a_{13} \\
                a_{32} & a_{33}
            \end{vmatrix} &
            +
            \begin{vmatrix}
                a_{12} & a_{13} \\
                a_{22} & a_{23} \\
            \end{vmatrix} \\[1.5em]
            -
            \begin{vmatrix}
                a_{21} & a_{23} \\
                a_{31} & a_{33}
            \end{vmatrix} &
            +
            \begin{vmatrix}
                a_{11} & a_{13} \\
                a_{31} & a_{33}
            \end{vmatrix}&
            -
            \begin{vmatrix}
                a_{11} &  a_{13} \\
                a_{21} &  a_{23}
            \end{vmatrix} \\[1.5em]
            +
            \begin{vmatrix}
                a_{21} & a_{22} \\
                a_{31} & a_{32}
            \end{vmatrix} &
            -
            \begin{vmatrix}
            a_{11} & a_{12} \\
            a_{21} & a_{22}
            \end{vmatrix} &
            +
            \begin{vmatrix}
                a_{11} & a_{12} \\
                a_{21} & a_{22}
            \end{vmatrix}
        \end{bmatrix}
$$
### Canonical SSM Forms
$$\dot{x} = \begin{bmatrix} 0 & 1 & 0 & \cdots & 0 \\ 0 & 0 & 1 & \cdots & 0 \\ 0 & 0 & 0 & \cdots & 1 \\ -a_0 & -a_1 & -a_2 & \cdots & -a_{n-1} \end{bmatrix} x + \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 1 \end{bmatrix} u$$
$$y(t)=[b_0\space b_1\space\cdots\space b_m\space0\space0\space0\cdots^{n-m+1\text{ times}}]\textbf{x}$$
$$\dot x_n=u(t)-a_0v-\cdots- a_n\frac{d^nv}{dt^{n}}$$
### Useful Trig Identities
$$\sin(a)\sin(b)=\frac{1}{2}(\cos(a-b)-\cos(a+b))$$
$$\cos(a)\cos(b)=\frac{1}{2}(\cos(a-b)+\cos(a+b))$$
$$\cos(a)\cos(b)=\frac{1}{2}(\sin(a+b)+\sin(a-b))$$
$$\sin(a\pm b)=\sin(a)\cos(b)\pm\cos(a)\sin(b)$$
$$\cos(a\pm b)=\cos(a)\cos(b)\mp\sin(a)\sin(b)$$$$\sin^2(t)=\frac{1}{2}(1-\cos(2t)),\space \cos^2(t)=\frac{1}{2}(1+\cos(2t)), \space\sin(2t)=2\sin(t)\cos(t)$$
$$e^{j\theta}=\cos\theta+j\sin\theta\to\sin\theta=\frac{e^{j\theta}-e^{-j\theta}}{2j}\to\cos\theta=\frac{e^{j\theta}+e^{-j\theta}}{2}$$
### Laplace And Residue
$$f(t)=\sum_{i=1}^n\text{Res}[F(s)e^{st},s=p_i]$$$$\text{Res}(F(s),s_0)=\frac{1}{(r-1)!}\frac{d^{r-1}}{ds^{r-1}}[F(s)]$$$$\lim_{t\to\infty}f(t)=\lim_{s\to0}sF(s)$$$$\mathcal{L}\{e^{at}\sin{bt}\}=\frac{b}{(s-a)^2+b^2}, \space\mathcal{L}\{e^{at}\cos{bt}\}=\frac{s-a}{(s-a)^2+b^2}$$
### Block Diagrams
![[IMG_D7388E9FF974-1.jpeg]]
![[Untitled Page 2.jpeg]]![[Untitled Page.jpeg]]
