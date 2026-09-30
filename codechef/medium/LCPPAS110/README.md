# LCPPAS110

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Print factorial

Write a program that uses a do-while loop to find the factorial of a given number.

### Sample 1:
Input
Output

```
5
```

```
120
```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-30T13:38:44.531Z  

```c_cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    long long fact = 1;
    int i = 1;
    do {
        fact *= i;
        i++;
    } while (i <= n);
    cout << fact;
    return 0;
}
```

---

[View on CodeChef](https://www.codechef.com/problems/LCPPAS110)