# Three Types
- Big-O from [[Time Complexity Analysis]]
	- Upper Bound
- Big-$\Omega$
	- Lower Bound
- Big-$\Theta$
	- Exact/Tight Bound

# Guideline 
$$1<\log(n)<\sqrt{n}<n<n\log(n)<n^2<n^3<2^n<3^n<n^n$$
# Def'n: Big-Oh/O
$$f(n)=O(g(n)) \iff \exists\space c,n_0>0,n_0\in\mathbb{N} : 0\leq f(n) \leq c\cdot g(n) \space\forall\space n\geq n_0$$
![[IMG_2D698DAFA2BC-1.jpeg]]

# Def'n: Big-$\Omega$
$$f(n)=\Omega(h(n)) \iff \exists\space c,n_0>0,n_0\in\mathbb{N} : 0 \leq c\cdot h(n) \leq f(n) \space\forall\space n\geq n_0$$![[IMG_C80E0239F7A1-1.jpeg]]

# Def'n: Big-$\Theta$
$$f(n)=\Theta(g(n)) \iff \exists\space c_1, c_2>0,n_0\in\mathbb{N} :0\leq c_1\cdot g(n)\leq f(n) \leq c_2\cdot g(n) \space\forall\space n\geq n_0$$
- Connects O and $\Omega$

