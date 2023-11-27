We can use integrate over a set we divide into infinitely small pieces with size of $dA$, $ds$, $dS$, etc.

## Integrating over scalar [[Curves and Paths]]:
- We partition into sizes, $ds$ and sample a linear density function:
![[IMG_C60091EED40D-1.jpeg]]
$$\int_Cf(x,y)ds$$
## Computing:
- Parameterize C
- Compute $ds$:$$ds=\sqrt{x'(t)^2+y'(t)^2}dt=\sqrt{dx^2+dy^2}$$
We have:
$$\int_Cf(x,y)ds=\int_a^bf(x(t),y(t))\sqrt{x'(t)^2+y'(t)^2}dt$$
![[IMG_C74B87A574FF-1.jpeg]]

## Fundamental Line Integral Theorem:

When given $C$ a curve with starting point $\vec p$ and ending point $\vec q$:
$$\int_C\nabla f\cdot d\vec r=f(\vec p)-f(\vec q)$$
But this is only relevant when $\vec F=\nabla f$ while computing $\int_C\vec F\cdot d\vec r$.
if curve is closed, $\vec p = \vec q$ and so:
$$\oint_C\nabla f\cdot d\vec r=0$$