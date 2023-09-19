In C, we had to [[Pass by Pointer]], now with [[References]] we can Pass by reference with C++.

``` C++
#include <iostream>
#include <string>
using namespace std;

// Function Decleratorions

void properSwap(int&, int&);

// Best practice to place main here;

int main(){

	int a = 7;
	int b = 13;
	cout << "Before Swapping: a = " << a << ", b = " << b << endl;
	
	properSwap(&a, &b); // Works as intended
	
	cout << "After Swapping: a = " << a << ", b = " << b << endl;

	return 0;

}

// Look at how simple and brilliant this is!

void properSwap(int& x, int& y){
	
	int temp = x;
	x = y; // *(&a) = *(&b)
	y = temp;

}
```
