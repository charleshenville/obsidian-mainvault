Hypertext Transfer Protocol is an application in [[The Application Layer]]
- Uses TCP by client initiating connection over port 80 to the host
- Stateless: ie no memory of previous requests
![[Pasted image 20250116162211.png]]

# Uniform Resource Locator (URL)
![[Pasted image 20250116162324.png]]

# Persistent (1.1) vs Non-Persistent (1.0)
- Many objects that can be downloaded over one session vs multiple sessions needing to be init'ed for multiple files/objects.
- Persistent HTTP things can be pipelined whereas Non-persistent cannot be.

# Round Trip Time (RTT)
- Multiple of round trip time + file transmission times for non persistent. If we have two files we must have 2 sessions even if all objects are hosted in the same place.
- Usually need fewer round trips in the persistent case

# Parallel TCP and Pipelining
![[Pasted image 20250116163313.png]]
- Parallel TCP allows for pipelines
![[Pasted image 20250116163350.png]]
- Requests are sent by the client upon referenced object encounters

# What a HTTP Request Message Looks Like
![[Pasted image 20250116164950.png]]
![[Pasted image 20250116165013.png]]

# Request Messages/Types
![[Pasted image 20250116165503.png]]

# Response Messages/Types
![[Pasted image 20250116165559.png]]
![[Pasted image 20250116165613.png]]
![[Pasted image 20250116165622.png]]
