We can split closed [[Complex Contour Integrals]] into constituents when we integrate wrt the contour direction, closely related to regular [[Circulation Integrals]]:
$$\oint_C\vec F\cdot d\vec r=\oint_C\vec F\cdot \hat Tds=\oint_CPdx+Qdy$$
We can define Complex Flux integrals similarly to how we defined [[Flux Integrals]], but we can again split into constituents:
$$\oint_C\vec F\cdot\hat nds=\oint_CPdy-Qdx$$
We can also relate these to regular [[Complex Contour Integrals]] via t-parameterization, with the substitution $f(z)=u(x,y)+iv(x,y)$:
$$\text{Let: }\vec F(x,y)=<P,Q>=<u(x,y),v(x,y)>$$
$$\oint_Cf(z)dz=\oint_Cf(z(t))z'(t)dt$$
$$\oint_C \overline{f(z)}dz=\oint_CPdx+Qdy+i\oint_CPdy-Qdx$$
$$\oint_C\overline{f(z)}dz=\text{(circulation)+}i\text{(net outward flux)}$$
