# Idea: to combine and study multiple [[Linear Time-Invariant Systems]]:

# Series Combinations:
![[Pasted image 20240324184020.png]]
Then, if $h_1, h_2$ are the corresponding impulse responses, we have, if appropriate **Associative** conditions for [[Existence of CT Convolution]] are met:$$y=h_2*\tilde x=h_2*(h_1*x)=(h_2*h_1)*x$$ Thus:
- We have an impulse response of $h_2*h_1$ for series combinations
- Using the commutative property from [[Properties of CT Convolution]], We can invert or mutate the order of the systems $T_1, T_2$ whilst getting the same $y$.

# Invertibility:
![[Pasted image 20240324184537.png]]
We have Invertibility iff, for a $T, \exists\space h_{\text{inv}}$: $$h*h_{\text{inv}}=\delta$$Consequently, $T_{\text{inv}}$ is also a LTI System.

# Parallel Combinations
![[Pasted image 20240324184942.png]]
We have:$$y=(h_1*x)+(h_2*x)=(h_1+h_2)*x$$With the impulse response:$$h=h_1+h_2$$
# Feedback Combinations
![[Pasted image 20240324185003.png]]
We have:$$y=h_1*(x-h_2*y)=h_1*x-h_1*(h_2*y)$$$$\because\delta*y=y\space \therefore(\delta+h_1*h_2)*y=h_1*x$$So, if the LTI System with $h=\delta+h_1*h_2$ is invertible, we have:$$y=h*x,\space y=(\delta+h_1*h_2)^{-1}*h_1$$
