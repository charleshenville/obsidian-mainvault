# Loosely:
- Systems where the principle of superposition holds, and the system will be the same in a few moments as it is at the present moment.
# Impulse Response of CT LTI Systems, $h(t)$:$$h(t)=T\{\delta(t)\}(t)$$
## $h$ enables us to compute the output of an LTI System for any given input signal, $x$ by way of its Impulse Representation:$$x(t)=\int_{-\infty}^\infty x(\tau)\delta(t-\tau)d\tau=\int_{-\infty}^\infty x(\tau)\delta_\tau d\tau$$$$y(t)=T\{x\}(t)=\int_{-\infty}^\infty h_\tau(t)x(\tau)d\tau=\int_{-\infty}^\infty h(t-\tau)x(\tau)d\tau=h*x$$
# This would bring us to [[Convolution]]

# The Impulse Response, $h=T\{\delta\}$ can tell us about the [[Properties of CT Systems]]:
- $T$ is causal iff $h(t)=0\forall t<0$
- $T$ is memoryless iff $h(t)=\alpha\delta(t):\alpha\in\mathbb{C}$
- $T$ is BIBO Stable if $h\in L_1$, in which case:$$||y||_\infty\leq||h||_1||x||_\infty\space\forall x\in L_\infty, y=T\{x\}$$
