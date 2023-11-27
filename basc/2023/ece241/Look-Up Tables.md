## LUTs

- Building logic function by programming some storage cells:
- Can implement any n-input logic function with any kind of [[Complex Logic Gates]].

```mermaid
graph LR
		
LUT["LUT(4 Storage cells)"]
	  x0 --> LUT
		x1 --> LUT
LUT --> f
```
$$ n_{cells}=2^{n_{inputs}} $$

## 2-LUT (2-input) Implementation with [[Multiplexers]]

- Where `[3:0] f` are Memory Cells storing 0 or 1.

```mermaid
graph LR
	muxa["MUX"]
	muxb["MUX"]
	muxc["MUX"]
  f0 --> muxa
	f1 --> muxa
	f2 --> muxb
	f3 --> muxb
	muxa --> muxc
	muxb --> muxc
	muxc --> f
	x0 ----> muxa
	x0 ----> muxb
	x1 -----> muxc
```
$$ n_{MUX}=2^{n_{inputs}}-1 $$

### FPGA on DE1-SoC: ~85k 4-LUTs, 32,075 ALUs [[Arithmetic Logic Unit]]s.