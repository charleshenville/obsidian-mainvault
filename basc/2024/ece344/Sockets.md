Another form of [[Basic IPC]] but between computers

We have different steps when thinking about servers vs clients.

# Servers - 4 steps
- `socket` creates the socket
- `bind` attaches the socket to some location
- `listen` indicates you’re accepting connections - sets the queue (how many connections can we old onto before dropping) limit
- `accept` returns the next incoming connection to handle as a fd - note this syscall blocks until there exists a connection!

# Clients - 2 Steps
- `socket` creates the socket
- `connect` connects to some location and we can now do TX/RX

# TCP
- All data from clients appears in same order on server
- Forms persistent connection
- Reliable but slow - keep track of order, do ACKs, etc.

# UDP
- No guarantee on order
- Sends messages faster but we can drop some