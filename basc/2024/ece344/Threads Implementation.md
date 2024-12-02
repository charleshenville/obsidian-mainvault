Implementation of [[Threads]]
# Implementation Methods

- Either in kernel or user space
    - If in kernel space, it can treat our threads specially (like blocking everything else but at the expense of having to context switch and use syscalls)
- All libraries we use run in user mode - we can have:
    - Many-to-one: threads that are implemented in user space with kernel only acking one process
        
        - Just user space!
        - fast, portable, compatible
        - One thread blocking can cause all threads to block
    - One-to-one: One user thread maps to a kernel acked thread
        
        - In Kernel mode implementation
        - Needs slowe syscall interface
    - Many-to-many: Many user-level threads mapping to kernel acked threads
        
        - The hybrid approach
        - Can get the absolute most out of cpus tho
        - We can just use thread pools that exist within libraries instead and when tasks come in we can give them tasks to do
![[image (19).png]]
# Thread Tables

- exist to support threads

# Thread Nuances

- Linux Kernel only copies the thread that created the fork.
- When a signal is sent to a multithreaded process the kernel picks one at random and just