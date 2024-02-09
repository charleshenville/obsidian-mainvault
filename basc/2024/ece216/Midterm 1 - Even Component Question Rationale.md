
### Given the signal:
$$x(t)=\cos(6\pi t)u(t)$$
Where, according to our definition in ECE216:
$$u(t)=\begin{cases}1 \text{ for }t≥0\\0\text{ otherwise}\end{cases}$$
We have $$x_{even}(t)=\frac{x(t)+x(-t)}{2}$$
$$x_{even}(t)=\frac{\cos(6\pi t)u(t)+\cos(-6\pi t)u(-t)}{2}$$$$x_{even}(t)=\frac{\cos(6\pi t)u(t)+\cos(6\pi t)u(-t)}{2}$$$$x_{even}(t)=\cos(6\pi t)(\frac{u(t)+u(-t)}{2})$$


### Observe that this will give us the following signal:
![[Pasted image 20240208191017.png]]

Represented by:
$$x_{even}(t)=\begin{cases}\frac{2}{2}\cos(0)=1\text{ for }t=0\\\frac{1}{2}\cos(6\pi t)\text{ otherwise}\end{cases}$$
Since at $t=0$ we have both unit step functions "activated" and only one "activated" everywhere else.
And we can clearly see that, for $t_0=0$:
$$x_{even}(t_0)\neq x_{even}(t_0+\frac{k}{3})\space \forall \space k\in\mathbb{Z}$$
Thus, it may not be entirely correct to say that $x_{even}(t)$ is periodic. Note that if we had defined $u(t)=\frac{1}{2}$ for $t=0$ in particular, this would have resulted in a periodic $x_{even}(t)$.