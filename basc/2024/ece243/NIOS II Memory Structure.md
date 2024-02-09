## Nios II - 32 Bit Processor.
- Has a word size of 32; access 32 bits at a time from [[Memory]].
- Although every byte has a separate address in memory.
- Memory addresses are 32 bits in size → gives us $2^{32}=4\text{BN}$ possible memory addresses.

|ADDRESS|CONTENTS (4 Bytes each for 32 Bit total)|
|---|---|
|0x0|Word 0|
|0x1|Word 1|
|0x4|Word 2|
|0xC|Word 3|

Taking Word 1 for example we must use 4 memory addresses:

|0x7|0x6|0x5|0x4|
|---|---|---|---|

### We have a least significant (0x4) and most significant (0x7) byte address
- Or little endian vs. big endian
- Where the address for the whole word is the least significant byte address.

## An [[Assembly Language]] Program to add and organize some numbers in memory appropriately

- similar to the array invocation in C: `int list[3]={10,20,30}`
- We must remember that every instruction will be placed into memory at some location, again in 4 byte chunks.

```nasm
.global _start
_start:
	movi r8, list   ;0x0
	ldw r9, (r8)    ;0x4 ;Load word from memory at address stored in r8 (0x24). Reminiscent of pointer dereference.
	ldw r10, 4(r8)  ;0x8 ;Load word from memory at address stored in r8+4 (0x28).
	ldw r11, 8(r8)  ;0xC ;r11 <- 30
	add r9, r9, r10 ;0x10
	add r9, r9, r11 ;0x14
	movi r8, answer ;0x18
	stw r9, (r8)    ;0x1C ;0x30 <- r9 (10+20+30=60)
	done: br done   ;0x20 ;our infinite loop. branch to done.
	list: .word 10  ;0x24 ;Place 10 at current word address, using a full word size.
		  .word 20  ;0x28
		  .word 30  ;0x2C
	answer: .word 0 ;0x30
	
```