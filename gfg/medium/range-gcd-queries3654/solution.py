from math import gcd

class Solution:
    def processQueries(self, arr, queries):
        n = len(arr)
        tree = [0] * (2 * n)
        for i in range(n):
            tree[n + i] = arr[i]
        for i in range(n - 1, 0, -1):
            tree[i] = gcd(tree[2 * i], tree[2 * i + 1])

        result = []
        for t, a, b in queries:
            if t == 0:
                l = a + n
                r = b + n + 1
                g = 0
                while l < r:
                    if l & 1:
                        g = gcd(g, tree[l])
                        l += 1
                    if r & 1:
                        r -= 1
                        g = gcd(g, tree[r])
                    l >>= 1
                    r >>= 1
                result.append(g)
            else:
                i = a + n
                tree[i] = b
                i >>= 1
                while i >= 1:
                    tree[i] = gcd(tree[2 * i], tree[2 * i + 1])
                    i >>= 1
        return result