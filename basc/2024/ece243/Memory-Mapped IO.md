# Input detection, and communication with peripherals through [[Memory]]

### Method 1: Polling → processor explicitly asks for something new

### Method 2: Interrupt-Driven → processor diverts to alternative software upon receiving an interrupt signal

## Illustrating the connections o and from the KEY (Buttons) on the DE1-SoC board:

- 0xff200050 → Data register/address

|0xff200050|Data Register|Holds the KEY values, capturing actual data values in real-time|
|---|---|---|
|0xff200054|Direction Register|Will not use this|
|0xff200058|Interrupt Register||
|0xff20005C|Edge Capture Register|Captures button release edge|

Writing a logical 1 (high) into any of the 4LSB of the Edge Capture Register will reset it, turning it to zero. This is unlike any other memory address as we need special, additional hardware for it.

## Polling Loop for Data [[Registers]] in [[Assembly Language]]:

```nasm
.equ KEY_BASE, 0xff200050
;loop:
poll: movia r8, KEY_BASE
			ldwio r9, 0(r8)
			andi r9, r9, 2
			beq r9, r0, poll ; we need not poll again if we see a 1 at the 2ns lsb.
```