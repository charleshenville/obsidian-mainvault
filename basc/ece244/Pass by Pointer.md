Swapping two variables from the parent function.

``` C++
#include <iostream>
#include <string>
using namespace std;

// Function Decleratorions

void swap(int, int);
void properSwap(int*, int*);

// Best practice to place main here;

int main(){

	int a = 7, b = 13;
	cout << "Before Swapping: a = " << a << ", b = " << b << endl;
	
	swap(a, b); // Does not work as intended
	properSwap(&a, &b); // Works as intended

	return 0;

}

// Will not change anything in main
void swap(int x, int y){

	int temp = x;
	x = y;
	y = temp;
}

// Works as intended
void properSwap(int* pa, int* pb){
	
	int temp = *pa;
	*pa = *pb; // *(&a) = *(&b)
	*pb = temp;

}
```

|**main**| 
|-|-|
|~~7~~ → 13|a|
|~~13~~ → 7|b
|**properSwap**||
|&a|pa|
|&b|pb|
|7|temp|



