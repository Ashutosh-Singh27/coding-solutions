# Minimum Sum of Squared Difference

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given two positive  **0-indexed**  integer arrays `nums1` and `nums2`, both of length `n`.

The  **sum of squared difference**  of arrays `nums1` and `nums2` is defined as the  **sum**  of `(nums1[i] - nums2[i])2` for each `0 <= i < n`.

You are also given two positive integers `k1` and `k2`. You can modify any of the elements of `nums1` by `+1` or `-1` at most `k1` times. Similarly, you can modify any of the elements of `nums2` by `+1` or `-1` at most `k2` times.

Return  *the minimum  **sum of squared difference**  after modifying array* `nums1` *at most* `k1` *times and modifying array* `nums2` *at most* `k2` *times*.

 **Note** : You are allowed to modify the array elements to become  **negative**  integers.

 

 **Example 1:** 

```
Input: nums1 = [1,2,3,4], nums2 = [2,10,20,19], k1 = 0, k2 = 0
Output: 579
Explanation: The elements in nums1 and nums2 cannot be modified because k1 = 0 and k2 = 0. 
The sum of square difference will be: (1 - 2)2 + (2 - 10)2 + (3 - 20)2 + (4 - 19)2 = 579.

```

 **Example 2:** 

```
Input: nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1
Output: 43
Explanation: One way to obtain the minimum sum of square difference is: 
- Increase nums1[0] once.
- Increase nums2[2] once.
The minimum of the sum of square difference will be: 
(2 - 5)2 + (4 - 8)2 + (10 - 7)2 + (12 - 9)2 = 43.
Note that, there are other ways to obtain the minimum of the sum of square difference, but there is no way to obtain a sum smaller than 43.
```

 

 **Constraints:** 

- n == nums1.length == nums2.length
- 1 <= n <= 105
- 0 <= nums1[i], nums2[i] <= 105
- 0 <= k1, k2 <= 109

## Solution

**Language:** Python  
**Runtime:** 213 ms (beats 41.25%)  
**Memory:** 36.3 MB (beats 98.75%)  
**Submitted:** 2026-10-10T16:44:29.164Z  

```py
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        m = max(abs(a - b) for a, b in zip(nums1, nums2))
        cnt = [0] * (m + 1)
        for a, b in zip(nums1, nums2):
            cnt[abs(a - b)] += 1

        if sum(i * cnt[i] for i in range(m + 1)) <= k:
            return 0

        top = m
        while top > 0 and k > 0:
            c = cnt[top]
            if c == 0:
                top -= 1
                continue
            if c <= k:
                k -= c
                cnt[top - 1] += c
                cnt[top] = 0
                top -= 1
            else:
                cnt[top] -= k
                cnt[top - 1] += k
                k = 0

        return sum(i * i * cnt[i] for i in range(m + 1))
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-sum-of-squared-difference/)