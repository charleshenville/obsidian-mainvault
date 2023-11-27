Motivated by Physics, we have:
$$\int_C\vec F(x,y)\cdot\hat Tds$$
Where $\vec F(x,y)$ represents some force field which we integrate over, and $\hat T$ the [[Unit Tangent]] to $C$.

![[Pasted image 20231102134432.png]]

We say that:
## The Circulation of $\vec F$ over the contour/ [[Curves and Paths]], $C$ is that integral.
- A measure of how much the field "flows" with the curve.
- Flipping Orientation of the Contour results in the negation of this circulation.

$$\int_C\vec F(x,y)\cdot\hat Tds=-\int_{-C}\vec F(x,y)\cdot\hat Tds$$
Also:
$$\int_C\vec F(x,y)\cdot\hat Tds=\int_C\vec F(x,y)\cdot d\vec r=\int_CF_xdx+F_ydy+F_zdz$$ Where:
$$d\vec r=\hat Tds,\space\vec F=<F_x,F_y,F_z>,\space\vec r=<x,y,z>,\space d\vec r=<dx,dy,dz>$$
## Computing these Integrals:

Given the parameterization of $C$: $\vec r(t)=<x(t), y(t)>,\space a\leq t\leq b$

$$\hat Tds=d\vec r=<x'(t), y'(t)>dt$$
$$\int_C F(x,y)\cdot d\vec r=\int_a^bF(x(t), y(t))\cdot<x'(t), y'(t)>dt$$
