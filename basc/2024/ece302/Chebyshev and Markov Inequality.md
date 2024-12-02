Looking at [[Expected Values]]:
$$E[x]=\int_0^axf_X(x)dx+\int_a^\infty xf_X(x)dx\geq \int_a^\infty xf_X(x)dx\geq \int_a^\infty af_X(x)dx\to aP[X\geq a]$$
The Inequality in question is as follows: $$P[X\geq a]\leq \frac{E[x]}{a}$$
Where X is a Non-Negative RV.

An Alternative, where we say $X=(Y-E[Y])^2$, we get the **Chebyshev inequality**:$$P[|Y-m|\geq b]\leq\frac{\text{Var}(Y)}{b^2}$$
Where Y(or anything) are [[Random Variables]].
