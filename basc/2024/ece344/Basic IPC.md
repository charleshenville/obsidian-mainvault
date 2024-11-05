## A refresher on File Descriptors
- `fd=0` -> std read
- `fd=1` -> std write

## Blocking vs Non-Blocking
- non-blocking calls return immediately
	- most operations are of this type

# Signals
- They are a form of IPC that "interrupt" your program
	- Like interrupts for user processes
- Some useful ones:
	- 2: `SIGINT` (interrupt from keyboard)
	- 9: `SIGKILL` (terminate immediately)
	- 11: `SIGSEGV` (memory access violation)
	- 15: `SIGTERM` (terminate)
- You can send signals directly to processes with `pidof`