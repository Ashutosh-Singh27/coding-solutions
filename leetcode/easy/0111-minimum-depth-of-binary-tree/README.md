# Minimum Depth of Binary Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

 **Note:**  A leaf is a node with no children.

 

 **Example 1:** 

```
Input: root = [3,9,20,null,null,15,7]
Output: 2

```

 **Example 2:** 

```
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

```

 

 **Constraints:** 

- The number of nodes in the tree is in the range [0, 105].
- -1000 <= Node.val <= 1000

## Solution

**Language:** Python  
**Runtime:** 58 ms (beats 17.47%)  
**Memory:** 45.1 MB (beats 25.91%)  
**Submitted:** 2026-10-29T11:13:10.829Z  

```py
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-depth-of-binary-tree/)