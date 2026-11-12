# Closest in BST

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given  **root**  of a Binary Search Tree (BST) and an integer  **k**, find the minimum absolute difference between k and the value of any node in the BST.

 **Examples:** 

```
Input: root = [10, 2, 11, 1, 5, N, N, N, N, 3, 6, N, 4], k = 13

Output: 2
Explanation: The node with value 11 is closest to k = 13. So, the minimum absolute difference is |11 - 13| = 2.

```

```
Input: root = [8, 1, 9, N, 4, N, 10, 3], k = 9

Output: 0
Explanation: The node with value 9 is closest to k = 9. So, the minimum absolute difference is |9 - 9| = 0.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-12T18:14:16.893Z  

```py
class Solution:
    def minDiff(self, root: 'Node', k: int) -> int:
        best = float('inf')
        node = root
        while node:
            best = min(best, abs(node.data - k))
            if best == 0:
                return 0
            if k < node.data:
                node = node.left
            else:
                node = node.right
        return best
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/find-the-closest-element-in-bst/1)