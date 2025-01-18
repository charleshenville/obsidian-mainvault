![[Pasted image 20250114153446.png]]
- $x_i$: Input
- $w_i:$ The weight for a given input i
- $b:$ is the bias , a weight we learn with no input
- $f:$ the [[Activation Function]] that determines how our output changes with the sum of all weight-input products
- $y:$ output

``` python
import math
x = [[1.0, 0.1,-0.2], # data
[1.0,-0.1, 0.9],
[1.0, 1.2, 0.1],
[1.0, 1.1, 1.5]]
t = [0, 0, 0, 1] # labels
w = [1, -1, 1] # initial weights
	def simple_ANN(x, w, t):
		total_e, e, y = 0, [], []
		for n in range(len(x)):
			v = 0
			for d in range(len(x[0])):
				v += x[n][d] * w[d]
			y.append(1/1+math.e**(-v)) # sigmoid
			e.append((y[n]-t[n])**2) # MSE
		total_e = sum(e)/len(x)
		return (y, w, total_e)
```

