from typing import List
from collections import Counter

class Solution:
    def cntSubsets(self, arr: List[int], l: int, r: int) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        cnt = Counter(arr)
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = pow2[i - 1] * 2 % MOD

        ans = 0
        prod = 1
        used = 0
        for m in range(0, min(r, n) + 1):
            if m > 0:
                c = cnt.get(m - 1, 0)
                if c == 0:
                    break
                prod = prod * (pow2[c] - 1) % MOD
                used += c
            if m >= l:
                greater = n - used - cnt.get(m, 0)
                ans = (ans + prod * pow2[greater]) % MOD
        return ans