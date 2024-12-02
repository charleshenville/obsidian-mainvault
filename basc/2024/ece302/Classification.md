Given a Vector of [[Random Variables]]
$$\vec X=\begin{bmatrix}X_1\\X_2\\\vdots\\X_n\end{bmatrix}$$
Goal: To classify these into a another class $Y$.
# Naive [[Bayes Rule]] Assumption:
- Given $Y$->$X$'s are independent: $$P(X=x|Y=y)=\prod_{i=1}^nP(X_i=x_i|Y=y)$$
We want to find $y$ which maximizes $P[Y=y|X=x]$
$$y^*=\arg \max_yP[Y=y|X=x]$$
Use [[Bayes Rule]]:$$y^*=\arg \max_y\frac{P(X=x|Y=y)P(Y\lt y)}{P(X=x)}$$
Use assumption and the fact that $\arg\max_y$ only depends on the Bayes expression with the assumption that each class is equally as likely to occur.$$y^*=\arg \max_y \prod_{i=1}^nP(X_i=x_i|Y=y)$$
Use a ML(Maximum Likelihood) $\log$ estimate for this:$$y^*=\arg \max_y \sum_{i=1}^n\log P(X_i=x_i|Y=y)$$
# By using a clever substitution: $$\boxed{y^*=\arg\max_y \sum_{i=1}^n\log f_{x_i}(x_i|y)}$$
