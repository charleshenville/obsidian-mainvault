``` C++
#include <iostream>
#include <string>
using namespace std;

int main(void)
{
    string courseTitle = "Programming Fundamentals";
    string courseDept, courseNum, courseCode;
    cout << "Enter…: ";
    cin >> courseDept >> courseNum;
    courseCode = courseDept + courseNum;

    if(courseCode == "ECE244")
    {
        cout << "Awesome";
    }

    return 0;
}
```