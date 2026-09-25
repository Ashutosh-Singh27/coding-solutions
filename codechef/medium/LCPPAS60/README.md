# LCPPAS60

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Grades of Student

Write a program to print the grades of a student based on the marks they have obtained provided as input. The student is graded  **A**  if marks are greater than  **90**,  **B**  if marks are greater than  **70**,  **C**  if greater than or equal to  **40**, else  **F**.

### Sample 1:
Input
Output

```
95  
```

```
A  
```

### Sample 2:
Input
Output

```
40
```

```
C
```

### Sample 3:
Input
Output

```
20
```

```
F
```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-25T16:08:51.423Z  

```c_cpp
#include <iostream>
using namespace std;

int main() {
    int marks;
    cin >> marks;
    
    if (marks > 90) {
        cout << "A";
    } else if (marks > 70) {
        cout << "B";
    } else if (marks >= 40) {
        cout << "C";
    } else {
        cout << "F";
    }
    
    return 0;
}
```

---

[View on CodeChef](https://www.codechef.com/problems/LCPPAS60)