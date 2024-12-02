When we care about the order of our [[Threads]].
# How semaphores work
- They are an integer value that is always $\geq$ 0
- Two atomic functions
	- `wait`: decrements the integer (unless already zero in which case it waits and blocks until the semaphore is incremented by another thread)
	- `post`: increments the value

```C
#include <semaphore.h>

int sem_init(sem_t *sem, int pshared, unsigned int value)
int sem_destroy(sem_t *sem); 
int sem_wait(sem_t *sem);
int sem_trywait(sem_t *sem);
int sem_post(sem_t *sem);
```

Can be used to implement a Mutex (from [[Locks]]) If we want
- init with 1
- wait as a lock
- post as an unlock