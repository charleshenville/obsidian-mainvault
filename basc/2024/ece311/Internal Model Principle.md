# Note The following
- $R(s)$ and $D(s)$ are rational and strictly / properly bounded
- The Controller, $C(s)$, solves BCP iff
	- $C(s)$ makes the closed loop BIBO Stable -> [[Stability In Control Systems]]
	- $C(s)G(s)$ has poles of $R(s)$ -> [[Asymptotic Tracking]]
	- $C(s)$ has all poles of $D(s)$ -> [[Disturbance Rejection]]