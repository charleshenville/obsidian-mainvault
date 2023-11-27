- An alias/alternate name to a variable

```cpp
int a =7, b = 12;
int& ra = a;
```

|**a, ra**|
|---|
|7|
|**b**|
|12|

- References cannot be reassigned.
- References do not have a separate memory location.
- References must be initialized at the time of declaration.

```cpp
int x = 10;
int& y = x;
y = 20;

//Now both x and y have values of 20. They share an address storing value 20.
```