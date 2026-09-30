# LCPPAS161

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Find the number of digits

Given an integer  **N**, Calculate and print the number of digits present in  **N**.

### Constraints
- $1 \leq N \leq 10^8$
### Sample 1:
Input
Output

```
1543
```

```
4
```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-30T13:44:10.827Z  

```c_cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int count = 0;
    while (n > 0) {
        count++;
        n /= 10;
    }
    cout << count;
    return 0;
}
```

---

[View on CodeChef](https://www.codechef.com/problems/LCPPAS161)