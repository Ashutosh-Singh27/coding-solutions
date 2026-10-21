# Shortest Safe Route in Grid

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a 2D matrix  **mat[][]**, where each cell is either 0 (landmine) or 1 (safe), find the minimum number of steps required to travel from any cell in the leftmost column to any cell in the rightmost column.

- You can move only in four directions: up, down, left, and right.
- A cell is unsafe if it contains a landmine or is directly adjacent (up, down, left, or right) to a landmine, and such cells must be avoided.
- Return -1 if no safe path exists.

 **Examples:** 

```
Input: mat[][] = [[1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]]

Output: 6
Explanation: We can see that length of shortest safe route is 6. 

```

```
Input: mat[][] = [[1, 1, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 1, 1]]

Output: -1
Explanation: There is no possible path from first column to last column.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-21T02:06:19.936Z  

```py
from collections import deque

class Solution:
    def shortestPath(self, mat):
        n = len(mat)
        m = len(mat[0])
        safe = [[True] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    safe[i][j] = False
                    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < m:
                            safe[ni][nj] = False
        dist = [[-1] * m for _ in range(n)]
        q = deque()
        for i in range(n):
            if safe[i][0]:
                dist[i][0] = 1
                q.append((i, 0))
        while q:
            i, j = q.popleft()
            if j == m - 1:
                return dist[i][j]
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and safe[ni][nj] and dist[ni][nj] == -1:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))
        return -1
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/find-shortest-safe-route-in-a-matrix/1)