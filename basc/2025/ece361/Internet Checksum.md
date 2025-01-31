In a UDP Segment
![[Pasted image 20250130155335.png]]

### GOAL: To detect error in transmitted segment
- Sender computes checksum via a ones compliment sum of other fields
- We know wether or not this is implemented if we check the checksum field and it is set to all zeros - in that case we know that it is not implemented.
![[Pasted image 20250130161809.png]]
$$0 = b_0 + b_1 + b_2+ ...+ b_{L-1} + b_L (\%2^{16}-1)$$
