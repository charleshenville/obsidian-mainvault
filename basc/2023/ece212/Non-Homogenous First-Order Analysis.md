## Presented with the Non-[[Homogenous Linear DEs]]:
$$\frac{dy}{dt}+\frac{y}{\tau}=\frac{E}{\tau}$$
To find solutions to this [[Ordinary Differential Equations]] we note the following with [[First-Order Analysis]]:
$$\int_{0}^{t}\frac{d}{dt}(e^{\frac{t}{\tau}}y)dt=\int_0^t\frac{E}{\tau}e^{\frac{t}{\tau}}dt$$
We get the solution:
$$y(t)=y(0)e^{-\frac{t}{\tau}}+E(1-e^{-\frac{t}{\tau}})$$
Where $E$ is a DC Source; Represents $\lim\limits_{t\to\infty}y(t)=y(\infty)$.
$$y(t)=y(\infty)+(y(0_+)-y(\infty))e^{-\frac{t}{\tau}}$$
We can also just just the [[Step-by-step Approach]].


