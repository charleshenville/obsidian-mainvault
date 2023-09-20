![[IMG_2929644A1C2A-1.jpeg]]

## [[Verilog]] For a Multiplexer

```verilog
module mux2to1 (x,y,s,f);

	input x,y,s;
	output f;

	assign f = (~s&x)|(s&y); //Boolean Logic Expression

end module //No semicolon.
```

NOT → ~

AND → &

OR → |

## Multi-bit Vector Multiplexer

![[IMG_872A79648689-1.jpeg]]
![[IMG_353C981E0BB8-1.jpeg]]
## [[Verilog]] implementation:

```verilog
module mux2to1_2bit(x,y,s,F);

	input [1:0] x,y; // Declaring that x and y have two bits
	input s;
	output [1:0] F;

	assign F[0] = (~s&x[0])|(s&y[0]);
	assign F[1] = (~s&x[1])|(s&y[1]);

end module
```
