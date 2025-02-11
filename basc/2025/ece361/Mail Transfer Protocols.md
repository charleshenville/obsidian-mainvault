Part of [[The Application Layer]]
- SMTP, IMAP, etc.

# SMTP (Simple Mail Transfer Protocol)
- User agents
- Mail Servers
![[Pasted image 20250126182226 1.png]]
## How it Works
- Transfer happens in phases
	- handshaking
	- message transfer
	- closure
- Command/response interaction (ASCII text <> Status code / phrase)
- Persistent TCP Connections ended with a . on a single line
![[Pasted image 20250126183657 1.png]]
### Message Format
 ![[Pasted image 20250126185951 1.png]]
# Post Office Protocol (POP/POP3)
- Uses TCP again (v3 currently)
- Auth and Transaction Phases
- Can be done via **SSL (Secure Socket Layer @:995)**
- Through the CLI
![[Pasted image 20250126194206 1.png]]

# Internet Message Access Protocol (IMAP)
- TLS (Transport Layer Security @:993, @:143 else)
- Emails left on server until user deletes (unlike where you can store and delete in POP)
![[Pasted image 20250126202542 1.png]]
