# Approximating Signals
## We have the rather complicated finite-duration signal:
![[Pasted image 20240131125154.png]]

## We can express $x(t)$ as a **weighted sum** of other signals as a basis
$$\hat x=\alpha_0\phi_0+\alpha_1\phi_1+\alpha_2\phi_2+\alpha_3\phi_3+\dots=\sum_k\alpha_k\phi_k$$
Where $\alpha_k\in\mathbb{C}$ and $\phi_k$ represent some "building block" signal.

# The Cosine Fourier Series
If $x(t)\in\mathbb{R}$, and is an **even** [[Continuous Time Signals]] with fundamental period $T_0$, it can be represented via this series:
$$x(t)=\frac{a_0}{2}+\sum_{k=1}^{\infty}a_k\cos(k\omega_0t),\space\omega_0=\frac{2\pi}{T_0}$$
$$a_k=\frac{2}{T_0}\int_{-\frac{T_0}{2}}^{\frac{T_0}{2}}x(t)\cos(k\omega_0t)dt,\space k\in\{0,1,2,\dots\}$$
## **Square Wave Example**
$$x_{fin}(t)=\begin{cases}1\text{ if }-\frac{\tau}{2}\leq t \leq\frac{\tau}{2}\\0\text{ else}\end{cases}$$
![[Pasted image 20240131202913.png]]

### Steps:
0. $x_{fin}$ is $T_0$ periodized as shown in the above figure
1. Compute $a_0$
$$a_0=\frac{2}{T_0}\int_{-\frac{T_0}{2}}^{\frac{T_0}{2}}x(t)dt=\frac{2}{T_0}\int_{-\frac{\tau}{2}}^{\frac{\tau}{2}}(1)dt=\frac{2\tau}{T_0}$$
2. For $k\geq1$ we compute
$$a_k=\frac{2}{T_0}\int_{-\frac{T_0}{2}}^{\frac{T_0}{2}}x(t)\cos(k\omega_0 t)dt=\frac{2}{T_0}\int_{-\frac{\tau}{2}}^{\frac{\tau}{2}}\cos(k\omega_0 t)dt=\frac{2\tau}{T_0}$$
$$a_k=\frac{2}{T_0k\omega_0}[\sin(k\omega_0 \frac{\tau}{2})+\sin(k\omega_0 \frac{\tau}{2})]$$
$$\text{With: }T_0\omega_0=T_0(2\pi f_0)=2\pi$$
$$a_k=\frac{2}{\pi k}\sin(k\omega_0 \frac{\tau}{2})$$
3. $x$ can be represented as
$$x(t)=\frac{\tau}{T_0}+\sum_{k=1}^\infty\frac{2\sin(k\omega_0 \frac{\tau}{2})}{\pi k}\cos(k\omega_0t)$$
4. If we keep only $K$ terms in the sum, we instead get the **approximation**
$$\hat x_K(t)=\frac{\tau}{T_0}+\sum_{k=1}^K\frac{2\sin(k\omega_0 \frac{\tau}{2})}{\pi k}\cos(k\omega_0t)$$
## Key Idea: We can observe that our **Approximation Quality** increases with increasing values of *K*
- **Denoted by $\hat x_K(t)$**
![[Pasted image 20240131210959.png]]
## The Frequency Domain
![[Pasted image 20240131212726.png]]
## The set $\{a_k\}_{k=0}^{\infty}$ we call the **Spectrum** of $x$.
- It represents $x(t)$ in the frequency domain.

# The Sine Fourier Series
If $x(t)\in\mathbb{R}$, and is an **odd** [[Continuous Time Signals]] with fundamental period $T_0$, it can be represented via this series:
$$x(t)=\frac{b_0}{2}+\sum_{k=1}^{\infty}b_k\sin(k\omega_0t),\space\omega_0=\frac{2\pi}{T_0}$$
$$b_k=\frac{2}{T_0}\int_{-\frac{T_0}{2}}^{\frac{T_0}{2}}x(t)\sin(k\omega_0t)dt,\space k\in\{0,1,2,\dots\}$$
# The Sine/Cosine Fourier Series
- To be used when $x(t)$ is neither **even or odd**.
$$x(t)=x_{even}(t)+x_{odd}(t)$$
$$x(t)=\frac{a_0}{2}+\sum_{k=1}^{\infty}a_k\cos(k\omega_0t),\space\omega_0=\frac{2\pi}{T_0}+\frac{b_0}{2}+\sum_{k=1}^{\infty}b_k\sin(k\omega_0t),\space\omega_0=\frac{2\pi}{T_0}$$
# The Complex Exponential Fourier Series
- To be used when $x(t)$ is neither **even or odd**, employing [[Complex Exponential Signals]].
### We will take our building blocks, $\phi_k(t)=e^{jk\omega_0t}$, representing $x$ as the familiar weighted sum:
$$\hat x(t)=\sum_{k=-\infty}^{\infty}\alpha_ke^{jk\omega_0t},\space \alpha_k\in\mathbb{C}$$
