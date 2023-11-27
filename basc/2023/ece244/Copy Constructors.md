## Definition
- [[Constructors]] that takes the same type as a parameter and simply copies all attributes to the new object that is being instantiated with that constructor.
- This is, by default, already implemented for every class; Programmed to do everything that we wish :).
- Just like any Constructor; has no return.

```cpp
Student a(b);
Student a=b; // Does NOT call Overloaded Assignment Operator.
```