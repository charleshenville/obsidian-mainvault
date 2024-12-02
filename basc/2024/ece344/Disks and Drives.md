This is a way to practice **Persistence**
- like [[Memory]] but is slower and persists after power cycling

# Solid State Drives (SSDs)
- Organized by [[Page Tables]]
![[Pasted image 20241125122435.png]]
- Assume 4KB pages for this course but they can be any size and dont have to match up with a memory page size (can be larger by a constant factor)
- The `TRIM` Command lets us as the Operating System to inform the SSD that we no longer need a given block of data so it can be erased during idle time so it is hopefully erased for us when we need to write data to it.

Constraints
- must be erased at a block level
- must be erased before we can overwrite

# SLEDs/RAIDs:
- Single Large Expensive Disks or Redundant Array of Independent Disks
- One point of failure for SLED and many for RAID although we have redundancy to prevent data loss.

| **RAID 0** - A Striped Volume                                                                              | **RAID 1** - A Mirrored Volume                                                                                                                                                   | **RAID 4**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | **RAID 5**                                                                                                                                                                                                                                                                                      | **RAID 6**                                                                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - Good throughput/performance<br>- Bad Redundancy (none, actually)<br>- $N$ Disks -> $N\times$ performance | - Decent Performance <br>- Fast Reads and slow writes as we have to write to many places<br>- Excellent Redundancy <br>- A whole drive or many drives can fail without data loss | - Introduces Parity<br>- Disks 0-2 are Striped like in RAID 0 but the extra disk is there to ensure that if we lose one of them we maintain data integrity<br>- Must have at least 3 drives<br>- We use `XOR` reconstruction here to figure out what bit of info we have lost.<br>- This only works if just one of the other drives fails, and else we have data loss<br>- $N$ Disks -> $(N-1)\times$ performance<br>- Write performance can suffer as we have to write to parity all the time<br>- Usable $(1-\frac{1}{N})\times$ the total storage | - Like RAID 4 but just with distributed Parity this time (better than RAID 4)<br>- Properties are very similar to that of RAID 4<br>- Write performance is slightly improved and we have a lower chance of wearing out a single parity drive as we now can have many of them to distribute load | - We now have another disk worth full of parity information<br>- Like RAID 5 but just with more redundancy<br>- We can now lose two data disks and still recover/reconstruct the information<br>- Needs at least 4 drives<br>- Usable $(1-\frac{2}{N})\times$ the total storage |
| ![[Pasted image 20241125123202.png]]                                                                       | ![[Pasted image 20241125123724.png]]                                                                                                                                             | ![[Pasted image 20241125124205.png]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | ![[Pasted image 20241125125633.png]]                                                                                                                                                                                                                                                            | ![[Pasted image 20241125125910.png]]                                                                                                                                                                                                                                            |
# XOR Reconstruction
- The result of `XOR`-ing three bits is 0 in the case that the sum is even and 1 if odd. Thus we know how to reconstruct the disk array if one of the things from the sum is missing.

# Disk Hierarchies and Combos
``` mermaid
graph TD
x["RAID 1"]
y1["RAID 0"]
y2["RAID 0"]

subgraph ..
d11[("Drive")]
d12[("Drive")]
d13[("Drive")]
end

subgraph .
d21[("Drive")]
d22[("Drive")]
d23[("Drive")]
end

x --> y1
x --> y2

y1 --> d11
y1 --> d12
y1 --> d13

y2 --> d21
y2 --> d22
y2 --> d23

```
- This is a RAID 0+1 Partitioning Scheme


``` mermaid
graph TD
x["RAID 0"]
y1["RAID 1"]
y2["RAID 1"]
y3["RAID 1"]

subgraph .
d11[("Drive")]
d12[("Drive")]
end

subgraph ..
d21[("Drive")]
d22[("Drive")]
end

subgraph ...
d31[("Drive")]
d32[("Drive")]
end

x --> y1
x --> y2
x --> y3

y1 --> d11
y1 --> d12

y2 --> d21
y2 --> d22

y3 --> d31
y3 --> d32

```
- This is a RAID 1+0 Partitioning Scheme