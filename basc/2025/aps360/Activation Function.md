# We can't always do Linear Things
- Datasets cannot always be classified over a linear boundary in [[Artificial Neural Networks]]
![[Pasted image 20250114160049.png]]

# Heaviside (Unit Step)
[[Laplace Transform]] basis too
![[Pasted image 20250114160301.png]]$$f(x)=\begin{cases}0&x<0\\1&x\geq0\end{cases}$$
# Sign
![[Pasted image 20250114160440.png]]

# Sigmoid
- These are nice because they are differentiable and derivatives look like a Gaussian distributions with diminishing values as x strays from 0
![[Pasted image 20250114160538.png]]
Examples: $$f(x)=\tanh(x)=\frac{e^x-e^{-x}}{e^x+e^{-x}}$$$$f(x)=\frac{1}{1+e^{-x}}$$
# ReLU
$$f(x)=\max(0,x)$$![[Pasted image 20250114161224.png]]
$$\text{LeakyReLU}(x)=\begin{cases}x&x\geq0\\-ax, a>0&x<0\end{cases}$$
![[Pasted image 20250114161957.png]]$$\text{PReLU}(x)=\begin{cases}x&x\geq0\\ax, a>0&x<0\end{cases}$$
# Continuous ReLU Approximations
![[Pasted image 20250114162342.png]]
## Swish$$\text{SiLU}(x) = x \cdot \sigma(x) = \frac{x}{1 + e^{-x}}$$
## SoftPlus$$\text{SoftPlus}(x) = \frac{1}{\beta} \log\left(1 + e^{\beta x}\right)$$
