# Q1. Count Consistent Subarrays I

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given an integer array `nums`.

A subarray is called  **consistent**  if the  **bitwise AND**  of all its elements is equal to the  **minimum**  value of the subarray.

Return the number of  **consistent subarrays**  in `nums`​​​​​​​.

A  **subarray**  is a contiguous, non-empty sequence of elements within an array.

 

Original
Python3
 **Example 1:** 

 **Input:**  nums = [5,3,1,2]

 **Output:**  6

 **Explanation:** 

The following subarrays are consistent:

Subarray	Values	Bitwise AND	Minimum Value
nums[0..0]	[5]	5	5
nums[1..1]	[3]	3	3
nums[2..2]	[1]	1	1
nums[3..3]	[2]	2	2
nums[1..2]	[3, 1]	3 AND 1 = 1	1
nums[0..2]	[5, 3, 1]	5 AND 3 AND 1 = 1	1

Therefore, the number of consistent subarrays is 6.

 **Example 2:** 

 **Input:**  nums = [1,1,1]

 **Output:**  6

 **Explanation:** 

For every subarray, both the bitwise AND and the minimum value are equal to 1. Therefore, the answer is 6.

 **Example 3:** 

 **Input:**  nums = [0]

 **Output:**  1

 **Explanation:** 

The only subarray is `[0]`, whose bitwise AND and minimum value are both 0. Therefore, the answer is 1.

 

 **Constraints:** 

- 1 <= nums.length <= 100
- 0 <= nums[i] <= 100

## Solution

**Language:** Python  
**Runtime:** 33 ms (beats 96.66%)  
**Memory:** 19.2 MB (beats 18.77%)  
**Submitted:** 2026-11-15T04:02:36.441Z  

```py
class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        n = len(nums)
        B = max(nums).bit_length() or 1

        # L[i]: nearest left index missing a bit of nums[i], or equal in value
        L = [-1] * n
        last_unset = [-1] * B
        last_val = {}
        for i, x in enumerate(nums):
            l = last_val.get(x, -1)
            for b in range(B):
                if x >> b & 1:
                    l = max(l, last_unset[b])
            L[i] = l
            for b in range(B):
                if not x >> b & 1:
                    last_unset[b] = i
            last_val[x] = i

        # Right side: nearest index missing a bit of nums[i]
        ans = 0
        next_unset = [n] * B
        for i in range(n - 1, -1, -1):
            x = nums[i]
            r = n
            for b in range(B):
                if x >> b & 1:
                    r = min(r, next_unset[b])
            ans += (i - L[i]) * (r - i)
            for b in range(B):
                if not x >> b & 1:
                    next_unset[b] = i
        return ans
```

---

[View on LeetCode](https://leetcode.com/problems/count-consistent-subarrays-i/)