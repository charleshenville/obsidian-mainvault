One of the [[Network Layers]]
# Run on Hosts
- Do not need them elsewhere

# Servers vs Client
- **Servers** are always-on hosts with an easily index-able/static IP Address
- **Clients** contact/communicate with server and can be intermittently connected. They don't connect directly with each other rather through servers running apps like HTTP, IMAP, FTP.
![[Pasted image 20250116152817.png]]
# Peer to Peer (P2P)
- Peers requests services arbitrarily to other peers
- AirDrop is an Example

# [[Sockets]] are analogous to doors that run on both servers and clients 
- We can identify applications with ports and an [[IP Address]]

# App-Layer Protocol Defines
- Message type, syntax, semantics, rules

# Requirements
- Data integrity, Timing, Throughput (low [[Bottlenecks and Delay]]), Security

## To address requirements we have TCP / UDP:
- Depends on how tolerant we are to loss. We should choose the best protocol...
![[Pasted image 20250116154952.png]]
![[Pasted image 20250116161953.png]]
# TCP 
- Lossless, Reliable, Slow
- Throughput reduction if necessary to prevent loss
- Complicated
# UDP
- loss-Tolerant, Faster, Unreliable

# Transport Layer Security (TLS)
![[Pasted image 20250116162031.png]]