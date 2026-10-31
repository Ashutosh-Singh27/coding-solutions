class Solution:
    def uniquePaths(self, grid):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        L0 = [[-1] * (n + 1) for _ in range(m + 1)]
        L1 = [[-1] * (n + 1) for _ in range(m + 1)]
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if grid[r][c] == 0:
                    L0[r][c] = r * n + c
                    L1[r][c] = r * n + c
                else:
                    L0[r][c] = L1[r + 1][c]
                    L1[r][c] = L0[r][c + 1]
        dp = [0] * (m * n)
        dp[0] = 1
        for i in range(m):
            for j in range(n):
                cur = dp[i * n + j]
                if cur == 0 or grid[i][j] == 1:
                    continue
                if j + 1 < n:
                    t = L0[i][j + 1]
                    if t != -1:
                        dp[t] = (dp[t] + cur) % MOD
                if i + 1 < m:
                    t = L1[i + 1][j]
                    if t != -1:
                        dp[t] = (dp[t] + cur) % MOD
        return dp[m * n - 1] % MOD