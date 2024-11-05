$$f_X(x)=\frac{1}{\sqrt{2\pi}\sigma}e^{\frac{-(x-\mu)^2}{2\sigma^2}}$$
# The corresponding CDF is given by: $$F_X(x)=\int_{-\infty}^x\frac{1}{\sqrt{2\pi}\sigma}e^{\frac{-(u-\mu)^2}{2\sigma^2}}du$$
- We can approximate $P[X=C]$ via $$\lim_{\Delta x\to0}P[C\leq X\leq C+\Delta x]$$
- And then get the area by approximating via a perfect rectangle: $f_X(C)\cdot \Delta x$

# We can mix these Gaussians
- must ensure that the area under remains 1
![[Pasted image 20241003114903.png]]

# [[Entropy and Uncertainty]] For a Gaussian
- Looking at Differential Entropy
$$H[X]=E[-\ln f_X(x)]=E[-\ln(\frac{1}{\sqrt{2\pi}\sigma}e^{\frac{-(x-\mu)^2}{2\sigma^2}})]=\ln({\sqrt{2\pi}\sigma})-E[\frac{-(x-\mu)^2}{2\sigma^2}]$$Finally, via some clever manipulation: 
# $$H[X]=\frac{1}{2}\ln(2\pi\sigma^2e)$$
$$\text{Differential Entropy}$$