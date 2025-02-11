A form of Web [[Caches]] - Handling [[Cookies]] with [[HTTP]]
- The goal is to not involve the origin server/cluster whenever possible
![[Pasted image 20250120121108 1.png]]
- Cache typically installed by ISP
![[Pasted image 20250120121942 1.png]]
# Verifying Recency
- We (as origin) do not send any objects if $\exists$ up to date objects in cache.
- Cache specifies the date of cached copy
- Cache asks the origin if it is up to date
![[Pasted image 20250120122848 1.png]]