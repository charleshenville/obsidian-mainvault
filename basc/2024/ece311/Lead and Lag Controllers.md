For [[Controllers]]

# Lead Controller $$C(s)=K\frac{Ts+1}{\alpha Ts+1}: 0<\alpha<1$$ 
![[Pasted image 20241218133408.png]]
### Generally for when we want to get to a specific PM.
# Lag Controller $$C(s)=\alpha\frac{Ts+1}{\alpha Ts+1}:\alpha>1$$
![[Pasted image 20241218142211.png]]
### Generally when we want to get a DC Gain

# Steps
1. Find $K$
2. Determine $\Phi_\max$ necessary to obtain desired PM $$\Phi_\max = PM - PM_{\text{original }}+\text{extra margin (≈30°)}: 0<\Phi_\max<\frac{\pi}{2}$$
3. Determine $\alpha$ from $\sin(\Phi_\max)=\frac{1-\alpha}{1+\alpha}\to \alpha=\frac{1-\sin(\Phi_\max)}{1+\sin(\Phi_\max)}$ Or just choose it such that you get a pole at the decade after your $\omega_\text{crossover}$
4. Find $\omega_\max$
5. Calculate $\frac{1}{T}=\sqrt{a}\omega_\max$ or $\frac{1}{T}\leq0.1\omega_c$
6. Verify new $CG$ function
7. Check stability with [[Nyquist Criterion]] or [[Routh Stability Criterion]].

