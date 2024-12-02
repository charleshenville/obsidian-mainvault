In the contexts of [[Threads Implementation]]
# Preventing Data Races
- Can occur when sharing data - when two concurrent actions access same var with at least one being to write
- We can detect these by looking at execution order between two threads

# Atomic Operations
- indivisible (assume)
- either happens or doesnt
- preemptability between atomic instrs

# Three Address Code (TAC)
- intermediate compiler lang from c to asm
- Used for analysis and optimizations by compilers
- gcc uses `GIMPLE`

# Mutual Exclusions ([[Mutexes]])
- we can lock/unlock with these objects. Protected code is a critical section

![[image (20).png]]
- note the lock here is blocking, we also have `pthread_mutex_trylock` that doesn't block.

# Sync Layering
![[image (21).png]]
- primitives ⇒ mutexes