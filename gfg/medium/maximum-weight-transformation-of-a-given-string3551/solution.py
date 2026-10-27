class Solution:
    def getMaxWeight(self, s):
        n = len(s)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1
            if i >= 2:
                pair = 4 if s[i - 1] != s[i - 2] else 3
                dp[i] = max(dp[i], dp[i - 2] + pair)
        return dp[n]