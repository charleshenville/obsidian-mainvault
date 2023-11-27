![[IMG_2FE12FCE26D0-1.jpeg]]

## [[Verilog]] Implementation of a Moore FSM:
```verilog
module sequence101(clock, Resetn, W, Z);
	input clock, Resetn, W;
	output Z;
	reg [2:1] y, Y;
	parameter [2:1] A = 2'b00, B = 2'b01, C = 2'b10, D = 2'b11;

	always@(*) begin // Implementation of Combinational Logic Ckt A In diagram Above.
		case(y) // Case for present state.
			A: if(!W) Y=A; else Y=B;
			B: if(!W) Y=C; else Y=B;
			C: if(!W) Y=A; else Y=D;
			D: if(!W) Y=C; else Y=B;
			default: Y=A;
			// This pattern of case statements is entirely based off of the state diagram
		endcase
	end
	always@(posedge clock) begin
		if (!Resetn) y<=A;
		else y<=Y;
	end
	assign z=(y==D);
endmodule
```