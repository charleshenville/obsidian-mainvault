# Note that Applications may pass through several Library layers
- Something like a GUI → Sys. daemon → libc making system calls to the Kernel. all of this would be running in user space.

# Dynamic Libraries
- Like the C standard library → `.so`
    - A collection of `.o` files containing function definitions; Multiple applications can use the same `.so` we only have to load [`libc.so`](http://libc.so) in memory once and share it to all process instances.
# Static vs Dynamic Libraries
- For static libraries, we have to essentially create a copy of it for every application that uses it
- In the case of dynamic, we can have a reference to it that all applications can use.
    - This can cause issues in the case that we change dynamic library source and break it; we not have all depending applications breaking as well.

# Semantic Versioning
- MAJOR.MINOR.PATCH
    - Both Minor and Patch changes would be backwards compatible.

![[image (7).png]]![[image (8).png]]
