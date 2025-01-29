Again looking at how the error changes given we have changed one of the network weights
# $$\frac{\partial E}{\partial w_{ij}}$$
![[Pasted image 20250114192846.png]]
## How we change the weights of the [[Artificial Neural Networks]] $$w_{ij}^{t+1}=w_{ij}^t-\gamma\frac{\partial E}{\partial w_{ij}},\quad\Delta w_{ij}=\gamma\frac{\partial E}{\partial w_{ij}}$$
- Where our **Learning Rate, $\gamma$** is a [[Hyperparameters]] chosen carefully such to be fast and not skip over minimums 
![[Pasted image 20250121190216.png]]

# Example
![[Pasted image 20250114194219.png]]
