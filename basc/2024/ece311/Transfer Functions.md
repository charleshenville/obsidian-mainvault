![[Pasted image 20241002211651.png]]

Where: 
# $$G(s)=\frac{Y(s)}{U(s)}=\frac{b_ms^m+\cdots+b_0}{a_ns^n+\cdots+a_0}=\frac{N(s)}{D(s)}$$
Only when we have zero initial conditions for $y(0), y'(0),\cdots$, else we have $$Y(s)=G(s)U(s)+\{\text{terms with }y(0), y'(0)\cdots\}$$

# Contextualization within the [[State-Space Model]]:
$$\dot x=Ax+Bu$$
$$y=Cx+Du$$
Taking $\mathcal{L}$:
$$sX(s)= AX(s)+BU(s)$$

$$Y(s)=CX(s)+DU(s)$$

Recalling that $I$ represents the identity matrix for a given $n,m$, we can say:
$$(sI-A)X(s)=BU(s)\to X(s)=(sI-A)^{-1}BU(s)$$
And finally:$$Y(s)=[C(sI-A)^{-1}B+D]U(s)$$
# $$G(s)=C(sI-A)^{-1}B+D$$
Where, with the adjoint/adjugate matrix of $sI-A$: $$(sI-A)^{-1}=\frac{1}{\det(sI-A)}\text{adj}(sI-A)$$
![[Pasted image 20241017213334.png]]
![[Pasted image 20241002213244.png]]
![[Pasted image 20241002213340.png]]

# We can define an intermediate to get to the [[State-Space Model]] from the transfer function:

![[Pasted image 20241002213655.png]]

We have that: $$V(s)=\frac{U(s)}{D(s)}=\frac{U(s)}{a_ns^n+\cdots+a_0}\to (a_ns^n+\cdots+a_0)V(s)=U(s)$$
Taking the Laplace transform and assuming zero initials:
$$(a_n\frac{d^n}{dt^n}+a_{n-1}\frac{d^{n-1}}{dt^{n-1}}+\cdots+a_0)v(t)=u(t)$$
Simplifying and making some substitutions:
$$\begin{matrix}x_1=v \\ x_2=\dot v \\ x_3=\ddot v \\ \cdots \\ x_n = \frac{d^{n-1}v}{dt^{n-1}} \\ \dot x_n = \frac{d^{n}v}{dt^{n}} \end{matrix}$$
And we have: $$\dot x_n=u(t)-a_0v-\cdots- a_n\frac{d^nv}{dt^{n}}$$
Finally: 
# $$\dot{x} = \begin{bmatrix} 0 & 1 & 0 & \cdots & 0 \\ 0 & 0 & 1 & \cdots & 0 \\ 0 & 0 & 0 & \cdots & 1 \\ -a_0 & -a_1 & -a_2 & \cdots & -a_{n-1} \end{bmatrix} x + \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 1 \end{bmatrix} u$$
And we have for $Y(s)$:
$$Y(s)=N(s)=[b_ms^m+\cdots+b_1s+b_0]V(s)$$
$$y(t)=b_m\frac{d^mv}{dt^m}+\cdots+b_0v$$
$$y(t)=[b_0\space b_1\space\cdots\space b_m\space0\space0\space0\cdots^{n-m+1\text{ times}}]x$$