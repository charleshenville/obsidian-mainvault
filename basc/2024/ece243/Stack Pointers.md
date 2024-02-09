## Akin to [[Stacks]] from 244.

- r27 in NIOS II, points to the top of the stack, called sp.
- This must be initialized at the beginning of the program
- We must pick an address and a direction for growth. We will choose decrementing addresses (”down”). Staring at a sufficiently high address. The heap grows with incrementing addresses.
- Conventionally, use 0x00020000 as the first stack address. It will grow down from there.

```nasm
movia sp, 0x20000
; We will push a word onto the stack.
movia r8, 0x1234f678
subi sp, sp, 4 ; Move down one word to get ready to push
stw r8, (sp) ; Move the thing in r8 into the new address of sp
; Now we will pop
ldw r9, (sp) ; Loads from memory
addi sp, sp, 4 ; Move the stack pointer back up
```

## Back to nested [[Subroutines]]

```nasm
_start:
	movia sp, 0x20000
	movi r4, 1
	call sub_1
done: br done
sub_1: 
	; push our current return address onto the stack
	subi sp, sp, 4
	stw ra, (sp)
	; do stuff
	call sub_2
	; pop
	ldw ra, (sp)
	addi sp, sp, 4
	ret ; pc<-ra
sub_2:
	; push current ra into the stack again
	subi sp, sp, 4
	stw ra, (sp)
	; do stuff
	call sub_3
	; pop
	ldw ra, (sp)
	add sp, sp, 4
	ret ;pc<-ra
sub_3:
	; push current ra into the stack again
	subi sp, sp, 4
	stw ra, (sp)
	; pop
	ldw ra, (sp)
	add sp, sp, 4
	ret ;pc<-ra
```