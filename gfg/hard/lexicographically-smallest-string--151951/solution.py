class Solution:
    def lexiString(self, s: str) -> str:
        n = len(s)
        t = s + s
        i, j, k = 0, 1, 0
        while i < n and j < n and k < n:
            a = t[i + k]
            b = t[j + k]
            if a == b:
                k += 1
            else:
                if a > b:
                    i += k + 1
                else:
                    j += k + 1
                if i == j:
                    j += 1
                k = 0
        start = min(i, j)
        return t[start:start + n]