Implementation of [[Locks]]
![[image (22).png]]
- Note that for this to work we have to make the `compare_and_swap` function atomic, happening all at once at the hardware level. It returns the original pointed to value, but swaps if that value is the second param, changing it to new.
- This is a **spinlock**
	- As it is strictly blocking

There are things we can do if we don't want to just block all the time, like implementing yielding and queueing
![[image (23).png]]
![[image (24).png]]
# Two-Variable Fix to the Above

```c
typedef struct {
	int lock;
	int guard;
	queue_t *q;
} mutex_t;

void lock(mutex_t *mtx) {
	while(compare_and_swap(mtx->guard, 0, 1); // Block
	if(!mtx->lock) {
		mtx->lock = 1; // get the mutex
		mtx->guard = 0;
	} else {
		enquque(mtx->q, self);
		m->guard = 0;
		thread_sleep();
		// we find ourselves here when we have the lock on wakeup
	}
}

void unlock(mutex_t *mtx) {
	while(compare_and_swap(m->guard, 0, 1)); // Block
	if(queue_empty(mtx->q)) mtx->lock = 0;
	else thread_wakeup(dequeue(mtx->q));
	mtx->guard = 0;
}
```

### Note we can still have as many readers to a critical section as we want and we can implement these r/w locks with additional reader guards.

- should use these if we know we have alot of readers
- We need kernel support for wake up notifs