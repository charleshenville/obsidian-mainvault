# [[Linear Time-Invariant Systems]] are Invertible iff:$$\exists h_{\text{inv}}:h*h_{\text{inv}}=\delta$$
We have then: $$H(j\omega)H_{\text{{inv}}}(j\omega)=1$$
# And we can then say that **A LTI System is invertible** iff:$$H(j\omega)\neq0\space\forall\space\omega\in\mathbb{R}$$
# Invertibility of Feedback Interconnections From [[Combinations of LTI Systems]]
- Take Negative Feedback for example:
- Has impulse response of $h=(\delta+h_1*h_2)^{-1}*h_1$
- Note that $(\delta+h_1*h_2)$ is only invertible if $$1+H_1(j\omega)H_2(j\omega)\neq0\space\forall\space\omega\in\mathbb{R}$$$$\text{If above holds: }H(j\omega)=\frac{H_1(j\omega)}{1+H_1(j\omega)H_2(j\omega)}$$
