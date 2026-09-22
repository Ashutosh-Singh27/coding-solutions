from bisect import bisect_left

class Solution:
    def findLongestWord(self, s, d):
        positions = [[] for _ in range(26)]
        for i, ch in enumerate(s):
            positions[ord(ch) - 97].append(i)

        def isSubsequence(word):
            pos = -1
            for ch in word:
                lst = positions[ord(ch) - 97]
                idx = bisect_left(lst, pos + 1)
                if idx == len(lst):
                    return False
                pos = lst[idx]
            return True

        result = ""
        for word in d:
            if isSubsequence(word):
                if len(word) > len(result) or (len(word) == len(result) and word < result):
                    result = word
        return result