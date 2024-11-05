with [[Time Complexity Analysis]]
# Heapsort (In-Place Sorting)

## Heap Properties 
![[IMG_D0C2DF1A380B-1.jpeg]]
### Heap Shape
- Complete tree with elements tending to the LHS

### Heap Order:
- key($\forall$parent) > key($\forall$child)

# Bubble-Down (i) -> $O(\log n)$
```
repeat
	swap(A[i]) with biggest of:
		 A[2i], A[2i+1]
until no more swaps can be made
```

# Build Heap (A) -> $O(n\log n)$
```
for i from floor(length(A)/2) to 1
	BubbleDown(A[i])
```

# Max Extract (A) -> $O(\log n)$
```
swap A[1] with A[length(A)]
	BubbleDown(A[1])
```

# Heap Sort (A) -> $O(n\log n)$
```
BuildHeap(A)
	for i=1 to length(A)
		MaxExtract(A)
```

# Bubble Up (A)
- inverse of bubble down

# Insert Key (A,i)
```
length(A) += 1
A[length(A)] = key, BubbleUp
```
