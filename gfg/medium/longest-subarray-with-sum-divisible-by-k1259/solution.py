class Solution:
    def longestSubarrayDivK(self, arr, k):
        first = {0: -1}   
        best = 0
        pref = 0
        for i, v in enumerate(arr):
            pref = (pref + v) % k
            if pref in first:
                best = max(best, i - first[pref])
            else:
                first[pref] = i
        return best