## We consider the worst case scenarios, example with arrays or [[Linked Lists]]:

## Linear Searches:

- We need to make at most `n` comparisons for a n-long list; O(n).

## Binary Searches:

- We have a sorted list; we start searching in the middle and divide by 2 while moving in a particular direction based on our target value.

$$\frac{n}{2^x}=1\to n=2^x \to x=\log_2(n)\text{ comparisons}$$

When evaluating `T(n)` (complexity involving multiple terms with varying degrees of n), we only regard its highest-degree or largest term as $n\to\infty$. This is what "explodes" with increasing n. We call this `O(g(n))`; the upper bound of `T(n)`. 
- For example, T(n) for matrix side length $n$ addition → $O(n^2)$.

![Big O Cheat Sheet – Time Complexity Chart](https://paper-attachments.dropbox.com/s_2D428973624E7FC84C7D69D11421DE762BEA6B6F3361231FCDCAE0425D14526F_1664885448372_Untitled.drawio+17.png)
