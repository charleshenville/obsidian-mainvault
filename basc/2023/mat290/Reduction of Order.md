## For solving Second-Order Linear Homogenous [[Ordinary Differential Equations]]:

1. Put into standard form $\to y''+P(x)y'+Q(x)y=0$
2. Observe the zeros of $P(x), Q(x)$.
3. Using a known solution, $y_1(x)$, for $x\in I$, we can reduce the DE into a First-Order one by expressing: $y_2(x)=u(x)y_1(x)$.
4. Second solution is given by: 
$$y_2(x)=y_1(x)\int\frac{e^{-\int P(x)dx}}{y_1^2(x)}dx$$