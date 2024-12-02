[[Process Creation]], [[Process Management]]

# Uniprogrammming vs Multiprogramming
- One process running at a time ( series ) vs many running in parallel.
- Modern OSs tend to run everything in parallel concurrently.

# Scheduler Responsibility
- OS must load process into memory to instantiate it
- When waiting - Scheduler decides when it gets to run (interesting mechanic)
- Runs on a core loop (`CONTEXT SWITCHING`) that is purely overhead and should be minimized:
    1. Pause process currently running
    2. Save paused state to come back later
    3. Get next scheduled process to run
    4. Load next process’ state
- We can let the processes choose when to pause or let it be handles by OS, generally we choose the latter.

# The `pipe()` syscall (API)

```c
int pipe(int pipefd[2]);
// Returns 0 on success, and -1 on failure (and sets errno)

// pipe forms a one-way communication channel using two file descriptors
	// pipefd[0] is the read end of the pipe
	// pipefd[1] is the write end of the pipe
	// pipe pipes pipefd[1] --> pipefd[0] explicitly
// You can think of it as a kernel managed (big) buffer
	// Any data written to one end can be read on the other end
```

# A note on File Descriptors in [[Filesystems]]
- like a pointer to a file
- if we create a pipe with `pipe` and then `fork`, we have essentially created a way for the parent to communicate with the child or vice-versa via the read and write ends of the pipe.
- The `read()` syscall is blocking, meaning that it blocks execution of subsequent instructions until `nbytes` are read or until `eof` is reached (`^D`).
- All file descripors for a process are closed upon exit. close fds as soon as you’re done with them.