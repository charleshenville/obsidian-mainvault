# PE1
### [[RC Series Analysis]] and [[First-Order Analysis]]

![[Pasted image 20240114124358.png]]
![[Pasted image 20240114134523.png]]
$$\tau =RC=(10^3)(10^{-6})=1\text{ms}$$
$$V_{out}(s)=[\frac{1}{sC(\frac{1}{sC}+R)}]V_{in}(s)$$
$$V_{out}(s)=\frac{1}{s+RCs^2}$$
$$V_{out}(s)=\frac{1}{RC}\frac{1}{s}\frac{1}{s+\frac{1}{RC}}$$
$$V_{out}(s)=\frac{1}{\tau}(\frac{\tau}{s}-\frac{\tau}{s+\frac{1}{\tau}})$$
$$V_{out}(s)=\frac{1}{s}-\frac{1}{s+\frac{1}{\tau}}$$
$$V_{out}(t)=(1-e^{-\frac{t}{\tau}})u(t)$$
$$0.1=1-e^{-\frac{t_{0.1}}{\tau}}\to t_{0.1}=-\tau\ln(0.9)$$
$$t_r=-\tau\ln(0.1)+\tau\ln(0.9)=2.19\text{ms}$$
![[Pasted image 20240114134605.png]]
$$t_{rm}=2.35-0.15=2.2\text{ms}$$
# PE2
$$\text{With R=}900\Omega\text{:}$$
![[Pasted image 20240114134820.png]]
![[Pasted image 20240114134916.png]]
$$t_{rm}=2.17-0.12=2.05\text{ms}$$
