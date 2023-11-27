## Defined as a Relatively Simple Integration Operation:
- Takes us into a different ($s$) domain.
$$\mathcal{L}\{f(t)\}=F(s)=\int_0^\infty e^{-st}f(t)dt$$
Where $s$ is defined as the [[Complex Functions]]:
$$s=\sigma+i\omega\to\omega=2\pi f$$
It follows that
$$e^{-st}=e^{-\sigma t}e^{-i\omega t}$$
We must evaluate this improper integral as a limit:
$$L\{f(t)\}=\lim\limits_{b\to\infty}\int_0^be^{-st}f(t)dt$$
Note that this is a Linear Transformation, that is:
$$L\{\alpha f(t)+\beta g(t)\}=\alpha F(s)+\beta g(s)$$
![[Pasted image 20231018222732.png]]
Note that here:
$$1=u(t)$$
Where $u(t)$ is the step (Heaviside) function.