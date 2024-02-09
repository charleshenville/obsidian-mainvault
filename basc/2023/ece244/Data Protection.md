## Employed when using [[Inheritance]]:
- `protected` data and function members of a class are inherited and accessible to derived classes but not to all classes (in the spectrum of private -> public).

```cpp
class Person{
	protected:
	int age; std::string name;
};
class Student : public Person{
	private:
		int ID;
	public:
		Student(std::string n, int a, int d){
			// Remember that we have inheried protected members and can use them here:
			Person::name=n;
			Person::age=a;
		}
};
```

## Note that we do not inherit:

- [[Constructors]]
- Copy constructors
- operator=
- [[Destructors]]