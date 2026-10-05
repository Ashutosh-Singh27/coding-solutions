# SUBSCRIBE_ - Rating 500

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-05T07:42:57.352Z  

```py
# cook your dish here
t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if a + b > 2 * c:
        print("YES")
    else:
        print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/SUBSCRIBE_)