# Min Flips for Alternate

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a binary string  **s**, we can flip any bit (change 0 to 1 or 1 to 0) to make the string alternating. A string is called alternating if no two adjacent characters are the same.

Find the minimum number of bit flips required to make the string alternating.

 **Examples:** 

```
Input: s = "001"
Output: 1
Explanation: Flip the bit at index 0 from 0 to 1 to obtain "101", which is an alternating binary string. Hence, the minimum number of flips required is 1.

```

```
Input: s = "0001010111" 
Output: 2
Explanation: Flip the bit at indices 1 and 8 to obtain "0101010101", which is an alternating binary string. Hence, the minimum number of flips required is 2.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-20T19:19:46.547Z  

```py
class Solution:
    def minFlips(self, s):
        n = len(s)
        a = 0
        for i in range(n):
            if int(s[i]) != i % 2:
                a += 1
        return min(a, n - a)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/min-number-of-flips3210/1)