class Solution:
    def getMinimumDays(self, s, p):
        n = len(s)
        day = [0] * n
        for d, idx in enumerate(p):
            day[idx] = d + 1

        ans = 0
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                ans = max(ans, min(day[i], day[i + 1]))
        return ans