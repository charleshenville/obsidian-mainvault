# You are this uncertain given the $P[A]$:$$\text{uncertainty}=\lg\frac{1}{P[A]}=-\lg P[A]$$
# We can get the average uncertainty by looking at mean/$E[x]$:$$-E[\lg P[A]]:g(x)=\lg P[A]\to-\sum_\text{all x}P_X(x)\lg P_X(x)$$ This is known as The Entropy of x, or $H[X]$:$$H[X]=-\frac{1}{\ln2}\sum_\text{all x}P_X(x)\ln (P_X(x))$$
# Entropy for Continuous [[Random Variables]]:$$H[X]=-\int_{-\infty}^\infty f_X(x)\ln f_X(x)dx-\ln(dx)\int_{-\infty}^\infty f_X(x)dx$$
## Looking at it term by term, we see: $$=\text{Differential Entropy}+\infty$$
# Entropy for Bernoulli [[Random Variables]]
![[Pasted image 20241103164326.png]]

# Quantized Continuous [[Random Variables]]
- break the sample space up into intervals of length $\Delta$ and consider the probability that X is within that interval.