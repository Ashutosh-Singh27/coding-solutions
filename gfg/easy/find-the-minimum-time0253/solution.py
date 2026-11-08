class Solution:
    def minTime(self, n, s1, s2):
        lo, hi = 1, n * min(s1, s2)
        while lo < hi:
            mid = (lo + hi) // 2
            if mid // s1 + mid // s2 >= n:
                hi = mid
            else:
                lo = mid + 1
        return lo