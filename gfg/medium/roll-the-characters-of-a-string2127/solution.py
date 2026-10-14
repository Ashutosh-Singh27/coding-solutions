class Solution:
    def findRollOut(self, s, roll):
        n = len(s)
        cnt = [0] * (n + 1)
        for r in roll:
            cnt[r - 1] += 1
        res = []
        total = 0
        for i in range(n - 1, -1, -1):
            total += cnt[i]
            res.append(chr((ord(s[i]) - 97 + total) % 26 + 97))
        return "".join(reversed(res))