## Attribute of a good hash function:

- Maps evenly across the array
- such as `h(k) = k % m`
- h: `k ~→ [0,1,…,m-1]`

Example: `h(k) = k % m` being used for $m=7$:

![[Untitled (6).png]]

## Collisions

- Happen when two or more items map to the same array idx.

## Employing Hashing with Chaining (Open Hashing)

- Each hash table entry now has a pointer to a [[Linked Lists]] of keys that map to the same entry.
- Worst case, O(n). Practically O(1) avg.

![[Untitled (7).png]]