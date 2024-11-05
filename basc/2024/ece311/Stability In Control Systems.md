If $\forall x(0)\in\mathbb{R}^n$, then $x(t)$ is bounded/ (all $x_i(t)$)
### Internal Stability
$$u=0\to\dot x=Ax$$
### Asymptotic Stability
- This is true iff all eigenvalues of $A$ have a negative real part.
### Input-Output Stability/ from BIBO Stability in [[Properties of CT Systems]]:$$\exists K\geq0:||y||_{\infty}\leq K||x||_\infty\space\forall\space x, y=T\{x\}$$ Where $$||x||_\infty=\max_{t\in\mathbb{R}}|x(t)|$$
# We can note that the system is unstable if at least one eigenvalues of $A$ has a positive real component. This is sufficient but not entirely necessary.
- ie can be unstable even if e have all eigenvalues $\leq0$

See Eigenvalues and [[Eigenvectors]].