- Output is not being immediately written in a file/terminal
    - We Do this in chunks
- We must buffer first.

```cpp
outFile << "Hi";
outFile << " every";

outFile << endl;
//OR
outFile.flush();
```

|H|i||e|v|e|r|y|
|---|---|---|---|---|---|---|---|

From memory to myFile.txt once flushed.

```
Hi every
```

## Buffer examples with [[File IO]]

### Example 1:

```cpp
int x,y;
cin >> x >> y; // Stored in a keyboard buffer initially
```

Input: `123 4`

`x -> 123, y -> 4`

NOTE: `cin` will essentially ignore white spaces/delimiters like `‘ ’, ‘\\t’, ‘\\n’`

### Example 2:

```cpp
int x,y;
cin >> x >> y; // Stored in a keyboard buffer initially
```

Input: `13.7`

`x -> 13, y -> ????`

Here, `cin` essentially fails and the keyboard buffer (and our variable, y) remains unaffected; stuck at the character `‘.’`