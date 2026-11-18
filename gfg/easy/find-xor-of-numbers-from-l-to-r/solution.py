class Solution:
    def findXOR(self, l, r):
        def f(n):
            m = n % 4
            if m == 0:
                return n
            if m == 1:
                return 1
            if m == 2:
                return n + 1
            return 0
        return f(r) ^ f(l - 1)