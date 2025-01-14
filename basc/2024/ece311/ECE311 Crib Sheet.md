## Model Types
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
## Canonical SSM Forms
$$\dot{x} = \begin{bmatrix} 0 & 1 & 0 & \cdots & 0 \\ 0 & 0 & 1 & \cdots & 0 \\ 0 & 0 & 0 & \cdots & 1 \\ -a_0 & -a_1 & -a_2 & \cdots & -a_{n-1} \end{bmatrix} x + \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 1 \end{bmatrix} u$$
$$y(t)=[b_0\space b_1\space\cdots\space b_m\space0\space0\space0\cdots^{n-m+1\text{ times}}]\textbf{x}$$
$$\dot x_n=u(t)-a_0v-\cdots- a_n\frac{d^nv}{dt^{n}}$$
## Linearization Example$$\Delta y = A\Delta x\to A= f'(x_0)=\begin{bmatrix}\frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} & \frac{\partial f_1}{\partial x_3}\\\frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} & \frac{\partial f_2}{\partial x_3}\end{bmatrix}|_{x_0}$$
## Transfer Function$$G(s)=\frac{Y(s)}{U(s)}=\frac{b_ms^m+\cdots+b_0}{a_ns^n+\cdots+a_0}$$$$G(s)=\frac{N(s)}{D(s)}=C(sI-A)^{-1}B+D$$$$(sI-A)^{-1}=\frac{1}{\det(sI-A)}\text{adj}(sI-A)$$$$\det(sI-A)=D(s)$$
## Time-Invariance; $x_\tau(t)=x(t)-\tau$ iff:$$y=T\{x\},\space y_\tau=T\{x_\tau\}\space\forall\space\tau\in\mathbb{R}$$
## Adjugate
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
## Useful Trig Identities
$$\begin{matrix}
\sin(a)\sin(b)=\frac{1}{2}(\cos(a-b)-\cos(a+b)) \\
\cos(a)\cos(b)=\frac{1}{2}(\cos(a-b)+\cos(a+b)) \\
\cos(a)\cos(b)=\frac{1}{2}(\sin(a+b)+\sin(a-b)) \\
\sin(a\pm b)=\sin(a)\cos(b)\pm\cos(a)\sin(b) \\
\cos(a\pm b)=\cos(a)\cos(b)\mp\sin(a)\sin(b) \\
\sin^2(t)=\frac{1}{2}(1-\cos(2t)),\space \cos^2(t)=\frac{1}{2}(1+\cos(2t)), \space\sin(2t)=2\sin(t)\cos(t) \\
e^{j\theta}=\cos\theta+j\sin\theta\to\sin\theta=\frac{e^{j\theta}-e^{-j\theta}}{2j}\to\cos\theta=\frac{e^{j\theta}+e^{-j\theta}}{2}
\end{matrix}$$
## Laplace And Residue
$$f(t)=\sum_{i=1}^n\text{Res}[F(s)e^{st},s=p_i]$$$$\text{Res}(F(s),s_0)=\frac{1}{(r-1)!}\frac{d^{r-1}}{ds^{r-1}}[F(s)]$$$$\mathcal{L}\{e^{At}\}=(sI-A)^{-1}$$![[Pasted image 20231018222732.png]]
## Basic Control Problem (BCP)
![[IMG_6A8B09ED77C9-1 1.jpeg]]
$$\begin{bmatrix}
E(s) \\
U(s) \\
Y(s)
\end{bmatrix}
=
\begin{bmatrix}
\frac{1}{1 + CG} & -\frac{G}{1 + CG} \\
\frac{C}{1 + CG} & \frac{1}{1 + CG} \\
\frac{CG}{1 + CG} & \frac{1}{1 + CG}
\end{bmatrix}
\begin{bmatrix}
R(s) \\
D(s)
\end{bmatrix}
$$
$$E(s)=R(s)-Y(s)$$
$$E(s)=\frac{R(s)}{1+C(s)G(s)}_{\text{no D(s)}}=\frac{R(s)-G(s)D(s)}{1+C(s)G(s)}$$
## Usual Controllers, $C(s)\to$ Proportional: $K$.   Integral: $\frac{K}{s}$.   Derivative: $Ks$ Combined in parallel usually
![[Pasted image 20241118135203.png]]
![[Pasted image 20241118135219.png]]
## Time Response
$$Y(s)=\frac{\omega_n^2}{s^2+2\zeta\omega_ns+\omega_n^2}$$
$$T_r=\frac{1.8}{\omega_n},\quad T_s=\frac{4}{\zeta\omega_n},
\quad\text{\%OS}=\exp\left(\frac{\zeta\pi}{\sqrt{1-\zeta^2}}\right),\quad\zeta=\frac{-\ln(\text{\%OS})}{\sqrt{\pi^2+\ln^2(\text{\%OS})}}$$
## Complex Region Analytics in Controller Design and Poles
$$s=-\sigma+j\omega_d=-\zeta\omega_n+j\omega_n\sqrt{1-\zeta^2}=\omega_ne^{j\theta}$$$$\theta=\arccos(\zeta)=\arcsin(\omega_n\sqrt{1-\zeta^2})$$
## Controller Design for 2nd Order Systems
$$PM_{L_O}=\arctan\frac{2\zeta}{\sqrt{-2\zeta^2+\sqrt{1+4\zeta^4}}}$$
![[Pasted image 20241219221552.png]]
## Initial/Final Value Theorem: 
$$\lim\limits_{t\to0^+}f(t)=\lim\limits_{s\to\infty}sF(s),\quad\lim\limits_{t\to\infty}f(t)=\lim\limits_{s\to0}sF(s)$$

## Routh Array: BIBO Stability / Polynomial roots $\in\text{OLHP}=\{s\in\mathbb{C}:\Re(s)<0\}$?
$$a(s)=s^n+a_{n-1}s^{n-1}+\cdots+a_1s+a_0$$
$$\downarrow$$
$$\begin{matrix}
s^n & 1& a_{n-2}& a_{n-4}&\cdots&0 \\
s^{n-1} & a_{n-1}& a_{n-3}& a_{n-5}&\cdots&0 \\
s^{n-2} & b_1& b_{2}& b_{3}&\cdots&0 \\
s^{n-3} & c_1& c_{2}& c_{3}&\cdots&0 \\
\vdots &\vdots &\vdots &\vdots &\ddots&\vdots \\
s^1 & y_1& y_{2}& 0&\cdots&0 \\
s^0 & z_1& 0& 0&\cdots&0 \\
\end{matrix}$$
$$b_1=-\frac{1}{a_{n-1}}\det\begin{pmatrix}1&a_{n-2}\\a_{n-1}&a_{n-3}\end{pmatrix};\quad b_2=-\frac{1}{a_{n-1}}\det\begin{pmatrix}1&a_{n-4}\\a_{n-1}&a_{n-5}\end{pmatrix};\quad$$$$c_1=-\frac{1}{b_1}\det\begin{pmatrix}a_{n-1}&a_{n-3}\\b_1&b_2\end{pmatrix};\quad c_2=-\frac{1}{b_1}\det\begin{pmatrix}a_{n-1}&a_{n-5}\\b_1&b_3\end{pmatrix};\quad$$
## Routh Criterion and Conclusions
- (Necc., Suffic.):  Roots $\in$ OLHP $\iff$ no sign changes in first column.
- No. sign changes = No. roots $\in$ RHP.
- If any first element $\in$ any row is zero we have roots $\in$ RHP.
- If an entire row is zero, the system has poles on the Imaginary axis.
## Nyquist Criterion
- In general, Let $n$ be the no. poles in $L(s):=P(s)C(s)\in\Re\{s\}>0$ the Closed-Loop (Feedback) system is stable $\iff$ Nyquist plot does not go through $\frac{-1}{K}+0j$ and encircles it $n$ times CCW. This interpretation is useful when we want to ensure we have 
- This is equivalent to saying $n'$ is no. poles in $L'(s):=KP(s)C(s)\in\Re\{s\}>0$ the Closed-Loop (Feedback) system is stable $\iff$ Nyquist plot does not go through $-1+0j$ and encircles it $n'$ times CCW.
## Stability Margins
![[Pasted image 20241218131252.png]]
$$\arctan(x)+\arctan(y)=\arctan(\frac{x+y}{1-xy})\quad\arctan(-x)=-\arctan(x)$$
## Internal Asymptotic Stability
- This is true $\iff$ all eigenvalues of $A$ have a negative real part.
$$\Lambda = \text{roots}\left(\det(A-\lambda I)\right)$$
## Lead Controller (Generally for when we want to get to a specific PM)$$C(s)=K\frac{Ts+1}{\alpha Ts+1}: 0<\alpha<1$$ 
## Lag Controller (Generally when we want to get a specific DC Gain)$$C(s)=\alpha\frac{Ts+1}{\alpha Ts+1}:\alpha>1$$ 
## Steps For Designing Lead/Lag Controllers
1. Find $K$
2. Determine $\Phi_\max$ necessary to obtain desired PM $$\Phi_\max = PM - PM_{\text{original }}+\text{extra margin (≈30°)}: 0<\Phi_\max<\frac{\pi}{2}$$
3. Determine $\alpha$ from $\sin(\Phi_\max)=\frac{1-\alpha}{1+\alpha}\to \alpha=\frac{1-\sin(\Phi_\max)}{1+\sin(\Phi_\max)}$ Or just choose it such that you get a pole at the decade after your $\omega_\text{crossover}$
4. Find $\omega_\max$
5. Calculate $\frac{1}{T}=\sqrt{a}\omega_\max$ or $\frac{1}{T}\leq0.1\omega_c$
6. Verify new $CG$ function
7. Check stability with [[Nyquist Criterion]] or [[Routh Stability Criterion]].
## Internal Model Principle (IMP)
- $R(s)$ and $D(s)$ are rational and strictly / properly bounded
- The Controller, $C(s)$, solves BCP iff
	- $C(s)$ makes the closed loop BIBO Stable -> [[Stability In Control Systems]]
	- $C(s)G(s)$ has poles of $R(s)$ -> [[Asymptotic Tracking]]
	- $C(s)$ has all poles of $D(s)$ -> [[Disturbance Rejection]]
## Bode Plot Guide
![[Pasted image 20241219184627.png]]
![[Pasted image 20241219211647.png]]