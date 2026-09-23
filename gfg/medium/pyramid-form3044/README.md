# Pyramid Array with Reduce Operations

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array  **arr[]**  consisting of stones, where arr[i] represents the height of the i-th stone.

- You need to transform the stones into a pyramid by only reducing the heights of the stones. Reducing the height of a stone by 1 costs 1 unit, and stones cannot be increased or moved.
- A valid pyramid consists of a contiguous subarray whose heights follow the pattern: 1, 2, 3,..., x - 1, x, x - 1,..., 2, 1 for some positive integer x.
- Every stone outside this subarray must have a height of 0.

Find the minimum total cost required to build a pyramid. It is guaranteed that at least one valid pyramid can always be formed.

 **Examples:** 

```
Input: arr[] = [1, 2, 3, 4, 2, 1]
Output: 4
Explanation: We can obtain the array [1, 2, 3, 2, 1, 0] by subtracting 2 out of 4, 1 out of 2, and 1 out of 1. In total, we will subtract 4.
```

```
Input: arr[] = [1, 2, 1]
Output: 0
Explanation: The array is already in pyramid form.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-23T15:52:33.125Z  

```py
class Solution:
    def formPyramid(self, arr):
        n = len(arr)
        left = [0] * n
        right = [0] * n
        left[0] = min(arr[0], 1)
        for i in range(1, n):
            left[i] = min(arr[i], left[i-1] + 1)
        right[n-1] = min(arr[n-1], 1)
        for i in range(n-2, -1, -1):
            right[i] = min(arr[i], right[i+1] + 1)
        best = 0
        for i in range(n):
            h = min(left[i], right[i])
            best = max(best, h * h)
        return sum(arr) - best
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/pyramid-form3044/1)