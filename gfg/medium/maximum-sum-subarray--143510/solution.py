class Solution:
    def maximumSubarray(self, arr):
        a = arr[0]
        b = arr[0] * arr[0]
        best = max(a, b)
        for x in arr[1:]:
            new_b = max(b + x, max(a, 0) + x * x)
            a = max(a + x, x)
            b = new_b
            best = max(best, a, b)
        return best