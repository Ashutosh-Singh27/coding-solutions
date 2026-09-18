# MFRLE

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-18T13:24:18.443Z  

```py
# cook your dish here
s = input().strip()

count = {}
for i in range(len(s) - 1):
    pair = s[i:i+2]
    count[pair] = count.get(pair, 0) + 1

result = sum(1 for v in count.values() if v > 1)
print(result)
```

---

[View on CodeChef](https://www.codechef.com/problems/MFRLE)