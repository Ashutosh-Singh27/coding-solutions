class Solution:
    def minimumCost(self, x, s, m, l, cs, cm, cl):
        dp = [0] + [float('inf')] * x
        for j in range(1, x + 1):
            dp[j] = min(
                dp[max(0, j - s)] + cs,
                dp[max(0, j - m)] + cm,
                dp[max(0, j - l)] + cl
            )
        return dp[x]