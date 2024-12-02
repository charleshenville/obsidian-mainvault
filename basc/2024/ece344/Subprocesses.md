New [[Processes]]
# Alternative to `execve()`

```c
int execlp(const char *file, const char *arg /* ..., (char *) NULL */);
// Doesnt return on success but -1 on fail (setting errno)
// Notice how we no longer have to use string arrays here
// Searches $PATH to search for executables
```

# Final `dup()` APIs

- `int dup(int oldfd);`
- `int dup2(int oldfd, int newfd);`
- These return a new file descriptor upon success and -1 on failure setting `errno`.
- `dup` returns the lowest fd
- `dup2` atomically closes `newfd` if open and makes `newfd` refer to the same thing as `oldfd`

# Sending and Receiving Data from processes

While going through this course we have to remember to be responsible parents and call `wait(pid)` on our children to prevent them from becoming orphans or zombies.