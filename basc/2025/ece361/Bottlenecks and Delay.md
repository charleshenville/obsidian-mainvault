What [[Packet Switching]] and [[Circuit Switching]] aim to resolve
# 4 Sources of Packet Delay
![[Pasted image 20250114113431.png]]
- The net delay or nodal delay is simply the sum of these delays

# Packet Queuing Delays
### Define traffic intensity, $\rho$ with Average packet length and arrival rate, over the bottleneck bandwidth of the link$$\rho=\frac{La}{R}$$![[Pasted image 20250114113740.png]]
# Throughput with Bottlenecks
![[Pasted image 20250114114045.png]]

# Internet Protocol Layers (5-7)
![[Pasted image 20250114114204.png]]
1. **Application:** Supporting network applications like HTTP, SMTP, IMAP, Custom enterprise applications, etc.
2. **Presentation/Session:** allow applications to interpret meaning of data, e.g., encryption, compression, machine-specific conventions and then session is synchronization, checkpointing, recovery of data exchange. *These layers are usually just part of the application layer too as it in theory should be responsible for them.*
3. **Transport:** process-process data transfer protocols like TCP, UDP
4. **Network:** routing of datagrams from source to destination IP, routing protocolsouting of datagrams from source to destination IP, routing protocols
5. **Link:** data transfer between neighbouring network elements. Ethernet, 802.11 (WiFi), PPP
6. **Physical:** Actual bits on the physical wire

# Encapsulation Methods
- Each layer adds it's own header
![[Pasted image 20250114115041.png]]
