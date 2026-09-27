class Solution:
    def longestPath(self, s, edges):
        n = len(s)
        if n == 1:
            return 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        color = {i + 1: s[i] for i in range(n)}
        parent = [0] * (n + 1)
        visited = [False] * (n + 1)
        order = []
        stack = [1]
        visited[1] = True
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    stack.append(v)
        A0 = [0] * (n + 1)
        A1 = [0] * (n + 1)
        ans = 1
        for u in reversed(order):
            pairs = []
            for v in adj[u]:
                if v == parent[u]:
                    continue
                if color[v] == color[u]:
                    c0 = A0[v]
                    c1 = A1[v]
                else:
                    c0 = 0
                    c1 = A0[v]
                pairs.append((c0, c1))
            if not pairs:
                A0[u] = 1
                A1[u] = 1
                continue
            c0_vals = [p[0] for p in pairs]
            top1 = -1
            idx1 = -1
            for i, c0 in enumerate(c0_vals):
                if c0 > top1:
                    top1 = c0
                    idx1 = i
            top2 = -1
            for i, c0 in enumerate(c0_vals):
                if i != idx1 and c0 > top2:
                    top2 = c0
            if top1 < 0:
                top1 = 0
            if top2 < 0:
                top2 = 0
            best_no_budget = top1 + top2
            best_with_budget = 0
            for i, (c0, c1) in enumerate(pairs):
                other = top2 if i == idx1 else top1
                val = c1 + other
                if val > best_with_budget:
                    best_with_budget = val
            A0[u] = 1 + top1
            A1[u] = 1 + max(p[1] for p in pairs)
            cand = 1 + max(best_no_budget, best_with_budget)
            if cand > ans:
                ans = cand
        return ans