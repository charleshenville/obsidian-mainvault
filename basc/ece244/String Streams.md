## To include and deal with [[Strings in C++]]:

```cpp
#include <sstream>
#incldue <string>
using namespace std;

int main(){

	int ID;
	string name;

	string inputLine = "1001 Joe";
	stringstream myStringStream(inputLine);
	myStringStream >> ID; // ID Stores 1001
	myStringStream >> name; // name Stores Joe

	if(myStringStream.fail()){
		myStringStream.clear();
		myStringStream.ignore(1000, '\\n');
	}
	
	myStringStream << name; // We can do this
	myStringStream << ID;
	cout << myStringStream.str(); // Accessing the actual string in this object through the .str() method

}
```

Note that we can now use [[Buffering]] with our strings via this method. [[Error Handling]] helps us deal with myStringStream.fail().
## Getline

```cpp
string inputLine;
getline(cin, inputLine); // Puts input from user into input line.
stringstream myStringStream(inputLine);
myStringStream >> ID;
```
