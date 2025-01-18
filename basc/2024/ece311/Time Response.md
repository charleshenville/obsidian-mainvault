- Looking at the standard form of a second order system in the context of control systems: $$Y(s)=\frac{\omega_n^2}{s^2+2\zeta\omega_ns+\omega_n^2}$$Where $\omega_n$ is the natural frequency, $\zeta$ is the damping ratio.

## In the time domain: $$y(t)=\frac{\omega_n}{\sqrt{1-\zeta^2}}e^{-\zeta\omega_nt}\sin(\omega_n\sqrt{1-\zeta t})\cdot t:s_{1,2}=-\zeta\omega_n\pm i\omega_n\sqrt{1-\zeta^2}\text{ or }\sigma\pm i\omega_d$$
Where when $$\begin{cases}\text{underdamped} & \zeta<1\\\text{crit. damped} & \zeta=1\\\text{overdamped} & \zeta>1\end{cases}$$
Notice what then happens to the $\Re, \Im$ components of $s_{1,2}$
[[Second Order Systems]]