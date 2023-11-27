# This happens when we drop the following assumption:
- All clock pulses reach all [[Flip-Flops]] or other clock-dependent elements simultaneously.
![[Pasted image 20231110143614.png]]
![[Pasted image 20231110150903.png]]

We must allow a minimum time, $T_{min}$ for data from `A` to reach `B` before the next clock edge. We can use [[Basic Timing]] to find a way to express this minimum T:
$$T_{min}=t_{CQ}+t_{gates}+t_{su}$$
$$\text{Max clock frequency, }F_{max}=\frac{1}{T_{min}}$$
We can create $T_{min_{new}}$ such that:
$$T_{min_{new}}\lt T_{min}$$
$$T_{min_{new}}+t_{skew}=T_{min}$$
![[Pasted image 20231110152951.png]]

## Checking for hold time with Clock Skew:
![[Pasted image 20231110153303.png]]

We must allow for the passing of $t_h$:
![[Pasted image 20231110155412.png]]

In this case:
$$t_{CQ}>t_h+t_{skew}$$
The inequality regarding $t_h$ and $t_{CQ}$ must be obeyed at all times. Conventionally, $t_{CQ}$ alone is larger than $t_h$.