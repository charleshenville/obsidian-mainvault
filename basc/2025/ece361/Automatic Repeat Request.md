(ARQ) Ensuring reliable data transfer across [[High-Level Internet]]
- This is just the process of repeating lost or errored packets.
- where errored means a bit has been flipped
- We have **Acknowledgements (ACKs)** and **Negative Acknowledgements (NAKs)**.
	- That being said we can remove the need for NAKs if we include the packet number with the ACK.
![[Pasted image 20250130163642.png]]
![[Pasted image 20250130163700.png]]
- We append sequence numbers in the packet itself so that we know what we are sending.
### Detecting Time-Outs
- if $RTT\in$ [[Random Variables]] with [[Gaussian Distribution]]$$\text{Time-out time}=E[RTT]+4\sigma_{RTT}$$
# Stop-and-Wait
- NAK-free
![[Pasted image 20250130165101.png]]
- This severely limits the hardware that we can use at once because we now often idle during round trip times$$U=\frac{L/R}{L/R+RTT}$$
![[Pasted image 20250130191940.png]]
