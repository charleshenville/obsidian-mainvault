![[Pasted image 20241205132739.png]]
# Trade-offs between Speed and size
- Larger things are slow
- Akin to [[Caches]]
- Goal is to hide the hierarchy from the user

Page replacement deals with exchanging Pages from [[Page Tables]] between memory and disk.

## Demand Paging
- using memory as cache for [[Filesystems]]
- Processes' working sets should fit in Mem else we get **Thrashing**

## Page Replacement Algos
Optimal
- Replace the page that won’t be used for the longest
Random
- Replace a random page
First-in First-out (FIFO)
- Replace the oldest page first
- this is worse for more memory counter-intuitively
Least Recently Used (LRU)
- Replace the page that hasn’t been used in the longest time
- implemented with a clock/counter (but is slow)
- could use a linked list but will be slow due to ptr updates


