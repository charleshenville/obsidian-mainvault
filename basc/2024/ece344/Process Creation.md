![[IMG_851D3CE0FCEA-1 (1).jpeg]]

# Process Control Block (PCB)
- Can browse `task_struct` for Linux on GH containing:
    - Process state
    - CPU registers
    - Scheduling information
    - Memory management information
    - I/O status information
    - Any other type of accounting information

# The Process State Diagram
- Waiting synonymous with ready
![[image (9).png]]
- You can read this state attached to any process through the `/proc` directory on linux
    - Not actually files in a directory, just looks like it.

# Creating Processes from ~~Scratch~~ a Clone
`int fork(void)` as the following API:
- Returns the process ID of the newly created child process
- 1: on failure, 0: in the child process, >0: in the parent process

# Fork Example
```c
int main(int argc, char *argv[]) 
{
	pid_t returned_pid = fork();
	if (retured_pid == -1) {
		int err = errno;
		perror("fork failed");
		return err;
	}
	if (returned_pid == 0) {
		printf("Child returned pid: %d\\n", returned_pid);
		printf("Child pid: %d\\n", getpid());
		printf("Child parent pid: %d\\n", getppid());
	}
	else {
		printf("Parent returned pid: %d\\n", returned_pid);
		printf("Parent pid: %d\\n", getpid());
		printf("Parent parent pid: %d\\n", getppid());
	}
	return 0;
}
```

# Note this would be executed in both copies of the forked process. The Original (Parent) and child.

NAME `getpid`, `getppid` – get parent or calling process identification

SYNOPSIS `#include <unistd.h>`

```
 pid_t
 getpid(void);

 pid_t
 getppid(void);
```

DESCRIPTION `getpid()` returns the process ID of the calling process. The ID is guaranteed to be unique and is useful for constructing temporary file names.

```
getppid() returns the process ID of the parent of the calling process.
```

ERRORS The `getpid()` and `getppid()` functions are always successful, and no return value is reserved to indicate an error.

# Replacing the Process with Another Program
- `execve`
- `pathname`: Full path of the program to load
- `argv`: Array of strings (array of characters), terminated by a null pointer
    - Represents arguments to the process
- `envp`: Same as `argv`
    - Represents the environment of the process
- Returns an error on failure, does not return if successful

# Execve Example
```c
int main(int argc, char *argv[]) 
{
	printf("I'm going to become another process\\n");
	char *exec_argv[] = {"ls", NULL};
	char *exec_envp[] = {NULL};
	
	int exec_return = execve("/usr/bin/ls", exec_argv, exec_envp);
	
	if (exec_return == -1) {
		exec_return = errno;
		perror("execve failed");
		return exec_return;
	}
	
	printf("If execve worked, this will never print\\n");
	return 0;
}
```