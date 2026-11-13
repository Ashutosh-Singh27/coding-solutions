# Count Non-Decreasing Subarrays After K Operations

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given an array `nums` of `n` integers and an integer `k`.

For each subarray of `nums`, you can apply  **up to**  `k` operations on it. In each operation, you increment any element of the subarray by 1.

 **Note**  that each subarray is considered independently, meaning changes made to one subarray do not persist to another.

Return the number of subarrays that you can make  **non-decreasing**  ​​​​​after performing at most `k` operations.

An array is said to be  **non-decreasing**  if each element is greater than or equal to its previous element, if it exists.

 

Original
Python3
 **Example 1:** 

 **Input:**  nums = [6,3,1,2,4,4], k = 7

 **Output:**  17

 **Explanation:** 

Out of all 21 possible subarrays of `nums`, only the subarrays `[6, 3, 1]`, `[6, 3, 1, 2]`, `[6, 3, 1, 2, 4]` and `[6, 3, 1, 2, 4, 4]` cannot be made non-decreasing after applying up to k = 7 operations. Thus, the number of non-decreasing subarrays is `21 - 4 = 17`.

 **Example 2:** 

 **Input:**  nums = [6,3,1,3,6], k = 4

 **Output:**  12

 **Explanation:** 

The subarray `[3, 1, 3, 6]` along with all subarrays of `nums` with three or fewer elements, except `[6, 3, 1]`, can be made non-decreasing after `k` operations. There are 5 subarrays of a single element, 4 subarrays of two elements, and 2 subarrays of three elements except `[6, 3, 1]`, so there are `1 + 5 + 4 + 2 = 12` subarrays that can be made non-decreasing.

 

 **Constraints:** 

- 1 <= nums.length <= 105
- 1 <= nums[i] <= 109
- 1 <= k <= 109

## Solution

**Language:** Python  
**Runtime:** 500 ms (beats 25.64%)  
**Memory:** 38.3 MB (beats 48.72%)  
**Submitted:** 2026-11-13T15:17:01.979Z  

```py
from collections import deque
class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        a = nums[::-1]
        dq = deque()
        cur = 0
        wsum = 0
        l = 0
        ans = 0
        for r, x in enumerate(a):
            cnt = 1
            while dq and dq[-1][0] <= x:
                v, c = dq.pop()
                cur -= v * c
                cnt += c
            dq.append([x, cnt])
            cur += x * cnt
            wsum += x
            while cur - wsum > k:
                dq[0][1] -= 1
                cur -= dq[0][0]
                wsum -= a[l]
                l += 1
                if dq[0][1] == 0:
                    dq.popleft()
            ans += r - l + 1
        return ans
```

---

[View on LeetCode](https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/)