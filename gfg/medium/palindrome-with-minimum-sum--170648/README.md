# Palindrome with Replacement

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string  **s**  consisting of lowercase English letters and the character '?', 

- Replace every '?' with a lowercase English letter such that the resulting string is a palindrome.
- If it is possible to form a palindrome, return the minimum possible sum of the absolute ASCII differences between every pair of adjacent characters in the resulting string.
- If it is not possible to form a palindrome, return -1.

 **Examples:** 

```
Input: s = a???c??c????
Output: 4
Explanation: One optimal palindrome is "abbbccccbbba". The sum of the absolute ASCII differences between adjacent characters is 1 + 0 + 0 + 1 + 0 + 0 + 0 + 1 + 0 + 0 + 1 = 4, which is the minimum possible. 
```

```
Input: s = a???c??c???c
Output: -1
Explanation: It is not possible to replace the '?' characters to make the string a palindrome because the first and last characters are different and cannot be changed.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-22T10:57:08.348Z  

```py
class Solution:
    def minimumSum(self, s: str) -> int:
        n = len(s)
        arr = list(s)
        for i in range(n // 2):
            j = n - 1 - i
            if arr[i] == '?':
                arr[i] = arr[j]
            elif arr[j] == '?':
                arr[j] = arr[i]
            elif arr[i] != arr[j]:
                return -1
        m = (n + 1) // 2
        prev = None
        total = 0
        for i in range(m):
            if arr[i] != '?':
                if prev is not None:
                    total += abs(ord(arr[i]) - ord(prev))
                prev = arr[i]
        return 2 * total
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/palindrome-with-minimum-sum--170648/1)