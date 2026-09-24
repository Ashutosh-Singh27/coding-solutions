# Check the status - Python

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two integer variables  **a**  and  **b**, and a boolean variable  **flag**. The task is to check the status and return accordingly.

Return  **True** for the following cases:

- Either a or b (not both) is non-negative and the flag is false.
- Both a and b are negative and the flag is true.

Otherwise, return  **False**.

 **Examples:**  

```
Input: a = 1, b = -1, flag = False
Output: True
Explanation: Since a is positive, b is negative, and flag is False, condition 1 holds true, so the function returns True.
```

```
Input: a = -182, b = -9121, flag = True
Output: True
Explanation: Since both a and b are negative and flag is True, condition 2 holds true, so the function returns True.
```

```
Input: a = 5, b = 3, flag = True
Output: False
Explanation: Neither condition 1 nor condition 2 holds, so the function returns False.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-24T14:40:25.023Z  

```py
class Solution:
    def checkStatus(self, a, b, flag):
        cond1 = ((a >= 0) != (b >= 0)) and not flag
        cond2 = (a < 0 and b < 0) and flag
        return cond1 or cond2
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/check-the-status/1)