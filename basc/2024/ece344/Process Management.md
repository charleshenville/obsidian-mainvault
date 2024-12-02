Leveraging methods of [[Process Creation]]
# Process States
	Running and runnable/waiting
	Interruptible Sleep
	Uninterruptible Sleep
	Stopped
	Zombie

# We can think of all processes coming from one, forming a tree

- The first one is `init` - the kernel runs this whenever the UNIX machine first boots up. PID of 1.
- All still use independent [[Virtual Memory]]

![[image (10).png]]

- `htop` can get you a good visualization of this

# Process Responsibility

- Parent processes are responsible for it’s children
- When processes terminate by calling `exit()`
    - if child exits first → zombie process
    - if parent exits first → orphan process

# The `wait()` system call

- returns `pid`
- `status`: Address to store the wait status of the process
- **Returns the process ID of child process**
    - -1: on failure (like in the case that we do not have any children )
    - 0: for non blocking calls with no child changes
    - > 0: the child with a change
        

The `wait status` contains a bunch of information, including the exit code. You can use `waitpid` to wait on a specific child process

```c
int main(int argc, char *argv[]) {
	pid_t pid = fork();
	if (pid == -1) { return errno; }
	if (pid == 0) {
		sleep(2); // This is so that the child process takes 2 seconds to execute
	}
	else {
		printf("Calling wait\\n");
		int wstatus;
		pid_t wait_pid = wait(&wstatus);
		if (WIFEXITED(wstatus)) {
			// We should see this after 2 seconds
			printf("Wait returned for an exited process! pid: %d, status: %d\\n",
			wait_pid, WEXITSTATUS(wstatus));
		}
	}
	return 0;
}
```

# Zombie Process Example

- Zombies (Child processes that have exited) must be acknowledged as terminated by their parent
    - Parent must read the exit status of the child

```c
int main(void) {
  pid_t pid = fork();
  if (pid == -1) {
    return errno;
  }
  if (pid == 0) {
    sleep(2);
  }
  else {
    int ret;
    sleep(1);
    printf("Child process state: ");
    ret = print_state(pid); // Searches the proc directory for pid pid and prints it state
    if (ret < 0) { return errno; }
    sleep(2);
    printf("Child process state: ");
    ret = print_state(pid);
    if (ret < 0) { return errno; }
  }
  return 0;
}
```

# Orphan Process Example

- Orphans need new parents: default is `init` ; it is like an orphanage.

```c
int main(void) {
  pid_t pid = fork();
  if (pid == -1) {
    int err = errno;
    perror("fork failed");
    return err;
  }
  if (pid == 0) {
    printf("Child parent pid: %d\\n", getppid());
    sleep(2);
    printf("Child parent pid (after sleep): %d\\n", getppid());
  }
  else {
    sleep(1);
  }
  return 0;
}
```