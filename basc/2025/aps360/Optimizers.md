# Stochastic [[Gradient Descent]] (SGD)
 - evaluate training sample from dataset at random
![[Pasted image 20250121183849.png]]
- can add a momentum term ($\lambda$) to influence our decision to keep traversing a direction depending on how well we are doing.
$$\begin{cases}v_{ji}^t=\lambda v_{ji}^{t-1}-\gamma\frac{∂E}{∂w_{ji}}\\w_{ji}^{t+1}=w_{ji}^t+v_{ji}^t\end{cases}$$
![[Pasted image 20250121185431.png]]

## Mini-Batch Gradient Descent (MBGD)
- look at average loss for $n$ samples and try to optimize that.
- [[Hyperparameters]]: 
	- **Batch** **Size** ($n$): num. training example per optimization step
		- Bigger not always better, sometimes we want noise in the averages and thus aprroximated gradient
	- **Iteration**: One single step
	- **Epoch**: # of times all the training data is used to update params

![[Pasted image 20250121185040.png]]

## Adaptive Moment Estimation (Adam)
- Learning rates are dynamic and each weight has its own weight$$\begin{align*}
m_t &= \beta_1 m_{t-1} + (1 - \beta_1) \left( \frac{\partial E}{\partial w_{ji}} \right) \\
v_t &= \beta_2 v_{t-1} + (1 - \beta_2) \left( \frac{\partial E}{\partial w_{ji}} \right)^2 \\
w_{ji}^{t+1} &= w_{ji}^t - \frac{\gamma}{\sqrt{v_t} + \epsilon} m_t
\end{align*}
$$
![[Pasted image 20250121190020.png]]
