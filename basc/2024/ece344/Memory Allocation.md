# [[Stacks]] are static
# Heaps are dynamic

# Fragmentation
- Wasted space, Dynamic only as we don't have this issue with static stack pointers fro things like normal variables.
- Happens with three requirements
	- Different Allocation Lifetimes
	- Different Allocation Sizes
	- Inability to Relocate Previous Allocations

# Internal vs External Fragmentation
![[Pasted image 20241205153333.png]]

# Allocator Implementations: free list
- Keep track of free blocks by chaining them in a ds
- allocate -> remove large enough block from free list
- deallocate -> add the corresponding block back to the free list, we can merge adjacent blocks.

Best fit: choose the smallest block that can satisfy the request
- Needs to search through the whole list (unless there’s an exact match)
![[Pasted image 20241205153913.png]]
![[Pasted image 20241205153931.png]]
![[Pasted image 20241205154004.png]]

Worst fit: choose largest block (most leftover space)
- Also has to search through the list
![[Pasted image 20241205154015.png]]
![[Pasted image 20241205154028.png]]
![[Pasted image 20241205154038.png]]

First fit: choose first block that can satisfy request
- Tends to leave "average" sized holes