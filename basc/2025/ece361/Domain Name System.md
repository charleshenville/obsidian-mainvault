This is out distributed, hierarchical, database that contains all the mappings from human names to 23 bit [[IP Address]]es. Obv Not centralized because of traffic and scaling.
![[Pasted image 20250126234721 1.png]]
## Services
- address translation
- canonical host aliasing (like redirects)
- mail server aliasing
- load distribution

## Local Name Servers
- Proxies for root DNS servers, can cache things too. Every ISP has one at an org-level.

### Recursive vs Iterated Queries
![[Pasted image 20250127001820 1.png]]
![[Pasted image 20250127001834 1.png]]
- A Note on caching here is that it can happen anywhere within the heirarchy or just at the local level.

# DNS (Resource) Records
- useful when adding new records to the DNS db. We insert NS and A type records.
![[Pasted image 20250127003808 1.png]]
![[Pasted image 20250127002143 1.png]]
![[Pasted image 20250127003523 1.png]]
### msg header
**identification**: 16 bit # for query, reply to query uses same #
**flags**:
- query or reply
- recursion desired
- recursion available
- reply is authoritative

Note: DNS Uses UDP for its fast response times and low overhead since DNS Servers often serve many (low-data) packets.

