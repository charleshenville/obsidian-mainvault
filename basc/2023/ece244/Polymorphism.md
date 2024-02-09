## Definition:
- Yet another pillar of OOP, see [[Encapsulation]] and [[Inheritance]]. 
## Motivation
- Overcoming inability to access members of derived objects and [[Classes]] if the pointer pointing to it is of the associated base type.
- if we declare a function as a virtual one in the base class, and redefined or overridden in the associated derived class, a call to that function through `Base*` will invoke the function depending only on the type of the object it points to and not the type of the pointer.

```cpp
class Polygon{
	protected:
		int width, height;
	public:
		void set(int w, int h){
			width = w; height = h;
		}
		virtual int area(){return 0;}
		
};

int main(){
	//Now if we did:
	Rectangle *p1 = new Rectangle;
	cout << p1->area() << endl;
	// Will print the widthxheight if that is how the area function is defined in Rectangle.
	return 0;
}
```

Note that [[Classes]] that inherit a virtual function are said to be Polymorphic classes.