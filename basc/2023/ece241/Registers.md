## We can Build them by Daisy-Chaining [[Data Latch]]es as follows, they are multi-bit [[Flip-Flops]]:
![[IMG_D9F74EC8D077-1.jpeg]]
![[IMG_D1674AFA46CB-1.jpeg]]

## [[Verilog]] implementation of a 4-bit Register

```verilog
module 4_bit_reg(D, En, clock, Resetn, Q);
	input [3:0] D;
	input En, clock, Resetn;
	output reg [3:0] Q;
	always@(posedge clock);
		begin
			if (Resetn==0); // Active low reset.
				Q<=0;
			else if (En==1); // Active high enable.
				Q<=D;
		end
endmodule
```

# Shift Registers:
- Exist to prevent high-cost wide wires.
![[IMG_FCEBE391B38F-1.jpeg]]

## 3-Bit example:
![[IMG_617A181A7001-1.jpeg]]
If we reset at the beginning, meaning:
$$Q_2=Q_1=Q_0=0,\space t=t_0$$
![[IMG_802B0BAA9F52-1.jpeg]]
## [[Verilog]] Implementation of a 3-bit Serial Shift Register

```verilog
always@(posedge clock);
	begin
		Q[2] <= W; // We MUST use Nonblocking <= here. 
		// These assignments happen simultaneously.
		Q[2] <= Q[2];
		Q[2] <= Q[1];
	end

//In verilog, we can also do
Q>>2
//To shift (bitwise) from left to right
```

## Parallel Shift example with [[Multiplexers]]:

![[IMG_8C22C02F17ED-1 1.jpeg]]
## [[Verilog]] Implementation of a 3-bit Parallel Shift Register

```verilog
always@(posedge clock);
	begin
		if (!Resetn) // Same as Resetn == 0
			Q<=0;
		else if (Loadn==0)
			Q<=D; // Parallel load. Both vectors here.
		else
			//Behave like We did before with the Serial Shift Register.
			Q[2] <= W; // Shift from left to right.
			Q[2] <= Q[2];
			Q[2] <= Q[1];
	end

```