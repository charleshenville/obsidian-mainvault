## Motivated by the [[Directional Derivative]], we have the definition:

$$\nabla f(a,b)=\space<\frac{\partial f}{\partial x}(a,b),\frac{\partial f}{\partial y}(a,b)>$$
$$\mathbb{R}^n\to \mathbb{R}^n$$
$$D_{\hat u}f = \nabla f\cdot\space\hat u=|\nabla f|\cos\theta$$
Note that this "lives" in $f$'s domain.

## Three fundamental Gradient Guidelines come from $D_{\hat u}f=|\nabla f|\cos\theta$:

1. Maximums: $\theta=0,\space\cos\theta=1$: $\nabla f$ points in the direction of maximum $D_{\hat u}f$.
2. Minimums: $\theta=\pi,\space\cos\theta=-1$: $-\nabla f$ points in the direction of minimum $D_{\hat u}f$.
3. Maximums: $\theta=\frac{\pi}{2},\space\cos\theta=0$: When $\nabla f\perp\hat u$  $D_{\hat u}f=0$; no change / rOc.

## We can now define [[Tangent Plane]] as follows:
$$L_{(a,b)}(x,y) \to \nabla f(a,b,c)\cdot(x-a,y-b,z-c)$$
Or for $f(x,y)=z$
$$z=f_x(a,b)(x-a)+f_y(a,b)(y-b)+f(a,b)$$
