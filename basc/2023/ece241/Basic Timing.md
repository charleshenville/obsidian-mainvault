## In Lieu of changing D on [[Data Latch]]es with the posedge clock:

![[IMG_EF767BF6979A-1.jpeg]]
We must have sufficient $t_{su},\space t_{hold}$ to prevent issues:

Timing Analysis of the following Sample circuit:

![[IMG_05AF1152E549-1.jpeg]]
- Goal is to find the max. Clock frequency to allow for sufficient $t_{su},\space t_{hold}$.
- A matter of finding critical paths and performing appropriate analyses:
	- For $t_{su}$ we look for longest path with most delays.
	- Opposite for $t_{hold}$.
$$t_{CQ}>t_{hold}$$ **(??)**
Where $t_{CQ}$ is the clock $\to$ Output delay.