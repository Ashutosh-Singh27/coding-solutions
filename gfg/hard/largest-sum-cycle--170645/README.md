# Largest Sum Cycle

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given an array   edge[]   of size   n , there are   n   cells numbered from   0   to   n - 1 . Each cell has at most one outgoing edge.

For every cell i:

- edge[i] is the cell reached from i in one step.
- edge[i] = -1 means that cell i has no outgoing edge.

A cycle is a sequence of cells where, by following the outgoing edges, we eventually return to the starting cell. The sum of a cycle is the sum of the indices of all cells in that cycle.

Return the maximum cycle sum. If there is no cycle, return -1.

  Examples:  

```
Input: edge[] = [1, 2, 0, -1]
Output: 3
Explanation: There is only one cycle in the graph i.e. 0 -> 1 -> 2 -> 0. Sum of the cell index in that cycle = 0 + 1 + 2 = 3.

```

```
Input: edge[] = [2, 0, -1, 2]
Output: -1
Explanation: There is no cycle in the graph. The edges are 1 -> 0 -> 2 <- 3. Hence, 2 has no outgoing edge, so no cycle exists.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-02T13:12:42.100Z  

```py
class Solution:
    def largestSumCycle(self, Edge):
        N = len(Edge)
        visited = [0] * N
        best = -1

        for s in range(N):
            if visited[s]:
                continue
            u = s
            while u != -1 and not visited[u]:
                visited[u] = s + 1
                u = Edge[u]

            if u != -1 and visited[u] == s + 1:
                total = 0
                v = u
                while True:
                    total += v
                    v = Edge[v]
                    if v == u:
                        break
                best = max(best, total)

        return best
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/largest-sum-cycle--170645/1)