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
