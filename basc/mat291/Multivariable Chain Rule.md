## We can consider the following two cases to Obtain the derivative of a function in terms of every [[Partial Derivative]]:

### Case 1
$$t \to_f(x,y)\to_g z$$

|$f:\mathbb{R}\to\mathbb{R}^2$|$g:\mathbb{R}^2\to\mathbb{R}$|$h:\mathbb{R}\to\mathbb{R}$|
|-|-|-|

$$h(t)=g(f(t))=(g\circ f)(t)=g(x(t), y(t))$$
$$h'(t)=\frac{dh}{dt}=\frac{\partial h}{\partial x}\frac{dx}{dt}+\frac{\partial h}{\partial y}\frac{dy}{dt}$$
### Case 2
$$(s,t) \to_f(x,y)\to_g z$$

|$f:\mathbb{R}^2\to\mathbb{R}^2$|$g:\mathbb{R}^2\to\mathbb{R}$|$h:\mathbb{R}^2\to\mathbb{R}$|
|-|-|-|

$$h(s,t)=g(f(s,t))=(g\circ f)(s,t)=g(x(s,t), y(s,t))$$
$$\frac{\partial h}{\partial s}=\frac{\partial h}{\partial x}\frac{\partial x}{\partial s}+\frac{\partial h}{\partial y}\frac{\partial y}{\partial s}$$
$$\frac{\partial h}{\partial t}=\frac{\partial h}{\partial x}\frac{\partial x}{\partial t}+\frac{\partial h}{\partial y}\frac{\partial y}{\partial t}$$
