Leveraging Persistence and [[Disks and Drives]]
- Layouts are Directed, Acyclic [[Graphs]] in the case of the **POSIX** Standard which is this where `binary, devices, etc(conf), home, mount` are needed: ![[Pasted image 20241125133106.png]]
# New APIs for this:
``` C
int open(const char *pathname, int flags, mode_t mode);
// flags can specify which operations: O_RDWR, O_WRONLY, O_RDWR
// also: O_APPEND moves the position to the end of the file initially

off_t lseek(int fd, off_t offset, int whence);
// seek changes the position to the offset
// whence (what the offset is relative to) can be one of: SEEK_SET, SEEK_CUR, SEEK_END
// set makes the offset absolute, cur and end are both relative
```
# PCBs from [[Process Management]] can be used to store File Tables
- File Descriptors are really indices within this table
![[Pasted image 20241125134021.png]]

# Local/Global Open File Tables (LOFs/GOFs)
- on fork, both resulting PCBs have access to the same GOF Table Entry
- we should only use `open()` after `fork()`ing
- Every PCB has it's own LOF Table and Entries (the `fds` for the [[Processes]])
![[Pasted image 20241125135024.png]]

| This                                                                           | That                                 |
| ------------------------------------------------------------------------------ | ------------------------------------ |
| `open("todo. txt", O_RDONLY);`<br>`fork();`<br>`open ("b.txt", O_RDONLY);`<br> | ![[Pasted image 20241125140247.png]] |

# Allocation Types
| Contiguous                                                                                                                                                                                                                                                                                         | Linked                                                                                                                                                             | File Allocation Table (FAT)                                                                                                                 | Indexed                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - Fast assuming no reallocations / File size changes<br>- Fast Random Access: $\text{block} = \lfloor\frac{\text{offset}}{\text{blocksize}}\rfloor$<br>- Some degree of internal fragmentation (within a block)<br>- High degree of external fragmentation when file deletion or truncation occurs | - Space efficiency: only need to store the head of a file and traverse for everything else<br>- Slow random Access as next pointers are stored on different blocks | - Like a Linked Allocation method but now all of our [[Linked Lists]] pointers are present of the same block so the Random Access if Faster | - Direct mapping of each block but now we have some blocks that are responsible for storing pointers to other blocks that constitute a file<br>- This is Identical to single level [[Page Tables]] |
| ![[Pasted image 20241125141315.png]]                                                                                                                                                                                                                                                               | ![[Pasted image 20241125141356.png]]                                                                                                                               | ![[Pasted image 20241125141420.png]]                                                                                                        | ![[Pasted image 20241125141459.png]]                                                                                                                                                               |
