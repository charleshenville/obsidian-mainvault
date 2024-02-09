# 1
Defining [[Continuous Time Signals]] and Sampling to create [[Discrete Time Signals]]:
```matlab
%Define a "CT" signal
T_max = 6; h=0.001;
t = -T_max:h:T_max;
x = cos(3*t).*exp(-0.2*t) + ...
heaviside(t+5)-heaviside(t-1);

%Sample the signal with period T_s
T_s = 0.5;
t_s = t(1:T_s/h:end);
x_s = x(1:T_s/h:end);

%Plot both signals
plot(t,x); hold on; stem(t_s,x_s); hold off;
```
# 2
![[Pasted image 20240123225448.png]]
