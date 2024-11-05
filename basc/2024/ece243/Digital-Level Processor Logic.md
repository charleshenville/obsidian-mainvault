# See [[Flip-Flops]], [[Registers]], [[Multiplexers]].

# The Register File

- A way to access the 4 8-bit registers we have on the [[Simplified Processor]] so we can use them for instructional execution.

```mermaid
graph TD
	c[" "]
	d[" "]
	e[" "]
	f[" "]
	g[" "]
	h[" "]
	RFWRITE --> RF
	subgraph RF
		regA
		regB
		regW
		dataA
		dataB
		dataW
	end
  c --2--> regA
  e --2--> regB
  h --8--> regW
  dataA --8--> d
  dataB --8--> f
  g --8--> dataW
  clock --> RF
```

- If `RFWRITE` is on, copy `dataW` into `regW`.

```mermaid
graph TD
	c[" "]
	d[" "]
	e[" "]
	g[" "]
	y[" "]
	z[" "]
	RFWRITE --> RF
	subgraph RF
		regA --> s
		regB --> sB
		dataA
		dataB
		dataW --D--> r0
		dataW --D--> r1
		dataW --D--> r2
		dataW --D--> r3
		r0-->MUXA
		r1-->MUXA
		r2-->MUXA
		r3-->MUXA
		r0-->MUXB
		r1-->MUXB
		r2-->MUXB
		r3-->MUXB
		
		subgraph MUXA
		f
		s
		end
		regW --> Decoder
		subgraph Decoder
		fi["00"]
		fo["01"]
		fe["10"]
		fu["11"]
		end
		fi --EN WITH RFW-->r0
		fo --EN WITH RFW-->r1
		fe --EN WITH RFW-->r2
		fu --EN WITH RFW-->r3
		subgraph MUXB
		fB["f"]
		sB["s"]
		end
		
		f-->dataA
		fB-->dataB
	end
	c --2--> regA
	g --2--> regB
	y --2--> regW
	z --8--> dataW
  dataA --8--> d
  dataB --8--> e
  
```

# The [[Arithmetic Logic Unit]] on the [[Simplified Processor]]:

|ALUop|ALUout|
|---|---|
|000|A+B|
|001|A-B|
|010|A|
|011|!(A&B)|
|100|A<<B|
|101|A>>B|
|110|reserved|
|111|reserved|
![[IMG_4F18A12FB668-1.jpeg]]
# And The [[Memory]]:

- If `Memread` then after next `posedge clk`: `*address → dataout`
- If `Memwrite` then after next `posedge clk`: `datain → *address`
![[IMG_D214E753E5D4-1.jpeg]]