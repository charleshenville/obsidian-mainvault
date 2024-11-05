# With [[Controlling Data-Paths with FSMs]]:
# Executing the add instruction:

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Ra|→|Rb|→|0|1|0|0|

1. **Fetch** - instruction from the memory via the address held by the pc
2. **Decode** - Figure out what the instruction is meant to do, look at bits [3:0] for Op Code.
3. Read - Ra and Rb from the register file, encoded in the instruction, must have two new registers, A and B.
4. Compute - `ALUout = Ra + Rb = A + B` With a new register, ALUout.
5. Write ALUout into Ra (in the RF) by activating RFWRITE.
6. Set Z&N.
7. pc ← pc + 1

# Note that other instructions follow a similar sequence... (Approximately).