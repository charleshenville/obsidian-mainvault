![[Note Sep 3, 2024.jpeg]]
# In the Discrete Case
$$E(x)=\sum_{\text{all x}}xP_X(x)$$
# And Generally:
$$E(x)=\int_{-\infty}^\infty xf_X(x)dx$$
# Example for $E(x^2)$
$$E(x^2)=\int_{-\infty}^\infty x^2f_X(x)dx$$
- Where $x^2$ represents the square of a random variable and $f_X(x)$ represents the probability density function corresponding to that random variable.

We can usually solve for these via [[Integration By Parts]]:
$$\int udv=uv-\int vdu$$
# Definition for [[Random Variables in Multiple Dimensions]]: $$E[Z=g(X,Y)]=\begin{cases}
\int_{-\infty}^\infty\int_{-\infty}^\infty g(x,y)f_{X,Y}(x,y)dxdy & X,Y\text{ jointly continuous} \\
\sum_i\sum_n g(x_i,y_n)p_{X,Y}(x_i,y_n)dxdy & X,Y \text{ discrete}
\end{cases}$$
