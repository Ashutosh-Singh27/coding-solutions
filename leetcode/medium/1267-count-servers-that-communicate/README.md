# Count Servers that Communicate

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a map of a server center, represented as a `m * n` integer matrix `grid`, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

 

 **Example 1:** 

```
Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.
```

 **Example 2:** 

```
Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.

```

 **Example 3:** 

```
Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.

```

 

 **Constraints:** 

- m == grid.length
- n == grid[i].length
- 1 <= m <= 250
- 1 <= n <= 250
- grid[i][j] == 0 or 1

## Solution

**Language:** Python  
**Runtime:** 23 ms (beats 33.05%)  
**Memory:** 21.4 MB (beats 89.83%)  
**Submitted:** 2026-11-08T04:13:33.964Z  

```py
class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m,n=len(grid),len(grid[0])
        rows=[sum(r)for r in grid]
        cols=[sum(grid[i][j]for i in range(m))for j in range(n)]
        return sum(
            1
            for i in range(m)
            for j in range(n)
            if grid[i][j]and(rows[i]>1 or cols[j]>1)
        )
```

---

[View on LeetCode](https://leetcode.com/problems/count-servers-that-communicate/)