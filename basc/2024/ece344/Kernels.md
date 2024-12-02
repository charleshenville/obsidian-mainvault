# Instruction Set Architectures
- Three major isas: x86-64, arm, riscv

# System Calls
- Can be represented as C Functions: See the Hello world example:

```c
void _start(void){
	// File descriptor 1 meaning a standard output (write)
	write(1, "Hello world\\n", 12); 
	exit_group(0); // Like returning from main with exit status zero
}
```

# Application Binary Interfaces (ABIs)
- Specifies low-level details relating to how to pass args and where to look for return values, think like [[The NIOS II Subroutine Calling Convention]]

# System Call ABI
We can generate interrupts with an `svc` instruction with registers for arguments. C-ABI doesnt work like this though.

# Executable Linkable Format (ELF)
- Linux executables and libraries. ASCII DEL ‘E’ ‘L’ ‘F’ as the header all the time
- Can use `readelf -a <FILE>` for details on linux
- [[Virtualization]]

# Disassembled Linux AArch64 ABI Hello World:
![[image (3).png]]
- Note the svc (System call ABI) to generate interrupts

# Def’n: Kernel
- Kernel Mode is a priv. level on your CPU that give access to more instructions, this is S-Mode on RISC-V.
- The Kernel is the part of the OS that runs in this special mode that has access to additional, lower level instructions.
- Something like the Linux kernel would only allow trusted software to interact with the hardware in this mode.

![[image (4).png]]
- We have system calls to interface between User and Kernel Space.

# Traceability
- On linux, we can see every system call that a given process makes.
- use strace `<ELF>` to see

# Microkernels and Monolithic Kernels
- IPC - Interprocess Communication
- Monolithic Kernels have as much as possible within the Kernel, so privilege while writing that software is not an issue, however, that poses issues with security if there are any exploits in that code.
- Microkernels try to mitigate this risk by moving as much as possible into User Mode.

![[image (5).png]]
![[image (6).png]]

Static [[Libraries]] are included