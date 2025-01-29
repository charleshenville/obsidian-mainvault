- Peer-to-peer at [[The Application Layer]]
	- This is what BitTorrent uses
	- no always-on server system
![[Pasted image 20250127111300.png]]

## Distribution Times

### For File-Server
![[Pasted image 20250127111443.png]]
# $$D_{cs}\geq\max\left\{\frac {NF}{u_s}, \frac{F}{d_{\min}}\right\}$$
- $N$ file copies transmitted by server

### For P2P File Sharing
- Number of file copies can increase exponentially
![[Pasted image 20250127111914.png]]
# $$D_{cs}\geq\max\left\{\frac{F}{u_s}, \frac{F}{d_{\min}},\frac {NF}{u_s\sum_{i=1}^Nu_i}\right\}$$
![[Pasted image 20250127112214.png]]

## Centralized Approach
- Have a server that serves as a dictionary to help us find recipients and distributors for particular files.

## Fully Distributed Approach (**Flooding**)
- Ask through the network for a member who has the desired file.
- This isn't an efficient use of bandwidth
- Not scalable

# Distributed Hash Tables (DHT)
- Method to construct a distributed database
- Assign integer identifier to each peer in the network as a member of the db $[0-2^{n-1}]$
![[Pasted image 20250127114432.png]]
- More records as you increase the ID
### Circular DHT
- Overlay network as each peer is only aware of successor and predecessor. $\mathcal{O}(n)$ [[Time Complexity Analysis]].
![[Pasted image 20250127114618.png]]
### Adding shortcuts
- Makes it $\mathcal{O}(\log n)$ as we now keep track of distant successors (short cuts)

### Peer Churn
- Now each network member is aware of its two successors (ping periodically to check if live)
- We can now handle a node leaving the network
![[Pasted image 20250127114929.png]]
- If we want to add a node, we simply send a message informing the network and let it propagate until it finds our place for us.
![[Pasted image 20250127115051.png]]
## BitTorrent
- file divided into 256kB chunks and distributed after successively
- can request/send file chunks to/from the net
- when receiving/requesting - we prioritize rare chunks
- when sending - we send chunks to top 4 peers currently sending us chunks at highest rate - otherwise the peer is choked
- every 30 seconds though we we **optimistically unchoke** another peer and they may join top 4 (**tit-for-tat**)
