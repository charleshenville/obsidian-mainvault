## We can use them to prevent memory leaks when dealing with [[Pointers]]
```cpp
class Student{

private:
	int grades;
	string name;
public:
	Student();
	Student(int);
	~Student(); // Destructor, doesnt receive any args or return anything with the name of the Class name. 
};

Student::Student(){ //Constructor

	grades = nullptr;
	name = "";

}
Student::Student(int numOfLabs){
	
	if(grades != nullptr){
		grades = new int[numOfLabs]; // allocated memory on heap for a numoflabs long int array.
	}
}
Student::~Student(){

	delete []grades; // Must use square brackets when de-allocating memory for this.

}

int main(){

	Student x(3); // Will call the second constructor with memory alloc.
	Student y(); // We did not allocate anyspace for this. Grades is null.
	delete Student; // De-Allocate 
	return 0;

} // We call the destructor here
```

## Info on Destructors:

- By default called when a [[Classes]] object goes out of scope.
- We can only have one destructor.

```cpp
class ComplexNum{
	public:
		double real;
		double img;
		ComplexNum(double r, double i){ // We can do this. (Constructor)
			real = r; img=i;
		}
}; // REMEMBER!!!
int main(){
	ComplexNum x(3,4); // calls the 
	x.real = 8;
	ComplexNum * p; // Constructor isnt called since we didnt actually instantiate a new object here.
	p =& x; // Now it points to x that we instantiated.
	p -> real = 9; // Identical to structs in C.
	// Now x.real=9, x.img=4.
}
```