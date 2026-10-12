class Solution:
    def minSquares(self, n, m):
        res = 0
        while m:
            res += n // m
            n, m = m, n % m
        return res