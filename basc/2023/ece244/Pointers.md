## Cell Memory Type

|[[Hexadecimals]] Adress|8-bit Cells|
|---|---|
|0x00||
|0x01||
|0x02||

|Heap: Dynamically Allocated Memory|
|---|
|Allocated manually; must be explicitly freed by the programmer to avoid memory leaks.|
||
|Stack: Localized variables of functions|
|Allocated for a function and freed automatically…,|
||
|Data: Global variables|
||
||
|Code: exe instructions|
||
||

## Pointers Used to [[Pass by Pointer]]:

- Stores an adress to a byte.
- `int*` would point to the 1st byte of an integer variable.

```cpp
int main(){

	int x;
	int *p, y; // p is a pointer, y is a variable.
	
	x = 7;
	p = NULL; // Null pointer
	p = &x; // p = Adress of x.

}
```

### We must specify the data type a pointer points to to determine how many bytes we should read after the first one which we are pointing to (Proper De-Referencing).

### For Integers and single-valued data types:

```cpp
p = new int; // adress on the heap is returned by new.
*p = 3;
delete p; // Equivalent to deallocating memory at adress p.
p = nullptr; // Good practice to do this after deallocation although not entirely necessary.
```

```cpp
int *pNum  = new int;
delete pNum;
pNum = NULL;
```

### For Arrays:

```cpp
int *arr = new int[10]; // 10 here can also be a variable since we are dynamically allocating
delete [] arr;
```