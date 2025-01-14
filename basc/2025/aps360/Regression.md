# Polynomial: $$y(x,w)=\sum_{i=0}^Mw_ix^i$$
Such that we as closely as possible minimise the loss for an expected dataset. The set of weights (coefficients) are what we are trying to deep learn here.
# Loss Functions
- Concerned with minimising square error: $$E(w)=\frac{1}{2}\sum_{n=1}^N\{y(x_n,w)-t_n\}^2$$![[Pasted image 20250114151814.png]]

# Avoiding picking a polynomial coefficient that is too high (Over-fitting)
- leverage different [[Sampling Methods]] here.
![[Pasted image 20250114152134.png]]
- The alternative here is to increase the size of the dataset to help the model generalise better.

# Regularisation $$\tilde E(w)=\frac{1}{2}\sum_{n=1}^N\{y(x_n,w)-t_n\}^2+\frac\lambda2||\vec w||^2$$$$\vec w =\begin{bmatrix}w_0\\w_1\\\vdots\\w_M\end{bmatrix},||\vec w||=\vec w^T\vec w$$
We want to choose some Regularisation rate, $\lambda$ such that our model is as general as possible
![[Pasted image 20250114152826.png]]

