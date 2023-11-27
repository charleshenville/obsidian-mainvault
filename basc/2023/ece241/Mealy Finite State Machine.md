![[IMG_F41D4F063ED5-1.jpeg]]

Mealy State Transitions happen faster than that of [[Moore Finite State Machine]]s, that is, on the same clock tick.

## [[Verilog]] Implementation of a Mealy FSM:

```verilog
always@(*) begin
	case(y) // Combinational Logic from State Table
		A: if(!W) Y=A; else Y=B;
		B: if(!W) Y=C; else Y=B;
		C: if(!W) Y=A; else Y=B;
		default: Y=A;
	endcase
end
always@(posedge clock) begin
	if(!Resetn) y<=A;
	else y<=Y; // Go to next state.
end

assign Z=W&(y==C); // If we are in state C and W turns on, then turn the output on
```