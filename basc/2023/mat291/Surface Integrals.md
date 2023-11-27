We can break up [[Surfaces]] into infinitely small partitions, $dS$ and multiply by some density function: $$f(x,y,z)$$
We get [[Double Integrals]]:
$$\iint_Sf(x,y,z)dS$$
# Computing Surface Integrals over these Scalar Functions:
We have some map:
$$(u,v)\to\vec r(u,v)$$
$$dA=dudv\to dS$$
By analogy of [[Change of Variables]]:
$$dS=|\frac{∂\vec r}{∂u}\times\frac{∂\vec r}{∂v}|dudv$$
We arrive at the rather messy formula:
$$\iint_Sf(x,y,x)=\iint_\tilde Sf(x(u,v),y(u,v),z(u,v))||\frac{∂\vec r}{∂u}\times\frac{∂\vec r}{∂v}||dudv$$

Generally, $dS$ for a sphere with radius $\rho$ parameterized with [[Spherical Coordinates]] is:
$$dS=||\frac{∂\vec r}{∂\theta}\times\frac{∂\vec r}{∂\phi}||d\theta d\phi=\rho^2\sin\phi d\phi d\theta$$
Generally, $dS$ for a cylinder with radius $R$ parameterized with [[Cylindrical Coordinates]] is:$$dS=||\frac{∂\vec r}{∂\theta}\times\frac{∂\vec r}{∂z}||d\theta dz=Rd\theta dz$$
