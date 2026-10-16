class Solution:
    def countAlwaysFound(self, arr):
        n = len(arr)
        suffix_min = [0] * n
        suffix_min[-1] = arr[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(arr[i], suffix_min[i + 1])

        count = 0
        prefix_max = float('-inf')
        for i in range(n):
            right_ok = (i == n - 1) or arr[i] < suffix_min[i + 1]
            if arr[i] > prefix_max and right_ok:
                count += 1
            prefix_max = max(prefix_max, arr[i])
        return count