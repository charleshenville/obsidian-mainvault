# With variable outcome

- Think coin toss, die roll

# Sample Space

$$ \text{example, coin toss: } S=\{H,T\} $$

## They can also be continuous

$$ S=\{0\to1\} $$

## We can map each event to a corresponding lieklyhood:

$$ N_k(n)=\text{no. of k results in n trials} $$

Relatively:

$$ f_k(n)=\frac{N_k(n)}{n} $$

## Then we can concretely define the probability of an outcome k by increasing our sample size to infty:

$$ \lim_{n\to\infty}f_k(n)=P[k] $$

Where:

$$ 0\leq P[k]\leq1,\space p[S]=1 $$

# Example with Mutual Exclusivity, $k_1, k_2$

- Meaning cannot co-occur

$$ P[k_1\textbf{ or }k_2]=P[k_1]+P[k_2] $$

# Def’n: [[Events]]

- A condition on outcomes, i.e a subset of S

Coin toss example again, where we define event A where both outcoms of two trials are the same:

$$ S=\{HH,HT,TH,TT\} $$

Then:

$$ P[A]=P[HH+TT]=P[HH]+P[TT]=\frac{1}{4}+\frac{1}{4}=\frac{1}{2} $$

If an Event consists of just a single outcopme then we call it an _Elementary Event_

# Sets

$$ A\text{ or }B = A \cup B $$

$$ A\text{ and }B=A\cap B $$

# Compliments

$$ A^c=\bar A $$

- The entire set S excluding A in this case

# DeMorgan’s Rule

$$ (A\cap B)^c=A^c\cup B^c $$

# Other version of [[Boolean Algebra]] DeMorgan’s Rule

$$ (A\cup B)^c=A^c\cap B^c $$

Provable via Venn Diagrams. Also:

$$ P[A\textbf{ or }B]=P[A]+P[B]-P[A\textbf{ and }B] $$
