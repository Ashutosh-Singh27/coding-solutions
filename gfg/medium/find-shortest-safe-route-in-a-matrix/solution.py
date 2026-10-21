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