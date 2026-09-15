from bisect import bisect_right

class Solution:
    def dominantPairs(self, arr: list[int]) -> int:
        n = len(arr)
        mid = n // 2

        second = sorted(arr[mid:])
        ans = 0

        for i in range(mid):
            limit = arr[i] // 5
            ans += bisect_right(second, limit)

        return ans