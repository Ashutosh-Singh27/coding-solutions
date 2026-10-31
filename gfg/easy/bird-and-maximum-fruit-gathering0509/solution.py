class Solution:
    def maxPackages(self, arr, totalTime):
        n = len(arr)
        k = min(totalTime, n)
        cur = sum(arr[:k])
        best = cur
        for i in range(k, n):
            cur += arr[i] - arr[i - k]
            if cur > best:
                best = cur
        return best