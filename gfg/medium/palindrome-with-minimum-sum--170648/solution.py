class Solution:
    def minimumSum(self, s: str) -> int:
        n = len(s)
        arr = list(s)
        for i in range(n // 2):
            j = n - 1 - i
            if arr[i] == '?':
                arr[i] = arr[j]
            elif arr[j] == '?':
                arr[j] = arr[i]
            elif arr[i] != arr[j]:
                return -1
        m = (n + 1) // 2
        prev = None
        total = 0
        for i in range(m):
            if arr[i] != '?':
                if prev is not None:
                    total += abs(ord(arr[i]) - ord(prev))
                prev = arr[i]
        return 2 * total