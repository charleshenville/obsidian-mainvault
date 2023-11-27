|$x_1$|$x_2$|minTerm|$f_{ex}$|
|---|---|---|---|
|0|0|$m_0=\bar x_1\bar x_2$|1|
|0|1|$m_1=\bar x_1 x_2$|1|
|1|0|$m_2=x_1\bar x_2$|0|
|1|1|$m_3=x_1x_2$|1|

## Karnaugh(K)-maps $\to$ Minimize Logic Expressions

## K-map:

| |$x_1\to0$|$x_1\to1$|
|---|---|---|
|$x_2\to0$|$m_0\to1$|$m_2\to0$|
|$x_2\to1$|$m_1\to1$|$m_3\to1$|

$m_0=\bar x_1\bar x_2$

$m_1=\bar x_1x_2$

$m_3=x_1x_2$

### We can combine these midterms with [[Sum of Products]] and repeat these terms as many times as we want ([[Boolean Algebra]]) without actually changing the logic. We eventually get:

$$f=\bar x_1+x_2$$

## For a 3-variable function:

|$x_1$|$x_2$|$x_3$|minTerm|$f_{ex}$|
|---|---|---|---|---|
|0|0|0|$m_0$|0|
|0|0|1|$m_1$|1|
|0|1|0|$m_2$|0|
|0|1|1|$m_3$|0|
|1|0|0|$m_4$|1|
|1|0|1|$m_5$|1|
|1|1|0|$m_6$|1|
|1|1|1|$m_7$|0|

| |$x_1x_2\to00$|$x_1x_2\to01$|$x_1x_2\to11$|$x_1x_2\to10$|
|---|---|---|---|---|
|$x_3\to0$|$m_0\to0$|$m_2\to0$|$m_6\to1$|$m_4\to1$|
|$x_3\to1$|$m_1\to1$|$m_3\to0$|$m_7\to0$|$m_5\to1$|

### We select boxes of Neighbours (only change in one variable) and such that we cover all entries where $f=1$. We create and order out table in such a way that we respect these neighbouring terms.
$$\bar x_3x_1+x_1\bar x_2+x_3\bar x_2 = \bar x_3x_1+x_3\bar x_2$$

## For a 4-variable function:

| |$x_1x_2\to00$|$x_1x_2\to01$|$x_1x_2\to11$|$x_1x_2\to10$|
|---|---|---|---|---|
|$x_3x_4\to00$|$m_0$|$m_4$|$m_{12}$|$m_8$|
|$x_3x_4\to01$|$m_1$|$m_5$|$m_{13}$|$m_9$|
|$x_3x_4\to11$|$m_3$|$m_7$|$m_{15}$|$m_{11}$|
|$x_3x_4\to10$|$m_2$|$m_6$|$m_{14}$|$m_{10}$|

## For $\sum m(0,1,5,9,10,13,14,15)$
- EPIs: $\bar a\bar b\bar c, \bar cd, ac\bar d$
- PIs: $\bar a\bar b\bar c, \bar cd, ac\bar d, abd, abc$
- We can choose blue $\oplus$ purple to form a cover.
![[Screenshot 2023-10-02 at 23.49.07.jpeg]]
## Five-Variable Example $f(a,b,c,d,e)$:
$$f(a,\dots e)=abc+\bar abd+a\bar b\bar c\bar d+bd\bar e$$
![[Screenshot 2023-10-02 at 23.54.37.jpeg]]
## Using [[Product of Sums]]:
$$f(a\dots e)=(\bar a+c+d)(a+\bar c)(b+\bar c+\bar d)(a+\bar b+\bar d)$$
![[Screenshot 2023-10-02 at 23.55.10.jpeg]]

## If we don't need all of our outputs, for example displaying 0-9 7-Segment [[Hierarchy Design]], we can consider them to be 1 or 0 depending on what is convenient, and create Prime Implicants from there.