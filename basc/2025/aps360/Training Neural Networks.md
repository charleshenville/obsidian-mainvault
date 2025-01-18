## Learning the wights and biases of NNs
- $\vec x\in\mathbb{R}^d$
- $y\in\mathbb{R}$
- $t\in\mathbb{R}$(ground truth)
- Neuron, $M(\vec x;\vec w)$ ie prediction

## Computing Loss
- $\mathcal{L}(y,t)$
- Comparing correct output with predicted from M

# Prediction -> Compute Loss -> Adjust Parameters -> Repeat until Loss is acceptable
- Computing $\frac{\partial \mathcal{L}}{\partial w_i}$ will help. Doing this via a backwards pass and chain rule.
- Backwards passes are only used in training for wight adjustments
- Forwards passes are done for inference and training when validating

# Loss Function
![[Pasted image 20250114183215.png]]
![[Pasted image 20250114183636.png]]
- To interpret outputs, we should map them to distinct probabilities that sum to one. we can do this via a softmax function.
# $$\text{Softmax}(x)_i=\frac{e^{x_i}}{\sum_{k=1}^Ke^{x_k}}$$
- After this we can take the difference between M and the on-hot encoded ground truth

# Loss Function Candidates

## Mean Squared Error (MSE) from [[Regression]] and [[Variance]] $$\text{MSE}=\frac1N\sum_{n=1}^N(y_n-t_n)^2$$![[Pasted image 20250114185106.png]]

## Cross Entropy (CE)$$\text{CE} = -\frac{1}{N} \sum_{n=1}^{N} \sum_{k=1}^{K} t_{n,k} \log(y_{n,k})
$$Where:
- $N$: The number of samples in the dataset.
- $K$: The number of classes.
- $t_{n,k}$: The true label for the n-th sample and k-th class (usually a one-hot encoded vector).
- $y_{n,k}$: The predicted probability for the n-th sample and k-th class.

## Binary Cross Entropy (BCE)$$BCE = -\frac{1}{N} \sum_{n=1}^{N} \left[ t_n \log(y_n) + (1 - t_n) \log(1 - y_n) \right]
$$
