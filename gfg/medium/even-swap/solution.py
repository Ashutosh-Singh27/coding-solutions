class Solution:
    def lexicographicallyLargest(self, arr: list[int]) -> list[int]:
        n = len(arr)
        result = []
        i = 0
        while i < n:
            j = i
            while j < n and arr[j] % 2 == arr[i] % 2:
                j += 1
            result.extend(sorted(arr[i:j], reverse=True))
            i = j
        return result