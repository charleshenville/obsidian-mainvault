### 1D Convolutions
- Observe simple [[Convolution Operator]]
### 2D Convolutions with Images ($I$) and a Kernel ($K$)$$y[m,n]=I[m,n]*K[m,n]=\sum_{j=-\infty}^\infty\sum_{i=-\infty}^\infty I[i,j]K[m-i,n-j]$$
![[Pasted image 20250130193057.png]]
![[Pasted image 20250130193115.png]]

# CNNs
- Forwards and Backwards Passes
	- Convolve Image with Kernel (now considering as weights) on the forwards pass
	- update the Kernel (weights) on the backwards pass using [[Gradient Descent]]
	- Pad the Image with Zeros to keep image sizes consistent.

### Stride
- Example with $s=2$
![[Pasted image 20250130194301.png]]

### Size of output: $$o=\left\lfloor\frac{i+2p-k}{s}\right\rfloor+1$$
### 3D Kernels
![[Pasted image 20250130194455.png]]

# Pooling and Strided Convolution
- Provides invariance to small translations in input
### Max Pooling:
![[Pasted image 20250130201221.png]]

### Average Pooling
![[Pasted image 20250130201320.png]]

### Strided Convolution
![[Pasted image 20250130201357.png]]

# LeNet
![[Pasted image 20250426174418.png]]

# AlexNet
![[Pasted image 20250426174442.png]]

