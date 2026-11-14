class Solution:
    def maxEqualSum(self, s1, s2, s3):
        a, b, c = sum(s1), sum(s2), sum(s3)
        i = j = k = 0
        n1, n2, n3 = len(s1), len(s2), len(s3)
        while i < n1 and j < n2 and k < n3:
            if a == b == c:
                return a
            m = max(a, b, c)
            if a == m:
                a -= s1[i]
                i += 1
            elif b == m:
                b -= s2[j]
                j += 1
            else:
                c -= s3[k]
                k += 1
        return 0