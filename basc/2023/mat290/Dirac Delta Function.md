We have the definition:
$$\delta_a(t-t_0) = 
\begin{cases}
0 & 0\leq t\leq t_0-a\\ 
\frac{1}{2a} & t_0-a\leq t\leq t_0+a \\
0 & t \geq t_0+a
\end{cases}$$
Where $a\to0$

## The Unit Area Property:
$$\delta_a(t-t_0)=\int_0^\infty \delta(t-t_0)dt=1$$
so,
$$\int_0^\infty f(t)\delta(t-t_0)dt=f(t_0)$$
We can apply this and take the [[Laplace Transform]] for $t_0=0$:
$$\mathcal{L}\{\delta(t)\}=1$$
This is beautiful.