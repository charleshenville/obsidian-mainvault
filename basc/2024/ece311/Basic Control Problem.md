Shorthand **BCP**

# Standard Feedback Control Loop
![[IMG_4020AB39A9A7-1.jpeg]]

- R(s) -> Reference Signal
- D(s) -> Disturbance Signal
- E(s) -> Tracking Error
- Y(s) -> Output Signal

# Key specifications for designing a controller, $C(s)$, to ensure:

1. **[[Stability In Control Systems]]**: 
	- The system remains bounded for any bounded reference input $r(t)$ and disturbance $d(t)$. 
	- Specifically, both the control signal $u(t)$ and the error $e(t)$ need to be bounded, ensuring the system does not become unbounded in response to normal inputs and disturbances. 
	- This is essential for preventing unbounded behaviour in real-world applications.

2. **[[Asymptotic Tracking]]**: 
	- Assuming no disturbances $(d(t)≡0)$, the controller should be able to make the system output $y(t)$ track the reference input $r(t)$ over time. 
	- This is achieved if the tracking error $\lim\limits_{t\to\infty}e(t)=\lim\limits_{t\to\infty}(r(t)−y(t))=0$.
	- Ensures that the system can follow the desired reference input accurately in the absence of disturbances. 
	- This is crucial for applications requiring precise control (like robotics or automated systems).

3. **[[Disturbance Rejection]]**: 
	- Assuming the reference $r(t)≡0$, the controller should reject any disturbances $d(t)$ by ensuring that $\lim\limits_{t\to\infty}y(t)=0$. 
	- This means that the system can counteract disturbances, with $\lim\limits_{t\to\infty}e(t)=0$, showing the system's ability to maintain its output stability despite external disruptions. 
	- This enhances system resilience, making it capable of handling unpredictable inputs while maintaining desired behaviour.