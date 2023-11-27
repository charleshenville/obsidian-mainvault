We have a rule for [[Laplace Transform]]s of a function's derivative:
$$\mathcal{L}\{\frac{dy}{dt}\}=\int_0^\infty e^{-st}\frac{dy}{dt}dt$$
Employing [[Integration By Parts]] on this Transform, we eventually Obtain:
$$\mathcal{L}\{\frac{dy}{dt}\}=\mathcal{L}\{y'\}=sY(s)-y(0)$$
Moreover, we can generalize to:
$$\mathcal{L}\{f^{(n)}\}=s^nF(s)-s^{n-1}f(0)-s^{(n-2)}f'(0)-\dots-s^0f^{(n-1)}(0)$$