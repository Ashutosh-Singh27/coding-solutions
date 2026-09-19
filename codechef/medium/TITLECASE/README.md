# TITLECASE

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-19T15:20:08.806Z  

```py
def findLargestOddSubstring(num: str):
    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) % 2 != 0:
            return num[: i + 1]
    return -1
```

---

[View on CodeChef](https://www.codechef.com/problems/TITLECASE)