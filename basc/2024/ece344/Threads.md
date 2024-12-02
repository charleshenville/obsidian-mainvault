# Concurrency vs Parallelism

- Switching between many things vs doing many things simultaneously

# Threads `#include <pthread.h>`

- Like processes but with shared memory
- Exact same address space (this can be dangerouse!!!@_@)
- have its own stack and registers

```c
int pthread_create(pthread_t* thread, 
										const pthread_attr_t* attr, 
										void* (*start_routine)(void*),
										void* arg);
										
// note that void* (*start_routine)(void*) denotes a function that has
// parameter of void pointer and returns a void pointer

// This is like wait but for threads
int pthread_join(pthread_t* thread, void** retval);

// Like exit for threads
void pthread_exit(void *retval);
```