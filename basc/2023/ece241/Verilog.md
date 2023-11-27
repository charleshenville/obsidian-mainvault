- A Hardware Description Language (HDL)
- Can:
    - Describe Circuits
    - Simulate Circuits
    - Synthesize Circuits

Generally, we must first design the circuit manually and then describe it through this HDL.

## By Structure
To describe this series of logic gates, we can use the following verilog:

```verilog
and a_and(c,a,b);
or a_or(f,d,e);
```

## By Behaviour ([[Boolean Algebra]] expressions)

```verilog
c = a & b; s = A + B;
```
