## Characteristic Table for D-Latches:
|$clk$|$D$|$Q(t+1)$|
|---|---|---|
|0|X|$Q(t)$|
|1|0|0|
|1|1|1|

### If the clock is enabled, $Q$ mimics $D$. Else $Q$ stores the previous state.

![[IMG_1EE5FEB3965B-1.jpeg]]
## [[Verilog]] Implementation of the D Latch:
```verilog
`timescale 1ns/1ns

module DLatch(D,clk,Q);
	input D, clk;
	output reg Q; // "reg" kwd so we can use it in the always block.

	always @ (*) //inplace of * we can write (all signals that affect output)
		begin
			if(clk==1)
				Q=D;
		end // No case necessary
endmodule
```