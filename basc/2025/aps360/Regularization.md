To prevent overfitting, helps/forces network to learn more about robust features

## Dropout
- Dropping activations -> 0 with probability $p$
- Multiply weights by ($1-p$) to keep [[Probability Density Function]].
![[Pasted image 20250121193340 1.png]]

## Weight Decay (L2)
- prevents weights from growing like crazy
- This lowers variance
$$\begin{align*}
E(W; y, t) &= E(W; y, t) + \frac{\alpha}{2} \| W \|_2^2 \quad \longrightarrow \quad \frac{\partial E}{\partial W} = \frac{\partial E}{\partial W} + \alpha W \\
W_{t+1} &= W_t - \gamma \left( \alpha W_t + \frac{\partial E}{\partial W} \right)
\end{align*}
$$
## Early Stopping with Patience
![[Pasted image 20250121193543 1.png]]

