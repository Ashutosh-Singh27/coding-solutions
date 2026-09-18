# Minimum Absolute Difference In BST

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given the root of a Binary Search Tree (BST) containing  **n (n > 1)**  nodes, find the minimum absolute difference between the values of any two different nodes in the tree.

Return the minimum absolute difference.

 **Examples:** 

```
Input: root[] = [50, 30, 70, 20, N, 60, 80]

Output: 10
Explanation: There are no two nodes whose absolute difference is smaller than 10.
```

```
Input: root[] = [60, 30, 90, 10]

Output: 20
Explanation: There are no two nodes whose absolute difference is smaller than 20.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-18T13:30:26.288Z  

```py
class Solution:
    def absDiff(self, root):
        self.prev = None
        self.min_diff = float('inf')

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.data - self.prev.data)
            self.prev = node
            inorder(node.right)

        inorder(root)
        return self.min_diff
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/minimum-absolute-difference-in-bst-1665139652/1)