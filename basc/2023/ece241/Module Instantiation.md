In [[Verilog]], we can use our modules in other modules.
- With our custom mux2to1 [[Verilog]] module

```verilog
//Need our module definition
module mux2to1 (x,y,s,f);

	input x,y,s;
	output f;

	assign f = (~s&x)|(s&y); //Boolean Logic Expression

end module //No semicolon.

module mux2to1_2bit(x,y,s,F);

	input [1:0] x,y;
	input s;
	output [1:0] F;

	mux2to1 U1(x[1], y[1], s, F[1]); // Module Instantiation
	mux2to1 U2(x[0], y[0], s, F[0]);

end module
```

## Alternative Instantiation by name:

```verilog
mux2to1 U1 (.x(x[1]), .s(s), .y(y[1]), .f(F[1])); // We can shuffle the signal locations here
mux2to1 U2 (.x(x[0]), .s(s), .f(F[0]), .y(y[0]));
```