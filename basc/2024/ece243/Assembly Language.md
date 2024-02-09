## Three Focal Components

### Processor / CPU

- 32 32 Bit Registers
- ALUs
- FSMs

### Memory

- Many Addresses. Byte-wise on NIOS II

### I/O Units

- Screens
- KBM
- LEDs
- 7 Segs.

## Converting the following C into ASM-L
```c
int A,B,C,D;
A=1;
B=8;
C=A+B;
D=B-A;
```

### In ASM-L
```nasm
	movi r8, 1 /* r8<-1 */
	movi r9, 8 /* r9<-8 */
	add r10, r8, r9 /* r10<-r8+r9 */
	sub r11, r9, r8 /* r11<-r9-r8 */
iloop: br iloop /* Branch to iloop repeatedly */
```
