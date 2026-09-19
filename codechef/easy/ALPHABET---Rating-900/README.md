# ALPHABET - Rating 900

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-19T15:20:16.786Z  

```py
# cook your dish here
t = int(input())
for _ in range(t):
    s = input()
    words = s.split()
    result = []
    for word in words:
        if word.isupper():
            result.append(word)
        else:
            result.append(word[0].upper() + word[1:].lower())
    print(' '.join(result))
```

---

[View on CodeChef](https://www.codechef.com/problems/ALPHABET)