## We have some C code that we compile into [[Assembly Language]], which is then assembled into machine-understandable machine code.

# Using I/O Devices in ASM versus C:

```nasm
.equ LEDs, 0xff200000
.equ SW, 0xff200040
_start: movia r8, LEDs
				movia r9, SW
loop: ldwio r10, (r9)
			stwio r10, (r8)
			br loop
```

```c
int main(void){
	volatile int *LED_ptr = 0xff200000; // The value at this address can change between accesses.
	volatile int *SW_ptr = 0xff200040; // Will not work without volatile.
	int value;
	while(1){
		value = *SW_ptr;
		*LED_ptr = value;
	}
	return 0;
}
```
