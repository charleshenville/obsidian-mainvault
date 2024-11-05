# The Derivative of the CDF from [[Probability Density Function]]s:
$$f_X(x)=\frac{dF_X(x)}{dx}$$
$$F_X(x)=\int_{-\infty}^xf_X(v)dv$$
Then $P[a\lt X \leq b]=\int_a^bf_X(x)dx$
- Follows by the fundamental theorem of calc that this is equal to $F_X(b)-F_X(a)$.

And: $$\int_{-\infty}^\infty f_X(x)dx=1$$ By definition.

# Laplacian Distributions$$f_x(x)=ce^{-\alpha|x|}:\alpha>0$$
Where by integrating and setting equal to one we get:
$$1=\frac{2c}{\alpha}\to c=\frac{\alpha}{2}$$
