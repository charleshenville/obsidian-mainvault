# There are Preemptible and Non-preemptible Resources
- A method of [[Process Management]]

A **preemptible** resource can be taken away and used for something else e.g. a CPU The resource is shared through scheduling A **non-preemptible** resource can not be taken away without acknowledgment e.g. disk space The resource is shared through allocations and deallocations Note: Parallel and distributed systems may allow you to allocate a CPU

# The scheduler runs whenever a process changes state

## Scheduling Metrics of Success
- Minimize waiting/idle time
- max cpu util
- max throughput → as many processes as possible
- Fairness → distribute process resources evenly

# First Come, First Serve (FCFS)
- Nothing special, just serve the processes that come first first and make all other processes wait for their turn.
- This may be inefficient if we put long jobs first

# Shortest Job First (SJF)
- Serve the shortest job first
- Unrealistic and not practical
    - We may starve long jobs
    - we don’t know the burst time of processes

# Shortest Remaining Time First (SRTF)
- This turns out to be better than SJF

# Round Robin (RR)

- First actual practical scheduling algorithm
- Uses a FIFO system that gets updated after a collection of time units (a quantum)
    - If $P_i$ executes for a quantum, but it still needs to do more work, we it has to be sent to the back of the queue and wait to be executed for some quanta.
    - We always prefer the newly arriving process when it is ambiguous (arrival at the end of a quantum). New arrivals do not get to skip ahead in line.

# Generally, Scheduling with different algos and params involves tradeoffs between:

- Response Time
- Waiting Time
- Context Switches