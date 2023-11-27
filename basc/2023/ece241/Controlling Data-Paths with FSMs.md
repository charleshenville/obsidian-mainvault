We wish to compute $Ax+B$.
![[IMG_2D22B490A73D-1.jpeg]]
We must perform these steps to accomplish this task:
0. `Reset` - Clearing all [[Registers]]
1. Load input $A$ into $RA$
2. Load input $B$ into $RB$
3. Load $RA \cdot x$ into RR
	- $x$ moves to $IA$, $RA$ moves to $IB$
	- `ALUfunc` set to `Multiplication`
4. Load $RR$ into $RA$
5. Load $[RA]+[RB]$ into $RR$
	- $RA$ moves to $IA$
	- $RB$ moves to $IB$
	- `ALUfunc` set to `Addition`

Example with $A=5, B=7, x=3$:

|Step|Reset|1|2|3|4|5|Done|
|---|---|---|---|---|---|---|---|
|x (INPUT)|-|5|7|3|3|3|3|
|RA|0|0|5|5|5|15|15|
|RB|0|0|0|7|7|7|7|
|RR|0|0|0|0|15|15|22|
|-|-|-|-|-|-|-|-|
|SelxR|0|0|0|0|1|0|0|
|SelxA|0|0|0|0|0|1|0|
|SelAB|0|0|0|0|0|1|0|
|LdRA|0|1|0|0|1|0|0|
|LdRB|0|0|1|0|0|0|0|
|LdRR|0|0|0|1|0|1|0|
|ALUfunc|ADD|ADD|ADD|MUL|ADD|ADD|ADD|

[[FSMs]] State Diagram:
![[IMG_20B6BD2E3D0E-1.jpeg]]
Note that a change in the state of any bottom-half variable induces a change in its respective top variable on the next step. It is also worth noting that we can control the `go` signal by using the inverse of the `KEY` (button) on the [[FPGAs]].

