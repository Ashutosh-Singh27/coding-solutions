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