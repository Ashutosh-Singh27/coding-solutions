# Lexicographically Smallest Rotation

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given a string  **s**, find the lexicographically smallest string after rotating the string left any number of times including 0.

 **Example:** 

```
Input: s = "abcd"
Output: "abcd"
Explanation: String after each rotation are "abcd", "bcda", "cdab", "dabc" and so on. Lexicographically smallest among them is "abcd".

```

```
Input: s = "baca"
Output: "abac"
Explanation: Strings after each rotation are "baca", "acab", "caba", "abac" and so on. Lexicographically smallest among them is "abac".
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-02T14:04:30.502Z  

```py
class Solution:
    def lexiString(self, s: str) -> str:
        n = len(s)
        t = s + s
        i, j, k = 0, 1, 0
        while i < n and j < n and k < n:
            a = t[i + k]
            b = t[j + k]
            if a == b:
                k += 1
            else:
                if a > b:
                    i += k + 1
                else:
                    j += k + 1
                if i == j:
                    j += 1
                k = 0
        start = min(i, j)
        return t[start:start + n]
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/lexicographically-smallest-string--151951/1)