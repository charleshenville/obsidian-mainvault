## To pass parameters into constructors for [[Classes]]:

```cpp
// In some header file: student.h

class Student{
	private: // Access Controller
		int ID;
		string name;
	public: // Access Controller

		Student(); // default constructor
		Student(int id); // Additional Constructors:
		Student(int id, string n);
		Student(string n, int id);

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

// Constructor:
Student::Student(){ // (1) DEFAULT!!!
	ID = 0;
	name = '';
	//no return statement at all;
}
Student::Student(int id){ // (2)
	ID=id;
	name = "";
}
Student::Student(int id, string n){ // (3)
	ID=id;
	name = n;
}
tudent::Student(string n, int id){ // (4)
	ID=id;
	name = n;
}
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

## Here, we implement a form of [[Function Overloading]] in our constructors.

```cpp
#include "student.h"

int main(){
	
	Student x; //No parameters passed (1)
	Student y(1001); //int parameter passed (2)
	Student y(1002, "BABABA"); //int, str parameter passed (3)
	Student y("WAWAWA", 1003); //str, int parameter passed (4)

	Student p[10]; //Array with 10 student objects. Constructor (1) called 10 times.
	
	Student *s; // We havent given an adress to this yet; no const will be called.
	Student *t = &x; // No const will be called. We already did.

}
```

### Note that if default constructor Student() is not implemented and others like Student(int n) are, if we try Student x;… We will get a compile-time error