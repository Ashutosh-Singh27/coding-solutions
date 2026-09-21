# Check Level Anagrams in Binary Trees

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given the roots of two binary trees   root1   and   root2 , check whether the nodes at every corresponding level of the two trees are anagrams of each other.

Two levels are considered anagrams if they contain the same node values with the same frequencies, regardless of their order.

 **Examples:** 

```
Input: root1 = [1, 3, 2, N, N, 5, 4], root2 = [1, 2, 3, 4, 5, N, N]

Output: true
Explanation: 
Level 0: [1] and [1]
Level 1: [3, 2] and [2, 3]
Level 2: [5, 4] and [4, 5]
The node values at every corresponding level are anagrams of each other. Hence, the answer is true.
```

```
Input: root1 = [1, 2, 3, 5, 4], root2 = [1, 2, 4, 5, 3]

Output: false
Explanation: 
Level 0: [1] and [1]
Level 1: [2, 3] and [2, 4]
Since the node values at level 1 are not anagrams, the answer is false.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-21T16:10:42.500Z  

```py
from collections import deque, Counter

class Solution:
    def areAnagrams(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False

        q1 = deque([root1])
        q2 = deque([root2])

        while q1 and q2:
            if len(q1) != len(q2):
                return False

            c1 = Counter()
            c2 = Counter()

            for _ in range(len(q1)):
                a = q1.popleft()
                b = q2.popleft()

                c1[a.data] += 1
                c2[b.data] += 1

                if a.left:
                    q1.append(a.left)
                if a.right:
                    q1.append(a.right)
                if b.left:
                    q2.append(b.left)
                if b.right:
                    q2.append(b.right)

            if c1 != c2:
                return False

        return not q1 and not q2
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/check-if-all-levels-of-two-trees-are-anagrams-or-not/1)