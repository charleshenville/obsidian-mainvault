## For the Second order [[Ordinary Differential Equations]], specifically [[Non-Homogenous Linear DEs]]:
$$L(y)=y''+P(x)y'+Q(x)y=f(x):$$
1. Determine linearly independent solutions $y_1, y_2$ of the Associated [[Homogenous Linear DEs]] ($L(y)=0$)
2. Solve for $u_1'(x), u_2'(x)$ from (First comes from thin air, second comes from subbing in $y, y', y''$ into the DE:
$$u_1'y_1+u_2'y_2=0$$
$$u_1'y_1'+u_2'y_2'=f(x)$$
Where, from Cramer's Rule:
$$u_1'=\frac
{det(\begin{bmatrix} 0 & y_2(x) \\ f(x) & y_2'(x) \\ \end{bmatrix})}
{det(\begin{bmatrix} y_1(x) & y_2(x) \\ y_1'(x) & y_2'(x) \\ \end{bmatrix})}=\frac{-y_2f}{W(y_1,y_2)}$$
$$u_2'=\frac
{det(\begin{bmatrix} y_1(x) & 0 \\ y_1'(x) & f(x) \\ \end{bmatrix})}
{det(\begin{bmatrix} y_1(x) & y_2(x) \\ y_1'(x) & y_2'(x) \\ \end{bmatrix})}=\frac{y_1f}{W(y_1,y_2)}$$

3. Use the fact that:
$$u_1(x)=-\int\frac{y_2f}{W(y_1,y_2)}dx$$

$$u_2(x)=\int\frac{y_1f}{W(y_1,y_2)}dx$$
4. We have now:
$$y_c=c_1y_1(x)+c_2y_2(x)$$
$$y_p=u_1(x)y_1(x)+u_2(x)y_2(x)$$
$$y=y_c(x)+y_p(x)$$
1. Solve the IVP with the initial conditions $y(0)=y_0$, $y'(0)=y'_0$