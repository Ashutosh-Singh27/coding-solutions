# Maximum Height Disc Stack

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given two arrays  **r[]**  and  **h[]**  of size  **n**, where **r[i]** and  **h[i]**  represent the radius and height of the i-th circular disc, respectively.

A disc can be placed above another disc only if both its radius and height are strictly smaller than those of the disc below it.

Find the maximum possible height of a stack that can be formed using the given discs. Each disc can be used at most once.

 **Examples:** 

```
Input: r[] = [5, 7, 3], h[] = [6, 5, 4]
Output: 10
Explanation: The discs (3, 4) and (5, 6) form a valid stack. Therefore, the maximum possible height is 4 + 6 = 10.
```

```
Input: r[] = [3, 7], h[] = [7, 4]
Output: 7
Explanation: Neither disc can be placed above the other because both required dimensions are not strictly smaller. Therefore, the maximum possible height is 7.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-24T14:35:30.758Z  

```py
class Solution:
    def maxStackHeight(self, r, h, n=None):
        if n is None:
            n = len(r)
        discs = sorted(zip(r, h), key=lambda x: (x[0], -x[1]))
        hs = [d[1] for d in discs]

        sorted_h = sorted(set(hs))
        comp = {v: i + 1 for i, v in enumerate(sorted_h)}
        m = len(sorted_h)
        tree = [0] * (m + 1)

        def update(i, val):
            while i <= m:
                if tree[i] < val:
                    tree[i] = val
                i += i & (-i)

        def query(i):
            res = 0
            while i > 0:
                if tree[i] > res:
                    res = tree[i]
                i -= i & (-i)
            return res

        ans = 0
        for height in hs:
            idx = comp[height]
            best = query(idx - 1) + height
            update(idx, best)
            ans = max(ans, best)

        return ans
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/stacking-up-discs1315/1)