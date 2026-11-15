class Solution:
    def maxDifference(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 2)
        for i in range(n - 1, -1, -1):
            s = nums[i]
            best = s - dp[i + 1] if s % 3 == 0 else s + dp[i + 1]
            if i + 1 < n:
                s = nums[i] + nums[i + 1]
                v = s - dp[i + 2] if s % 3 == 0 else s + dp[i + 2]
                best = max(best, v)
            dp[i] = best
        return dp[0]