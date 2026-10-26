# Minimize Max Min Diff with Subarray Removal

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an array  **arr[]**  of size  **n**. You need to remove a subarray of size  **k** , such that the difference between the maximum and minimum values of the remaining array is minimized. Find the minimum value obtained after performing the operation of the removal of the subarray.

 **Examples:** 

```
Input: arr = [1, 2, 3, 4, 5], k = 3 
Output: 1
Explanation: We remove first subarray of length 3, the remaining array is [4,5] and the difference of maximum and minimum element is 1 i.e 5 - 4 = 1
```

```
Input: arr = [2, 3, 1, 4, 6, 7], k = 3
Output: 2
Explanation: 
If we remove the subarray [2,3,1] then remaining array is [4,6,7] and the difference  = 7-4 = 3
If we remove the subarray [3,1,4] then remaining array is [2,6,7] and the difference  = 7-2 = 5
If we remove the subarray [1,4,6] then remaining array is [2,3,7] and the difference  = 7-2 = 5
If we remove the subarray [4,6,7] then remaining array is [2,3,1] and the difference  = 3-1 = 2
So the answer is min(3,5,5,2) = 2
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-26T11:49:03.606Z  

```py
class Solution:
    def minDiff(self, k: int, arr: list[int]) -> int:
        n = len(arr)
        if k >= n:
            return 0
        pre_min = [float('inf')] * (n + 1)
        pre_max = [float('-inf')] * (n + 1)
        suf_min = [float('inf')] * (n + 2)
        suf_max = [float('-inf')] * (n + 2)
        for i in range(n):
            pre_min[i + 1] = min(pre_min[i], arr[i])
            pre_max[i + 1] = max(pre_max[i], arr[i])
        for i in range(n - 1, -1, -1):
            suf_min[i] = min(suf_min[i + 1], arr[i])
            suf_max[i] = max(suf_max[i + 1], arr[i])
        ans = float('inf')
        for i in range(n - k + 1):
            mn = min(pre_min[i], suf_min[i + k])
            mx = max(pre_max[i], suf_max[i + k])
            ans = min(ans, mx - mn)
        return ans
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/minimize-the-difference/1)