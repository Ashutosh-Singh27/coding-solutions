class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        total = 0
        for i in range(n):
            freq = [0] * 26
            cnt = [0] * (n + 2)
            mx = 0
            mn = 0
            for j in range(i, n):
                c = ord(s[j]) - 97
                old = freq[c]
                if old > 0:
                    cnt[old] -= 1
                freq[c] += 1
                cnt[old + 1] += 1
                if old + 1 > mx:
                    mx = old + 1
                if old == 0:
                    mn = 1
                elif mn == old and cnt[old] == 0:
                    mn = old + 1
                total += mx - mn
        return total