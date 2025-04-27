To be used as a form of [[Dynamic Programming]] under [[Bayesian Networks]].
- Variable elimination uses the product decomposition that defines the Bayes Net and the summing out rule to compute posterior probabilities from the information (CPTs) already in the network.

## Variable Elimination Example
![[Pasted image 20250418183602.png]]
$$F=f_1(A)f_2(B)f_3(A,B,C)f_4(C,D)$$
$$F'=f_1(A)f_2(B)f_3(A,B,C)f_4(C)|_{D=d}$$
$$F''=f_1(A)f_2(B)g_1(A,B): g_1(A,B)=\sum _{c_i\in C}f_3(A,B,c_i)f_4(c_i)$$
$$F'''(A)=f_1(A)g_2(A): g_2(A)=\sum _{b_i\in B}f_2(b_i)g_1(A,b_i)$$
$$P(A|D=d)=\frac{f_1(A)g_2(A)}{\sum_{a_i\in A}f_1(a_i)g_2(a_i)}$$

## Min Fill Heuristic
- Fairly effective, just get rid of the variable that results in the smallest factor size next. We want to get large reductions in factor scope as soon as possible. 
