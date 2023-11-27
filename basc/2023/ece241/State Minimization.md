We can minimize the needed states of [[FSMs]] by observing state outputs and state transitions:
![[Pasted image 20231028130949.png]]

## By Partitioning:
- Given a state table like the following, we can follow a procedure to minimize the needed sates to represent an equivalent system:

|Current|Next (!W)|Next (W)|Output (Z)|
|---|---|---|---|
|A|B|C|1|
|B|D|F|1|
|C|F|E|0|
|D|B|G|1|
|E|F|C|0|
|F|E|D|0|
|G|F|G|0|

1. Assume all states are Equivalent
2. Look for "Reasons" to break them apart:
	1. Looking at outputs
	2. Looking at next states (State Transitions)
3. Repeat $2$ until we cannot anymore.

For the Above Example:
1. $P_0=(ABCDEFG)$
2. $P_1=(ABD)(CEFG) = g_1g_2$
	1. Since $g_1: A,B,D\to Z$ and $g_2:C,E,F,G\to \bar Z$ 
2. We observe no reason to further partition $g_1$ but for $g_2$:![[Pasted image 20231028131834.png]]
	1. Now, $P_2=(ABD)(CEG)(F)=g_1g_2g_3$.
3. Since we have changed our group definitions, we have a reason to partition $g_1$ now since $B\to g_3$ if $W$ and $A,D\to g_2$ if $W$. Now we have $P_3=(AD)(B)(CEG)(F)=g_1g_2g_3g_4$
3. We observe no reason to partition $g_2, g_3$, so finally, we have:
$$P_4=(AD)(B)(CEG)(F)=S_1S_2S_3S_4$$
We can observe a new, reduced state table:

|Current|Next (!W)|Next (W)|Output (Z)|
|---|---|---|---|
|$S_1$|$S_2$|$S_3$|`1`|
|$S_2$|$S_1$|$S_4$|`1`|
|$S_3$|$S_4$|$S_3$|`0`|
|$S_4$|$S_3$|$S_1$|`0`|