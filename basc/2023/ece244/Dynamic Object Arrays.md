## An Array of Dynamically Allocated [[Classes]] Objects:
```cpp
class Student{
	// Defn
	int ID;
	string name;
	Student(){
		ID=0; name="";
	}
	// Destructor:
	~Student(){
		cout << "Destructor" << endl;
	}
}

int main(){
	Student * arr = new Student[3];
	delete [] arr; // Deletes all sucessfully. 
	return 0;
}
```

## Dynamically Allocating an Array of [[Pointers]] to Objects

```cpp
Student** arr2p = new Student* [3];

for(int i=0 i<3; i++){
	arr2p[i] = new Student;
}

for(int i=0; i<3; i++){
	arr2p[i]->ID = i+1; // Accessing the ID member of the arr2p[i] pointer which points to a Student Object
}

for(int i=0; i<3; i++){
	delete arr2p[i]; // Destructor is called here since we have freed an object.
	arr2p[i] = NULL;
}

delete []arr2p; // Sticky like this.
arr2p = NULL;
```

## Overloading Operators

```cpp
class Complex{
	private:
		double real;
		double img;
	public:
		Complex(){
			real=0.0; 
			img=0.0;
		}
		Complex(double r, double i;){
			real = r;
			img = i;
		}
};
int main(){

	Complex x(3,4);
	Complex y(3,4);
	Complex z;

	// We want to do the following by we cannot yet:
	z = x+y;
	return 0;

}
```

### We can employ Operator Overloading on the ‘+’ operator of `z=x+y`.

- We want to do the equivalent invocation: `x.Operator+(y);`

```cpp
class Complex{
	private:
		double real;
		double img;
	public:
		Complex(){
			real=0.0; 
			img=0.0;
		}
		Complex(double r, double i;){
			real = r;
			img = i;
		}
		Complex Operator+(Complex rhs);
};

Complex Complex::Operator+(Complex rhs){
	return Complex(real+rhs.real, img+rhs.img);
}

```