## Schema:
![[Note Sep 30, 2023.jpeg]]
Where "part 1" refers to Ripple-Carry [[Adders]].

## A note on [[Verilog]] Bitwise Reduction and Concatenation Operators to accomplish this:
```Verilog
module X(...);

	parameter N = 4;
	input [N:0] a,b;
	output out;

	wire [N+N] a_concat_b;
	wire redux_and_result;
	wire redux_or_result;

	assign a_concat_b = {a, b};
	assign redux_and_result =& a_concat_b;
	assign redux_or_result =| a_concat_b;

endmodule
```