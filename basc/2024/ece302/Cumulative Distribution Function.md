# Applies to all [[Random Experiments]]
- Regardless of [[Continuity]] or Discreetness.

## We're looking at the number of Heads in three coin tosses here.
- This is a Cumulative Distribution Function (CDF) ($F_X(x)$)
![[302 Notes.jpeg]]

## For Picking $x\in(0,1)$

# Properties of the Cumulative Discreet Function (CDF) 
$$F_X(x)=P(X\leq x)$$$$0\leq F_X(x)\leq 1$$
$$\lim_{x\to\infty}F_X(x)=P(X\leq\infty)=1$$
$$\lim_{x\to-\infty}F_X(x)=P(X\leq-\infty)=0$$

## We can get the probability that we have our variable falling between two values, we can take the difference of two of our CDF values:$$P[a<x\leq b]=P[X\leq b]-P[X\leq a]$$$$=F_x(b)-F_x(a)$$
# Probability Mass Function:$$\sum_{\text{all values}}P_X(x)=1$$
