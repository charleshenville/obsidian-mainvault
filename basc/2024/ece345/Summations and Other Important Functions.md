See [[Taylor Series]]
# Arithmetic Series
$$\sum_{i=1}^{n}i=\frac{n(n+1)}{2}=\Theta(n^2)$$
# Fibonacci Numbers 
$F_0=0,\space F_1=1\space F_i=F_{i-1}+F_{i-2}$
$$F_i=\frac{\phi^i-\hat\phi^i}{\sqrt 5},\space\phi=\frac{1+\sqrt5}{2},\space\hat\phi=\frac{1-\sqrt5}{2}$$
# Geometric Series
$$\sum_{i=0}^nx^i=1+x+x^2+\dots+x^n=\frac{x^{n+1}-1}{x-1}$$
# Infinite Geometric Series
$$\sum_{i=0}^\infty x^i=\frac{1}{1-x}\iff|x|\lt1$$

### $\sum_{k=0}^\infty{kx^k}=\frac{x}{(1-x)^2}$ Can be proved by using the inf. Geo. Series formula and differentiating both sides.

# Telescoping
$$\sum_{i=1}^na^i-a^{i-1}=?$$
$=a_1-a_0+a_2-a_1+\dots+a_n-a_{n-1}=\bf{a_n-a_0}$ since everything else cancels out.

### We can leverage [[Partial Fraction Decomposition]] to get complex summations into the closed form.

# Binomial Coefficients
$$(x+y)^r=\sum_{i=0}^r(\begin{matrix}r\\ i\end{matrix})x^iy^{r-i}\space\text{where }(\begin{matrix}r\\ i\end{matrix})=\frac{r!}{(r-i)!i!}$$
