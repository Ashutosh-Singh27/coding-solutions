# CREDCOINS - Rating 541

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-09T14:41:41.994Z  

```py
# cook your dish here
t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if [a, b, c].count(0) >= 2:
        print("Water filling time")
    else:
        print("Not now")
```

---

[View on CodeChef](https://www.codechef.com/problems/CREDCOINS)