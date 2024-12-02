
# Monitors
- exist in some OOPs as [[Mutexes]] that exist in all objects that are added at compile time to simplify things.

# Dealing with `pthread_cond_t *cond`s (Condition Variables)
- Like [[Semaphores]] but even more general
- Must be paired with [[Mutexes]]
- Creating [[Queues]] of [[Threads]] with [[Locks]]
	- Waits for something to become `True`
- `signal()`, `broadcast()`, `wait()`

## Threads calling `wait()`
- added to the cv q
- unlocks mtx
- gets blocked

## Threads calling `wait()` but now called on by `signal()` or `broadcast()`
- gets unblocked
- tries to again lock mtx
	- return from `wait()` on success of this

# Locking Granularity
- How much code is between a locking and unlocking call
- Must consider overhead, contention, and deadlocks (no threads can make any progress)
	- The more locks we have, the more we must worry about deadlocks.
- Usually the smaller the grains the better, but there is some noticeable overhead while locking.
	- Memory allocation, init and destructing locks.
