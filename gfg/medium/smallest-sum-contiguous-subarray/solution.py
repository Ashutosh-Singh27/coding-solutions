class Solution:
    def minSubarraySum(self, arr):
        cur = arr[0]
        best = arr[0]
        for x in arr[1:]:
            cur = min(x, cur + x)
            best = min(best, cur)
        return best