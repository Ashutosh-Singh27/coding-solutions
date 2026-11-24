# Maximum Subarray With Equal Products

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given an array of  **positive**  integers `nums`.

An array `arr` is called  **product equivalent**  if `prod(arr) == lcm(arr) * gcd(arr)`, where:

- prod(arr) is the product of all elements of arr.
- gcd(arr) is the GCD of all elements of arr.
- lcm(arr) is the LCM of all elements of arr.

Return the length of the  **longest**   **product equivalent**  subarray of `nums`.

 

Original
Python3
 **Example 1:** 

 **Input:**  nums = [1,2,1,2,1,1,1]

 **Output:**  5

 **Explanation:**  

The longest product equivalent subarray is `[1, 2, 1, 1, 1]`, where `prod([1, 2, 1, 1, 1]) = 2`, `gcd([1, 2, 1, 1, 1]) = 1`, and `lcm([1, 2, 1, 1, 1]) = 2`.

 **Example 2:** 

 **Input:**  nums = [2,3,4,5,6]

 **Output:**  3

 **Explanation:**  

The longest product equivalent subarray is `[3, 4, 5].`

 **Example 3:** 

 **Input:**  nums = [1,2,3,1,4,5,1]

 **Output:**  5

 

 **Constraints:** 

- 2 <= nums.length <= 100
- 1 <= nums[i] <= 10

## Solution

**Language:** Python  
**Runtime:** 30 ms (beats 68.75%)  
**Memory:** 19.3 MB (beats 56.25%)  
**Submitted:** 2026-11-24T10:22:48.629Z  

```py
from math import gcd
class Solution:
    def maxLength(self, nums: list[int]) -> int:
        n = len(nums)
        best = 0
        for i in range(n):
            p, g, l = 1, 0, 1
            for j in range(i, n):
                x = nums[j]
                p *= x
                g = gcd(g, x)
                l = l * x // gcd(l, x)
                if p == g * l:
                    best = max(best, j - i + 1)
        return best
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-subarray-with-equal-products/)