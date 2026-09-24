class Solution:
    def maxStackHeight(self, r, h, n=None):
        if n is None:
            n = len(r)
        discs = sorted(zip(r, h), key=lambda x: (x[0], -x[1]))
        hs = [d[1] for d in discs]

        sorted_h = sorted(set(hs))
        comp = {v: i + 1 for i, v in enumerate(sorted_h)}
        m = len(sorted_h)
        tree = [0] * (m + 1)

        def update(i, val):
            while i <= m:
                if tree[i] < val:
                    tree[i] = val
                i += i & (-i)

        def query(i):
            res = 0
            while i > 0:
                if tree[i] > res:
                    res = tree[i]
                i -= i & (-i)
            return res

        ans = 0
        for height in hs:
            idx = comp[height]
            best = query(idx - 1) + height
            update(idx, best)
            ans = max(ans, best)

        return ans