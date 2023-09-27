### Including the same header file many times may cause issues and redundancy.

```cpp
//a.h

struct A{
 
};
```

```cpp
//b.h

#include "a.h" // this is needed
void func(struct A);
```

```cpp
//c.h

#include "a.h" // this is needed
void func2 (struct A);
```

```cpp
//main.cpp
#include "a.h"
#include "b.h"
#include "c.h"

int main(){
	
	func(...)
	func2(...)
	struct A ...;
	
}
```

## A solution for this issue implementing [[Error Handling]]: Header Guards

- Guards against including header file content several times.

```cpp
#ifndef A_H
#define A_H

struct A{
//Dec'ln of struct A
};

#endif
```

# Why header files?

```cpp
//print.cpp
#inlcude <iostream>

void printNum(){
	...
}
```

```cpp
//main.cpp
#include "print.cpp" //Problematic, will have to do redundant recompilations

int main(){
	printNum();
}
```

Problems with the above:

1. We must also recompile main.cpp if print.cpp is changed
2. printNum will be defined twice: in print.cpp and main.cpp. You will get an error for multiple definitions.