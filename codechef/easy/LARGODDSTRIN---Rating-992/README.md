# LARGODDSTRIN - Rating 992

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-16T17:49:24.508Z  

```py
t = int(input())
while t > 0:
    s = input()
    d1 = int(s[0:2])
    d2 = int(s[3:5])
    y = int(s[6:10])
    leap = (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0))
    dim = [31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ddmm = 1 <= d2 <= 12 and 1 <= d1 <= dim[d2 - 1]
    mmdd = 1 <= d1 <= 12 and 1 <= d2 <= dim[d1 - 1]
    if ddmm and mmdd:
        print("BOTH")
    elif ddmm:
        print("DD/MM/YYYY")
    else:
        print("MM/DD/YYYY")
    t -= 1
```

---

[View on CodeChef](https://www.codechef.com/problems/LARGODDSTRIN)