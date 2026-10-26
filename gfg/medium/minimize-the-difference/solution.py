class Solution:
    def minDiff(self, k: int, arr: list[int]) -> int:
        n = len(arr)
        if k >= n:
            return 0
        pre_min = [float('inf')] * (n + 1)
        pre_max = [float('-inf')] * (n + 1)
        suf_min = [float('inf')] * (n + 2)
        suf_max = [float('-inf')] * (n + 2)
        for i in range(n):
            pre_min[i + 1] = min(pre_min[i], arr[i])
            pre_max[i + 1] = max(pre_max[i], arr[i])
        for i in range(n - 1, -1, -1):
            suf_min[i] = min(suf_min[i + 1], arr[i])
            suf_max[i] = max(suf_max[i + 1], arr[i])
        ans = float('inf')
        for i in range(n - k + 1):
            mn = min(pre_min[i], suf_min[i + k])
            mx = max(pre_max[i], suf_max[i + k])
            ans = min(ans, mx - mn)
        return ans