## Detecting [[File IO]] Failure:

In the following

```cpp
#include <fstream>
#include <string>
using namespace std;

int main(){

	ifstream inputFile("myFile.txt"); 
	// note this can be devided: ifstream inputFile; inputFile.open("myFile.txt")
	int num1, num2, num3;
	inputFile >> num1 >> num2 >> num3;
	inputFile.close();
	return 0
	

}
```

Things that can go wrong:

- File doesn’t exist: `inputFile.fail()`
- Input reads a non-int: `inputFile.fail(), cin.fail()`
- Reached EOF: `inputFile.eof()` : Detected EOF character.

For standard inputs: CMD+D raises an EOF flag: `cin.eof()`

## Detecting A File cannot be opened

```cpp
ifstream inputFile("myFile.txt");

if(inputFile.fail()){

	cerr << "Error in file reading! Cannot open file!";
	return -1; // No longer returning 0, as we have a failiure.

}
```

## When input is unexpected (Effectively clearing errors and [[Buffering]]):

```cpp
cin.clear(); // -> Clear faliure conditions cin.fail(), cin.eof() -> False
cin.ignore(int n, char ch); // Ignores n characers in input buffer until the character ch (incl)
```

## Example program that reads an int from user:

- If it is not an int, prompt again

```cpp
main(){

	int n;
	cout << "Provide a number:";
	cin >> n;
	
	while(cin.fail()){
		
		cin.clear();
		cin.ignore(1000, '\\n');
		cout << "Provide a number:";
		cin >> n;

	}

	return 0;

}
```

## Example Program that reads ints from a file and prints their sum: If a non-int detected, ignore and keep reading. Ints live on separate lines.

```cpp
//Check if file exists
//Loop until we reach an EOF (inputFile.EOF())

int main(){
	
	if(inFile.fail()){
		
		cerr << "Can't open the file";
		return -1

	}
	int num=0, sum=0;
		
	while(!inputFile.eof()){

		inFile >> num;
		if(inFile.fail()){
		
			inFile.clear();
			inFile.ignore(1000, '\\n);
	
		}else{
		
			sum += num
		}
	}
}
```
