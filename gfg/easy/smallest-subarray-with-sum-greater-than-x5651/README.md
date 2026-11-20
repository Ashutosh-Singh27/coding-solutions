# Smallest Subarray Sum Greater Than x

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer  **x** and an array of integers,  **arr[]**. Find the length of the smallest subarray whose sum is strictly greater than  **x**.

If no such subarray exists, return  **0**.

 **Examples:** 

```
Input: x = 51, arr[] = [1, 4, 45, 6, 0, 19]
Output: 3
Explanation: The smallest subarray with a sum greater than 51 is [4, 45, 6], whose sum is 55 and length is 3.
```

```
Input: x = 100, arr[] = [1, 10, 5, 2, 7]
Output: 0
Explanation: No subarray has a sum greater than 100. Hence, the answer is 0.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-20T19:21:50.111Z  

```py
class Solution:
    def smallestSubWithSum(self, arr, x):
        n = len(arr)
        left = 0
        total = 0
        best = n + 1
        for right in range(n):
            total += arr[right]
            while total > x:
                best = min(best, right - left + 1)
                total -= arr[left]
                left += 1
        return best if best <= n else 0
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/smallest-subarray-with-sum-greater-than-x5651/1)