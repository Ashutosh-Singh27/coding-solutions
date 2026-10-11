class Solution:
    def mergeTwoParts(self, arr):
        n = len(arr)
        k = n
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                k = i
                break
        left = arr[:k]
        right = arr[k:]
        i = j = 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res.extend(left[i:])
        res.extend(right[j:])
        arr[:] = res
        return arr