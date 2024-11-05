# Very Similar to [[Continuous Time Systems]].$$T\{x\}[n]:\space n\in\mathbb{Z}$$
# Pointwise Definitions of DT Systems
- Giving a formula for $y[n] = T\{x\}[n]$ in terms of $\subseteq\{x[n]\}_{n\in\mathbb{Z}}$ 
- ex. $T_{\text{SQ}}\to y[n]=(x[n])^2$ or $y[n]=\text{max}\{x[n],x[n-1],x[n-2]\}$

# Recursive Definitions
- ex. $s[n]=(1+r)s[n-1]+x[n]$
- Turns into $s[n]=\sum_{k=0}^n (1+r)^{n-k}x[k]$
