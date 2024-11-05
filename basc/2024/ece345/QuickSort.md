[[Sorting]] Method:

![[IMG_6C005F4184C7-1.jpeg]]

# Worst Case
$$T(n)=T(n-1)+\Theta(n)=O(n^2)$$
For a bad pivot choice

# Best Case
$$T(n)=2T({\frac{n}{2}})+\Theta(n)=n\log n$$
For a perfect set where we select a middle pivot every time

# Balanced (Average) Case
$$T(n)=T(\frac{n}{10})+T(\frac{9n}{10})+O(n)=O(n\log n)$$
$$T(n)=T(\frac{n}{1000000})+T(\frac{999999n}{1000000})+O(n)=O(n\log n)$$
# A Formalized Worst Case
$$T(n)=\max_{1\leq q\leq n-1}\{T(q)+T(n-q)\}+O(n)\to O(n^2)$$
We can see this is the case when q is at either extreme (either $1$ or $n-1$).

![[IMG_DD252BA7F6DD-1.jpeg]]

![[Pasted image 20241004215359.png]]