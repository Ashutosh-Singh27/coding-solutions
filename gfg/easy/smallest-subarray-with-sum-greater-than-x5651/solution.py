class Solution:
    def smallestSubWithSum(self, arr, x):
        n = len(arr)
        left = 0
        total = 0
        best = n + 1
        for right in range(n):
            total += arr[right]
            while total > x:
                best = min(best, right - left + 1)
                total -= arr[left]
                left += 1
        return best if best <= n else 0