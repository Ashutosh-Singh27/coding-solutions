# Longest Colored Path

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given an undirected acyclic graph (tree) with  **n**  nodes numbered from 1 to n. Each node is colored either Red (R) or Blue (B).

The colors of the nodes are given by a string  **s**  of length n, where:

- s[i] = 'R' means node i + 1 is Red.
- s[i] = 'B' means node i + 1 is Blue.

You are also given a list of n - 1 edges  **edges[][]**, where each edges[i] = [u, v] represents an undirected edge between nodes u and v.

You can start from any node and traverse along the edges to form a path.

A path is called valid if, once you visit a Blue node, you cannot visit any Red node after it on the same path.

In other words, a valid path must have the following form:

- Only Red nodes, or
- Only Blue nodes, or
- Some Red nodes followed by some Blue nodes.
- A path containing a pattern like Blue -> Red is invalid.

Find the maximum number of nodes in a valid path.

 **Examples:** 

```
Input: s = "RBB", edges = [[1, 2], [1, 3]] 
  
Output: 2
Explanation: The longest path is either 1 -> 2 or 1 -> 3. In both cases, the length of the path is 2.
```

```
Input: s = "BB", edges = [[1, 2]]
  
Output: 2
Explanation: The longest path is 1 -> 2. The length of the path is 2.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-27T14:57:37.965Z  

```py
class Solution:
    def longestPath(self, s, edges):
        n = len(s)
        if n == 1:
            return 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        color = {i + 1: s[i] for i in range(n)}
        parent = [0] * (n + 1)
        visited = [False] * (n + 1)
        order = []
        stack = [1]
        visited[1] = True
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    stack.append(v)
        A0 = [0] * (n + 1)
        A1 = [0] * (n + 1)
        ans = 1
        for u in reversed(order):
            pairs = []
            for v in adj[u]:
                if v == parent[u]:
                    continue
                if color[v] == color[u]:
                    c0 = A0[v]
                    c1 = A1[v]
                else:
                    c0 = 0
                    c1 = A0[v]
                pairs.append((c0, c1))
            if not pairs:
                A0[u] = 1
                A1[u] = 1
                continue
            c0_vals = [p[0] for p in pairs]
            top1 = -1
            idx1 = -1
            for i, c0 in enumerate(c0_vals):
                if c0 > top1:
                    top1 = c0
                    idx1 = i
            top2 = -1
            for i, c0 in enumerate(c0_vals):
                if i != idx1 and c0 > top2:
                    top2 = c0
            if top1 < 0:
                top1 = 0
            if top2 < 0:
                top2 = 0
            best_no_budget = top1 + top2
            best_with_budget = 0
            for i, (c0, c1) in enumerate(pairs):
                other = top2 if i == idx1 else top1
                val = c1 + other
                if val > best_with_budget:
                    best_with_budget = val
            A0[u] = 1 + top1
            A1[u] = 1 + max(p[1] for p in pairs)
            cand = 1 + max(best_no_budget, best_with_budget)
            if cand > ans:
                ans = cand
        return ans
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/longest-colored-path--151454/1)