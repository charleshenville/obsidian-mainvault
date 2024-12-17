Using [[Virtual Machines]] and user processes to emulate operations from [[Kernels]] (Type 2 H.).
# Abstracts entire machines
- Much like [[Processes]] abstract [[Simplified Processor]]s
# Hypervisors
- AKA Virtual Machine Manager (VMM) controls VMs
	- Creation, Management and Isolation privs.
### **Type 1** Hypervisors 
- Bare metal
- Runs on Host Hardware
### **Type 2** Hypervisors 
- Simulation based
- Hosted on the VM -> on the host it looks like an application or process
- Slower but no fancies required

VMs "Run in Hypervisors"
![[Pasted image 20241205204223.png]]

Note they are not emulations
- But they enable us to pause/play
- Good for security as we as the Hypervisor can restrict access to hardware or other memory contents etc.

# Trap and Emulate
- Trap kernel (illegal) instrs and then execute it. slows down native execs.
![[Pasted image 20241206125656.png]]
- an exception here is for special instrs that behave differently depending on them mode. they need binary translation which translate them to a set of instructions with the same end effect

# Hardware Rescue
- ring -1

# Containers, like Docker, Aim to be Faster
The hypervisor sets limits on: CPU time, memory, network bandwidth, etc.
- What if the kernel supported this directly, without [[Virtualization]]?
Linux control groups (cgroups) support hypervisor-like limits for processes
- Isolate a process to a namespace
You can set other resources a namespace can access (mount points, IPC,
etc.)
- Containers are lighter-weight than full virtual machines, they use a normal kernel

### Virtual Machines Virtualize a Physical Machine
• Virtual machines provide isolation, the hypervisor allocates resources
• Type 2 hypervisors are slower due to trap-and-emulate and binary
translation
• Type 1 hypervisors are supported by hardware, IOMMU speeds up devices
• Hypervisors may overcommit resources and need to physically move VM
• Containers aim to have the benefits of VMs, without the overhead