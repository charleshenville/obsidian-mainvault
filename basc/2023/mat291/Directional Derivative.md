## Similar to the [[Partial Derivative]], only now we can move in any linear direction as opposed to only parallel to the x or y axis.

### Defined as follows if $\vec a = (a_1,a_2) \in \mathbb{R}^2$:
$$D_{(\hat u)}f(\vec a)=\lim\limits_{t\to0}\frac{f(\vec a+t\hat u)-f(\vec a)}{t}$$
Where $\hat u$ is a unit vector that defines a particular linear Direction.

If we take:
$$\hat u=[1,0]$$
$$D_{(\hat u)}f(\vec a)=\frac{\partial f}{\partial x}(\vec a)$$
Similarly:
$$\hat u=[0,1]$$
$$D_{(\hat u)}f(\vec a)=\frac{\partial f}{\partial y}(\vec a)$$
The [[Partial Derivative]] is a particular type of Directional Derivative.

Note that if a function displays [[Differentiability]] at $\vec a$ **ALL and ANY** Directional Derivatives must exist, including those that are Non-Linear, defined by another [[Path Function]], perhaps.

## Provided f displays [[Differentiability]] at $(a,b)$,  and $\hat u=(u_1,u_2)$:
$$D_{\hat u}f(a,b)=u_1\frac{\partial f}{\partial x}(a,b)+u_2\frac{\partial f}{\partial y}(a,b)$$
$$D_{\hat u}f(a,b)=\space<\frac{\partial f}{\partial x}(a,b),\frac{\partial f}{\partial y}(a,b)>\cdot\space\hat u$$
