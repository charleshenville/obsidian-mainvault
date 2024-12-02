Short for Index Nodes -> function similar to Virtual nodes from [[Filesystems]].
- If we look at an **Indexed Allocation Scheme** From [[Filesystems]] we can see that this functions identically to Multi-Level [[Page Tables]] where we have a variable amount of level depending on the size of the file we want to store.
- This is to meet the performance requirements of the system.
- We want to be efficient for small files while allowing compatibility for large ones.
![[Pasted image 20241125214601.png]]

# Soft Links - `ln -s todo.txt b.txt`
- Paths to another file (name to name)
![[Pasted image 20241125235208.png]]
- SL (Symlink) targets do not need to exist
- Targets can be deleted without notice of SL
- Unresolvable softlink -> error/exception

# Hard Links - `ln -s todo.txt b.txt`
- Paths to a given inode (name to inode)
![[Pasted image 20241126144721.png]]

# In UNIX everything is a file
- directories, devices, pipes, sockets, etc.

# Inode Contents
- No filename (in dir)
- No parent/relative path information (in dir) - file can be in many dirs
- Yes to File Size
- Yes to File Type
- No knowledge of softlinks to file
- Yes to knowledge of hard links to file excluding the location of them (in dir)
- Yes to access rights and timestamps
- Yes to pointers to file contents but no to the actual file contents (but sometimes yes)
- Yes to ordered list of data blocks (pointers to them)

# [[Caches]] in [[Filesystems]] can Speed Up writing to [[Disks and Drives]]
- [[Threads]] in [[Kernels]] (Daemons) 
- `flush()` and `sync()` syscalls are used here to trigger permanent writing to [[Disks and Drives]].

Removing a file on UNIX [[Filesystems]]:
- Remove the directory entry
- Releasing the inode into the pool of free inodes
- Returning the used disk blocks into the pool of free disk blocks

# Journaling Filesystems (macOS)
- Ensure that if a crash occurs between the above steps that we can recover from it and ensure no storage leaks (journals contain operation in progress)