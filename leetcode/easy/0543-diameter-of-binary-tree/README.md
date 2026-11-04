# Diameter of Binary Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given the `root` of a binary tree, return  *the length of the  **diameter**  of the tree*.

The  **diameter**  of a binary tree is the  **length**  of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.

The  **length**  of a path between two nodes is represented by the number of edges between them.

 

 **Example 1:** 

```
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

```

 **Example 2:** 

```
Input: root = [1,2]
Output: 1

```

 

 **Constraints:** 

- The number of nodes in the tree is in the range [1, 104].
- -100 <= Node.val <= 100

## Solution

**Language:** Python  
**Runtime:** 5 ms (beats 43.51%)  
**Memory:** 22 MB (beats 78.96%)  
**Submitted:** 2026-11-04T14:34:53.880Z  

```py
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0

        def height(node):
            if not node:
                return 0
            l = height(node.left)
            r = height(node.right)
            self.best = max(self.best, l + r)
            return 1 + max(l, r)

        height(root)
        return self.best
```

---

[View on LeetCode](https://leetcode.com/problems/diameter-of-binary-tree/)