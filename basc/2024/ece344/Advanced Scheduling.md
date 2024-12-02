An extension of [[Scheduling]]
# Adding Priorities to Our Schedules

- Run higher priorities first (`int \\in -20,19` ) where 19 is lowest priority.
- Do a Round Robin on Processes with the same priority
- We can also dynamically assign priorities and do priority inheritance in case there are other dependencies (high pri. waits on low pri.)
- We can also account for Foreground vs Background

# Per-CPU Schedulers

- One scheduler for each cpu/core
- Better than global scheduling in everything other than load imbalances

# Global AND Per-CPU

- We have a per-cpu base scheduler but a global alternative that oversees all operations

# Gang/Co Scheduling

- Can treat processes that depend on each-other
- Requires global context-switching across all CPUs and cores

# Real-Time Scheduling

- This just imposes time constraints on processes, for critical real time tasks like audio/video rendering or autopilot.
- We use soft-real-time scheduling on Linux that just gives critical processes higher priority (alongside FCFS and RR). In practice real time processes are always prioritized

# Ideal Fair Scheduling vs Completely Fair Scheduling

- Ideal assumes we have infinitely small context switching overhead and gives all concurrent processes an equal amount of runtime in a small quantum.
- Completely (what is used in practice) assigns a virtual (because it is adjustable based on priority but still monotonically increases) runtime to make a more informed decision on when it can be switched out. (Based on lowest v. runtime).
- Decisions are made after each time slice in both cases
- The CFS Is implemented with Red-Black (Self-balancing BSTs) Trees keyed by v. runtime giving $O(\lg n)$ insert, delete, update find minimum with nanosecond fidelity/granularity.
- CFS tends to favour I/O bound processes by default.

We can also use [[Scheduling]] on [[Threads]]