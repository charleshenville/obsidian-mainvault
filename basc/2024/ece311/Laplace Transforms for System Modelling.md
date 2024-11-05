# See The [[Laplace Transform]] as well as [[Existence of Laplace]]:

When we have poles in our s-domain functions that need to be dealt with, we can employ [[Residue Theory]]. Or [[Partial Fraction Decomposition]].

Laplace Table for this course:
![[IMG_4474EB038A05-1.jpeg]]

# Recall [[Cauchy's Integral Formula]] to solve residues:
$$\text{Res}(f,a)=\frac{1}{2\pi j}\oint_\gamma f(z)dz$$
$$\oint_C\frac{F(s)}{(s-s_0)^{n+1}}ds=\frac{2\pi j}{(r-1)!}\frac{d^{r-1}}{ds^{r-1}}[F(s)]$$
$$\oint_C\frac{f(z)}{(z-z_0)^{n+1}}dz=\frac{2\pi i\cdot f^{(n)}(z_0)}{n!}$$
# So:$$\text{Res}(F(s),s_0)=\frac{1}{(r-1)!}\frac{d^{r-1}}{ds^{r-1}}[F(s)]$$
