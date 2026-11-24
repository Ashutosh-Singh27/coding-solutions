# Two Pairs with Same Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array  **arr[]**  of positive integers, find four indices  **a**,  **b**,  **c**, and  **d**  such that arr[a] + arr[b] = arr[c] + arr[d], where a, b, c, d are all distinct indices.

- If multiple such quadruplets exist, return the one that is lexicographically smallest when the indices are considered in the order a, b, c, d.
- If no such quadruplet exists, return {-1, -1, -1, -1}. 
- Ensure a < b and c < d, and the pair (a, b) is lexicographically smaller than the pair (c, d).

 **Examples:** 

```
Input: arr[] = [3, 4, 7, 1, 2, 9, 8]
Output: [0, 2, 3, 5]
Explanation: arr[0] + arr[2] = 3 + 7 = 10, arr[3] + arr[5] = 1 + 9 = 10. 
This is the lexicographically smallest such quadruplet of indices.
```

```
Input: arr[] = [1, 2, 3, 3]
Output: [-1, -1, -1, -1]
Explanation: No two distinct pairs of indices produce the same sum.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-24T10:24:47.388Z  

```py
class Solution:
    def findPairs(self, arr: list[int]) -> list[int]:
        n = len(arr)
        groups = {}
        for a in range(n):
            for b in range(a + 1, n):
                groups.setdefault(arr[a] + arr[b], []).append((a, b))

        best = None
        for lst in groups.values():
            if len(lst) < 2:
                continue
            # lst is already sorted lexicographically
            if best is not None and lst[0] > best[:2]:
                continue
            found = False
            for i in range(len(lst)):
                a, b = lst[i]
                if best is not None and (a, b) > best[:2]:
                    break
                for j in range(i + 1, len(lst)):
                    c, d = lst[j]
                    if c != a and c != b and d != a and d != b:
                        cand = (a, b, c, d)
                        if best is None or cand < best:
                            best = cand
                        found = True
                        break
                if found:
                    break

        return list(best) if best else [-1, -1, -1, -1]
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/satisfy-the-equation5847/1)