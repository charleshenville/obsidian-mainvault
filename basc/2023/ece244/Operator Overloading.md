## We can define operations to do specific things for objects of differing [[Classes]].

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

### We can employ Operator Overloading on the ‘+’ and ‘=’ (addition and assignment) operators of `z=x+y`.

- We want to perform the equivalent invocation: `x.Operator+(y);`
- And the equivalent invocation: `z.Operator=(x.Operator+(y));`

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
		Complex operator+(Complex rhs);
};

Complex Complex::operator+(const Complex & rhs)const{ 
// (1) Being more memory efficient; we arent making a new object.
// (2) const keyword for safety.
// (3) const modifier (second)
	return Complex(real+rhs.real, img+rhs.img);
}

// in main:
int main(){
	
	Complex x(4,5), y(6,7), z;
	z = x+y; 
	// This will actually work right now despite not implementing
	// Complex Complex::Operator=() manually. It is automatically
	// but simply implemented for any class we create.

}
```

## Good practices

1. Pass parameter object by method of [[Pass by Reference]]
2. Safety: passing object parameter as a constant if we need not mutate it.
3. Safety: const modifier ensures that

### Suppose we want to modify `Complex::Operator=(){}`

```cpp
Complex Complex::operator=(const Complex&rhs){
	real = rhs.real;
	img = rhs.img;

	return *this; //*this is just the object. We have dereferenced it.
}
```

## The `this` keyword:

- Stores a [[Pointers]] to the object itself
- Cannot be changed to point to something else
- Enables us to [[Return by Reference]]

## The `<<` Operator:

```cpp
#inlcude <iostream>
// There is a class called ostream with a cout object of type ostream.
int main(){
	Compelx z(1,2);
	cout << z;
	// This requires us to manually implement an overloading operator for << in the ostream class.
	// We have not the liberty to do this.
}
```