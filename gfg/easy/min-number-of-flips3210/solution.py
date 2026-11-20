class Solution:
    def minFlips(self, s):
        n = len(s)
        a = 0
        for i in range(n):
            if int(s[i]) != i % 2:
                a += 1
        return min(a, n - a)