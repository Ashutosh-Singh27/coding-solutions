class Solution:
    def socialNetwork(self, arr):
        n = len(arr) + 1
        parent = [0] * (n + 1)
        for i in range(2, n + 1):
            parent[i] = arr[i - 2]
        result = []
        for i in range(2, n + 1):
            dist = {}
            node = i
            steps = 0
            while node != 1:
                node = parent[node]
                steps += 1
                dist[node] = steps
            for j in range(1, i):
                if j in dist:
                    result.append([i, j, dist[j]])
        return result