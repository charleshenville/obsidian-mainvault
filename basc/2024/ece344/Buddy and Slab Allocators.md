Method of [[Memory Allocation]]

# Buddy Allocators -> Rounding Up $$\text{space allocated} = 2^{\lceil\lg(\text{space requested})\rceil}$$
![[Pasted image 20241205195951.png]]
- Reduces external fragmentation
- used in Linux
- goal is to try and coalesce where possible

# Slab Allocators -> Fixed Sized Allocation
- Allocate same-sized objects from dedicated pool
- Every type has its own pool eg. structs, ints, classes, etc.
- Slabs can be allocated using buddy allocators
![[Pasted image 20241205201054.png]]

