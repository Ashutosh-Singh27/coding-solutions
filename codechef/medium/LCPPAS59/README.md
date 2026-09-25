# LCPPAS59

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Positive and Negative

Write a program to check whether the given number as input is positive, negative, or zero.

### Sample 1:
Input
Output

```
20  
```

```
Positive  
```

### Sample 2:
Input
Output

```
0
```

```
Zero
```

### Sample 3:
Input
Output

```
-95
```

```
Negative
```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-25T16:15:42.138Z  

```c_cpp
#include <iostream>
using namespace std;

int main() {
    int num;
    cin>>num;
    if(num>0)
        cout<<"Positive";
    else if(num<0)
        cout<<"Negative";
    else
        cout<<"Zero";

    return 0;
}

```

---

[View on CodeChef](https://www.codechef.com/problems/LCPPAS59)