# Subarrays Distinct Element Sum of Squares II

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given a  **0-indexed** integer array `nums`.

The  **distinct count**  of a subarray of `nums` is defined as:

- Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].

Return  *the sum of the  **squares**  of  **distinct counts**  of all subarrays of* `nums`.

Since the answer may be very large, return it  **modulo**  `109 + 7`.

A subarray is a contiguous  **non-empty**  sequence of elements within an array.

 

 **Example 1:** 

```
Input: nums = [1,2,1]
Output: 15
Explanation: Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 + 22 + 22 + 22 = 15.

```

 **Example 2:** 

```
Input: nums = [2,2]
Output: 3
Explanation: Three possible subarrays are:
[2]: 1 distinct value
[2]: 1 distinct value
[2,2]: 1 distinct value
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 = 3.
```

 

 **Constraints:** 

- 1 <= nums.length <= 105
- 1 <= nums[i] <= 105

## Solution

**Language:** Python  
**Runtime:** 4015 ms (beats 68.97%)  
**Memory:** 118.5 MB (beats 24.14%)  
**Submitted:** 2026-10-16T16:37:50.655Z  

```py
class Solution:
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        size = 1
        while size < n:
            size *= 2
        s = [0] * (2 * size)
        q = [0] * (2 * size)
        lz = [0] * (2 * size)
        ln = [1] * (2 * size)
        for i in range(size - 1, 0, -1):
            ln[i] = ln[2 * i] * 2

        def apply(node, k):
            q[node] += 2 * k * s[node] + k * k * ln[node]
            s[node] += k * ln[node]
            lz[node] += k

        def update(node, lo, hi, a, b):
            if a <= lo and hi <= b:
                apply(node, 1)
                return
            if lz[node]:
                apply(2 * node, lz[node])
                apply(2 * node + 1, lz[node])
                lz[node] = 0
            mid = (lo + hi) // 2
            if a <= mid:
                update(2 * node, lo, mid, a, b)
            if b > mid:
                update(2 * node + 1, mid + 1, hi, a, b)
            s[node] = s[2 * node] + s[2 * node + 1]
            q[node] = q[2 * node] + q[2 * node + 1]

        last = {}
        ans = 0
        for r, x in enumerate(nums):
            p = last.get(x, -1)
            update(1, 0, size - 1, p + 1, r)
            last[x] = r
            ans += q[1]
        return ans % MOD
```

---

[View on LeetCode](https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/)