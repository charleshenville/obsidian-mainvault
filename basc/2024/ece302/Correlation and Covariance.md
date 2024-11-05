Similar to [[Variance]] but only applicable for [[Random Variables in Multiple Dimensions]]:

# We have the $jk^\text{th}$ joint moment of X and Y defined as follows
$$E[X^j Y^k] = 
\begin{cases} 
\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} x^j y^k f_{X,Y}(x, y) \, dx \, dy, & X, Y \text{ jointly continuous} \\
\sum_i \sum_n x_i^j y_n^k p_{X,Y}(x_i, y_n), & X, Y \text{ discrete}
\end{cases}$$

The Correlation of X and Y is achieved when we have j=k=1.

# Central Moment$$E[(X-E[X])^j(Y-E[Y])^k]$$
- if we have j=2, k=0, we get $\text{VAR}(x)$ and it is similar for Y
- The Covariance is achieved when we have j=k=1
$$\text{COV}(X,Y)=E[(X-E[X])(Y-E[Y])]=E[XY]\iff \{E[X]=0\space||\space E[Y]=0\}$$$$=E[XY]-E[X]E[Y]$$
- Note Covariance is always zero if X and Y are independent of each other.

# Correlation Coefficient$$\rho_{X,Y}=\frac{\text{COV(X,Y)}}{\sigma_X\sigma_Y}$$
- $-1\leq\rho_{X,Y}\leq1$
