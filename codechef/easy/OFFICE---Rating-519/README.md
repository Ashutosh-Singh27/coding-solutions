# OFFICE - Rating 519

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-07T05:58:53.709Z  

```py
# cook your dish here
t = int(input())
for _ in range(t):
    x, y, z = map(int, input().split())
    print("YES" if 2 * z > x * y else "NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/OFFICE)