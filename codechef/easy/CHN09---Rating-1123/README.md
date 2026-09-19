# CHN09 - Rating 1123

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-19T15:20:24.784Z  

```py
# cook your dish here
s = set(input())
n= int(input())
for _ in range(n):
    w= input()
    print("Yes"if set(w).issubset(s) else "No")
```

---

[View on CodeChef](https://www.codechef.com/problems/CHN09)