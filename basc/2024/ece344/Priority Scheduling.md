Another method of [[Advanced Scheduling]]
# Dynamic Priority Scheduling

- See [[Scheduling]]
- Low Priority processes can get reprioritized
    - Inc. Priorities that don’t use time slice
    - Dec. Priorities that use time slice
- The following steps should be taken at each time slice
    - Record how much time a given process with priority $P_n$ executes for and call it $C_n$
    - $P_n = \frac{P_n}{2}+C_n$: observe that this results in a lower priority if C_n is small
    - $C_n=0$

![[image (18).png]]
![[image (16) 1.png]]
# New System call: `mmap()`
![[image (17).png]]