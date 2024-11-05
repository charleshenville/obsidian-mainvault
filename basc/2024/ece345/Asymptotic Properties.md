### For [[Time Constraints]]:
# Transitive Property
$$f(n)=\Theta(g(n))$$$$g(n)=\Theta(h(n))$$$$f(n)=\Theta(h(n))$$
# Symmetry Property
$$f(n)=\Theta(g(n))\iff g(n)=\Theta(f(n))$$
# Transpose Property
$$f(n)=O(g(n))\iff g(n)=\Omega(f(n))$$
# Other Properties
- $n^a\in O(n^b)\iff a\leq b$
- $\log_a(n)\in O(\log_bn)\space\forall\space a,b$
- $c^n\space\in O(d^n)\iff\space c\leq d$
- If $f(n) = O(p(n)) \text{ and } g(n)=O(q(n))$
	- $f(n)g(n)=O(p(n)q(n))$
	- $f(n)+g(n)=O(\max(p(n), q(n)))$

