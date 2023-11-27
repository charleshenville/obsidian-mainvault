## Definition
- Allowed to “see” privates of its friend [[Classes]].
- Must be implemented outside the class.

```cpp
//In class definition:

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
		friend operator<<(ostream os); 
		// Can't Implement this inside of the Complex class definition.
		// We can declare it here though!! IMPORTANT!
};

//Friend function implementation:
ostream& operator<<(ostream& os, Complex rhs){ // Not a member of Complex, rather it is just a friend
	// We are passing and returning the same ostream objctect
	os << rhs.real << "+" << rhs.img  << "j"; // Allowed
	return os; // we return this ostream that 
}

int main(){
	
	Complex z (3,4);
	cout << " z is "<< z << endl;
	return 0;
}
```

### “ostream” and other streams cannot be returned or [[Pass By Value]]. Must be by reference.
- This is because it will delete the [[Copy Constructors]].
