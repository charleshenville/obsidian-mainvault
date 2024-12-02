[[Dynamic Programming]]

# $A_1,\cdots A_m$
$$A_1A_2A_3\to((10*100)(100*5)(5*50))\to\text{some amount of operations}$$
- Let's try to minimize operations

| $(A_1A_2)A_3$      | $A_1(A_2A_3)$        |
| ------------------ | -------------------- |
| $10*100*5+10*5*50$ | $50*100*5+10*100*50$ |
|                    |                      |

# Solution
$$m[i,j]=\begin{cases}0\text{ if }i=j\\\min\limits_{i<k\leq j}\{m(i,k-1)+ m(k,j)+P_{i-1}P_kP_j\} \text{ if }i<j\end{cases}$$

Connection here to [[Complexity Classes]]