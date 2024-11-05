**# The Master Method For Recurrences: rooted in [[Recursion]]
- Solving them when they are of the form 
$$T(n)=aT(n/b)+f(n):\space a,b>0,\space f(n)=cn^k$$
We have three main cases to consider when finding tight $\Theta\text{-notation}$ bounds for these recurrences:
$$T(n)=\Theta(n^k) \text{ if } a<b^k$$
$$T(n)=\Theta(n^k\log n) \text{ if } a=b^k$$
$$T(n)=\Theta(n^{\log_b a}) \text{ if } a>b^k$$

# Master Theorem
### When the driving function is not in the form $cn^k$:
$$T(n)=\Theta(n^{\log_ba})\iff\exists\space\epsilon>0:f(n)=O(n^{\log_ba-\epsilon})$$
$$T(n)=\Theta(n^{\log_ba}\lg^{k+1}n)\iff\exists\space\epsilon>0:f(n)=\Theta(n^{\log_ba}\lg^{k}n)$$
$$T(n)=\Theta(f(n))\iff\exists\space\epsilon>0:f(n)=\Omega(n^{\log_ba+\epsilon}) \text{ and }af(\frac{n}{b})\leq cf(n): c<1$$
Where the condition in case c is referred to as the **regularity condition**

