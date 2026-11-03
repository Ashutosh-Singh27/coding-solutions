class Solution:
    def maximumWeight(self, n, edges, queries):
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        edges = sorted(edges, key=lambda e: e[2])
        order = sorted(range(len(queries)), key=lambda i: queries[i])
        ans = [0] * len(queries)

        j = 0
        pairs = 0
        for i in order:
            x = queries[i]
            while j < len(edges) and edges[j][2] <= x:
                u, v, _ = edges[j]
                ru, rv = find(u), find(v)
                if ru != rv:
                    pairs += size[ru] * size[rv]
                    if size[ru] < size[rv]:
                        ru, rv = rv, ru
                    parent[rv] = ru
                    size[ru] += size[rv]
                j += 1
            ans[i] = pairs
        return ans