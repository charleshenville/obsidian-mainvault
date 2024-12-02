Implementing [[Page Tables]]
# We will continue with our implementation of Page Tables (With LN…L0 Page Tables (usually 3 levels in modern machines))

$$ \text{No. Levels} = \left\lceil\frac{n_\text{virtual bits}-n_\text{offset bits}}{n_\text{index bits}}\right\rceil $$

# Alignment

- Everything is aligned every `4096` bytes ex `0x7000` to `0x7FFF`, start is divisible by 4096.

# Translation Look-Aside Buffer (TLB)

- Serves to cache Page Table Entries (PTEs) to make things
- Saving a single result for future use once we’ve used it once (in the case that it isn’t already there)

![[image (15).png]]

# Effective Access Time

- Proves that this caching method is (almost) as good as just using physical memory straight-up.
- $\alpha\in[0,1]$ represents the percentage of accesses that we hit in the TLB

$$ \text{EAT}=\alpha(\text{TLB HIT TIME})+(1-\alpha)(\text{TLB MISS TIME}) $$

- Note that to either hit or miss we need to run a **TLB_Search**

# But what happens when we context switch if we only have one TLB?

- We’ve gotta flush that jawn.
- Sometimes when we load the base page table we also flush the TLB