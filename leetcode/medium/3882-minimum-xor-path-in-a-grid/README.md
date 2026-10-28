# Minimum XOR Path in a Grid

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a 2D integer array `grid` of size `m * n`.

You start at the  **top-left**  cell `(0, 0)` and want to reach the  **bottom-right**  cell `(m - 1, n - 1)`.

At each step, you  **may**  move either  **right or down**.

The  **cost**  of a path is defined as the  **bitwise XOR**  of all the values in the cells along that path,  **including**  the start and end cells.

Return the  **minimum**  possible XOR value among all valid paths from `(0, 0)` to `(m - 1, n - 1)`.

 

 **Example 1:** 

 **Input:**  grid = [[1,2],[3,4]]

 **Output:**  6

 **Explanation:** 

There are two valid paths:

- (0, 0) → (0, 1) → (1, 1) with XOR: 1 XOR 2 XOR 4 = 7
- (0, 0) → (1, 0) → (1, 1) with XOR: 1 XOR 3 XOR 4 = 6

The minimum XOR value among all valid paths is 6.

 **Example 2:** 

 **Input:**  grid = [[6,7],[5,8]]

 **Output:**  9

 **Explanation:** 

There are two valid paths:

- (0, 0) → (0, 1) → (1, 1) with XOR: 6 XOR 7 XOR 8 = 9
- (0, 0) → (1, 0) → (1, 1) with XOR: 6 XOR 5 XOR 8 = 11

The minimum XOR value among all valid paths is 9.

 **Example 3:** 

 **Input:**  grid = [[2,7,5]]

 **Output:**  0

 **Explanation:** 

There is only one valid path:

- (0, 0) → (0, 1) → (0, 2) with XOR: 2 XOR 7 XOR 5 = 0

The XOR value of this path is 0, which is the minimum possible.

 

 **Constraints:** 

- 1 <= m == grid.length <= 1000
- 1 <= n == grid[i].length <= 1000
- m * n <= 1000
- 0 <= grid[i][j] <= 1023​

## Solution

**Language:** Python  
**Runtime:** 1049 ms (beats 84.17%)  
**Memory:** 64.8 MB (beats 35.83%)  
**Submitted:** 2026-10-28T10:48:28.528Z  

```py
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[None] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                v = grid[i][j]
                if i == 0 and j == 0:
                    dp[i][j] = {v}
                else:
                    s = set()
                    if i > 0:
                        s |= dp[i - 1][j]
                    if j > 0:
                        s |= dp[i][j - 1]
                    dp[i][j] = {x ^ v for x in s}
        return min(dp[m - 1][n - 1])
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-xor-path-in-a-grid/)