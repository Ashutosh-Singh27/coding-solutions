# Max Equal Sum in 3 Stacks

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given three stacks  **s1**,  **s2**, and  **s3**, represented by arrays where the first element of each array represents the top of the corresponding stack.

Find the maximum possible equal sum(sum of all elements) of all three stacks by removing zero or more elements from the top of each stack.

If it is not possible to make the sum of all three stacks equal, return  **0**.

 **Examples:** 

```
Input: s1 = [3, 2, 1, 1, 1], s2 = [4, 3, 2], s3 = [2, 5, 4, 1]
Output: 5
Explanation: Remove 3 from s1, 4 from s2, and 2, 5 from s3. The remaining sums of all three stacks are equal to 5.

```

```
Input: s1 = [4,7], s2 = [10], s3 = [1,2,3]
Output: 0
Explanation: It is not possible to make the sums of all three stacks equal by removing elements from their tops.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-14T13:46:06.437Z  

```py
class Solution:
    def maxEqualSum(self, s1, s2, s3):
        a, b, c = sum(s1), sum(s2), sum(s3)
        i = j = k = 0
        n1, n2, n3 = len(s1), len(s2), len(s3)
        while i < n1 and j < n2 and k < n3:
            if a == b == c:
                return a
            m = max(a, b, c)
            if a == m:
                a -= s1[i]
                i += 1
            elif b == m:
                b -= s2[j]
                j += 1
            else:
                c -= s3[k]
                k += 1
        return 0
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/find-maximum-equal-sum-of-three-stacks/1)