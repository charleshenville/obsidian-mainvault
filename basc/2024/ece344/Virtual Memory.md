A method of [[Virtualization]]
# Need a way to map virtual addresses to physical ones.
- Remember here that memory is byte addressable

# Segmentation/ Segments (Coarse Grained)
- Partitioning of virtual memory space into segments for code, data, stack, heap
- These can be large and costly to relocate
- Obsolete

# MMUs and Pages
- Memory Management Units do the task at the start of this note
- We usually divide memory up into static-sized pages (`4096` bytes usually (`0x1000000000000` bytes)!)

# VPN → PPN for 64-bit systems (we don’t use everything)
![[image (11).png]]![[image (12).png]]
