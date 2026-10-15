# Maximum Without 3 Consecutive Set Bits

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a non-negative integer  **n**, you can only change a set bit (1) to an unset bit (0). Find the maximum possible value of n such that its binary representation does not contain three consecutive set bits (111) after performing zero or more allowed operations.

 **Examples:** 

```
Input: n = 2
Output: 2
Explanation: The binary representation of 2 is 10, which does not contain three consecutive set bits. Therefore, no change is required.
```

```
Input: n = 7
Output: 6
Explanation: The binary representation of 7 is 111, which contains three consecutive set bits. Changing the rightmost set bit to 0 gives: 111 -> 110. Thus, the maximum possible value is 6.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-15T12:31:45.483Z  

```py
class Solution:
    def maxValue(self, n: int) -> int:
        bits = list(bin(n)[2:])
        count = 0
        for i in range(len(bits)):
            if bits[i] == '1':
                count += 1
                if count == 3:
                    bits[i] = '0'
                    count = 0
            else:
                count = 0
        return int(''.join(bits), 2)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/geek-hates-too-many-1s--170647/1)