# Mutual Exclusions
- we can lock/unlock with these objects. **Protected code** is a critical section.

![[image (20).png]]
- note the lock here is blocking, we also have `pthread_mutex_trylock` that doesn't block.

Good to think of it as something that can be possessed by a given thread - when we lock, we start possessing it and when we unlock, we stop. Only one thread can possess the mutex at a time.