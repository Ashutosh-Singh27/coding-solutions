class Solution:
    def longIncPath(self, matrix, n, m):
        cells = sorted(((matrix[i][j], i, j) for i in range(n) for j in range(m)), reverse=True)
        dp = [[1] * m for _ in range(n)]
        best = 1
        for v, i, j in cells:
            cur = 1
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                x, y = i + di, j + dj
                if 0 <= x < n and 0 <= y < m and matrix[x][y] > v:
                    if dp[x][y] + 1 > cur:
                        cur = dp[x][y] + 1
            dp[i][j] = cur
            if cur > best:
                best = cur
        return best