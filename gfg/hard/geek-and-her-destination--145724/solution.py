class Solution:
    def minTime(self, a: int, b: int, d: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        c = max(a - b, 1)

        def F(u):
            if u <= 0:
                return 0
            q, rem = divmod(u, c)
            return c * q * (q + 1) // 2 + rem * (q + 1)

        total = 0

        cnt_far = max(0, r - max(l, d) + 1)
        total += cnt_far

        if l < d:
            hi_j = min(r, d - 1)
            t_lo = d - hi_j
            t_hi = d - l
            cnt = t_hi - t_lo + 1
            sum_t = (t_lo + t_hi) * cnt // 2
            sum_k = F(t_hi - a) - F(t_lo - 1 - a)
            total += cnt + sum_t + 2 * b * sum_k

        return total % MOD