## Double [[Pointers]]
- Variables that store an address to a pointer (Variable that stores an address to a regular data frag).

Memory Diagram for the following code:

|Heap| |
|---|---|
|0x10|~~5~~→8|
|||
|||
|Stack||
||q|
|0x54|p = 0x10|
|0x55|p2p = &p = 0x54|

```cpp
(int**) p2p // Double pointer Decl'n
int *p, *q;
p = new int; 
*p = 5;

p2p = &p; // LHS and RHS type match

// We can say: 
q=*p2p;
// *(p2p) = *(&p) = p
// Then: q=p is equivalent to this.

*q = 8;

// All are equivalent
cout << *p << endl;
cout << *q << endl;
cout << **p2p << endl;
// **p2p = *(*(&p))

// Suppose we want to free, we should not:
delete q;
delete p;

// We only need as many deletes as news!
delete *p2p;

// Not delete p2p;, this tries to free something that was never dynamically allocated.
```

## Dynamic Memory Allocation of Arrays of Objects using Double Pointers

### Regular:

1. Fixed-Size array

```cpp
int arr[4] = {1,2,3,4}; // Allocated regularly on the stack.

// arr equivalent to &(arr[0])
// *(arr+1) equivalent to arr[1]
```

|1|2|3|4|
|---|---|---|---|

2. Variable-size array

```cpp
int size;
cin >> size;
int arr[size]; // Still allocated on the stack
```

3. Dynamically allocate and later free an array of pointers to integers.

```cpp
int size = 7;
cin >> size;
int * arr = new int [size];
// Useful since we can explicitly define and mutate the lifetime of this array and it's allocation.
// Using delete later:

delete []arr;
arr = NULL; // Just good practice, not necessary (But you should!).

// For an array of pointers to ints:

int** arr = new int* [3];

// Suppose we want to dynamcally allocate space in the heap for all of these pointers in this array:

for(int i=0; i<3; i++){
	arr[i] = new int;
	*(arr[i]) = i+1;
}

// To free everything:

for(int i=0; i<3; i++){
	delete arr[i]; // delete all integers allocated in the array
	arr[i] = NULL; // GP
}
delete []arr;
arr = NULL; // GP

```

We can employ these principles to [[Dynamic Object Arrays]].