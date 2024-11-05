### We can apply the principle of [[Linearization of Non-Linear Systems]] to situations with the [[State-Space Model]]:$$\dot x=f(x,u)$$
## We assume there are equilibrium solutions: $\exists t:x(t)\equiv x_0, u(t)\equiv u_0, f(x_0, u_0)=0=\dot x$

# Consider a [[Neighbourhood]] of the above equilibrium points:
$$x(t)=x_0+\Delta x(t),\space u(t)=u_0+\Delta u(t)$$
$$\dot x(t)=f(x_0,u_0)+A\Delta x(t)+B\Delta u(t)+\text{HOTs}$$
We have $[A|B]=f'(x_0, u_0)$ and $\because f(x_0,u_0)\to\dot x=\dot{\Delta x}$:
$$\dot{\Delta x}=A\Delta x+ B\Delta u$$ and similarly if we have $y=h(x, u)$:
$$h'(x_0,u_0)=[C|D]\to\Delta y=C\Delta x+ D\Delta u$$
