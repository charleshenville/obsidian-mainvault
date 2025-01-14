Recall Nyquist-Shannon from [[Bandlimited Signals]]
Usual assumptions for [[Controllers]] and their OL systems
- P(s) and C(s) are proper with at least one of them being strictly proper
- P(s)C(s) has no pole-zero cancellation in Re s > 0
- K is non-zero
# Proper Property of [[Transfer Functions]]
A transfer function is proper ==when the degree of its numerator is less than or equal to the degree of its denominator==. **Strictly Proper** $\iff$ strictly less than

# Nyquist Criterion
Defined with the closed-loop characteristic polynomial: $$1+KC(s)P(s)$$
The system at large is stable $\iff$ no polynomial zeros $\in\Re\{s\}\geq 0$
- Less generally, the criterion states that if the Nyquist Plot does not encircle -1 then the system exhibits [[Stability In Control Systems]] under the provision that the open loop transfer function does not have any poles in the RHP.

**In general, Let $n$ be the no. poles in $L(s):=P(s)C(s)\in\Re\{s\}>0$ the Closed-Loop (Feedback) system is stable $\iff$ Nyquist plot does not go through $\frac{-1}{K}+0j$ and encircles it $n$ times CCW. This interpretation is useful when we want to ensure we have 
This is equivalent to saying $n'$ is no. poles in $L'(s):=KP(s)C(s)\in\Re\{s\}>0$ the Closed-Loop (Feedback) system is stable $\iff$ Nyquist plot does not go through $-1+0j$ and encircles it $n'$ times CCW.**

To evaluate the stability, the following identities come in handy: $$\arctan(x)+\arctan(y)=\arctan(\frac{x+y}{1-xy})\quad\arctan(-x)=-\arctan(x)$$
![[Pasted image 20241217143144.png]]
