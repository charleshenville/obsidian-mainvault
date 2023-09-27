## In C, we used Structs:

```c
struct student{
	int ID;
	string name;
}

struct student x;
```

## We expand on this in C++ with the addition of functions.

- We now call class instances Objects. We can now use [[Encapsulation]]. Note that we should define classes in [[Header Macros]] and we can make [[References]] to these new objects just like any other variable.

```cpp
// In some header file: student.h

class Student{
	private: // Access Controller
		int ID;
		string name;
	public: // Access Controller
		void print();
		void setName(string n);
		string setName(string n);
		string getName();
};
```

```cpp
#include "student.h" // The class def'n is in this header
#include <string>
#include <iostream>

void Student::setName(string n){ // Must specify Student here with scope operator "::"
	name = n;
}
string Student::getName(){
	return name;
}
void Student::print(){
	cout << "Name: " << name << "ID: " << ID;
}
```

```cpp
//main.cpp
#include "student.h"

int main(){

	Student x; // Creates an object named x.
	x.setName("Joe");
	x.name = "Joe"; // Will not work as name is a private member of Student: Compile time error.
	Student y;
	
	// if we try:
	x.print();
	// We will see a hot load of garbage under the ID variable!
	// Constructors can help with this.
	
}
```
