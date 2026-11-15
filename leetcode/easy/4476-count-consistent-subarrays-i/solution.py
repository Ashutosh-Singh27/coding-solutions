class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        n = len(nums)
        B = max(nums).bit_length() or 1

        # L[i]: nearest left index missing a bit of nums[i], or equal in value
        L = [-1] * n
        last_unset = [-1] * B
        last_val = {}
        for i, x in enumerate(nums):
            l = last_val.get(x, -1)
            for b in range(B):
                if x >> b & 1:
                    l = max(l, last_unset[b])
            L[i] = l
            for b in range(B):
                if not x >> b & 1:
                    last_unset[b] = i
            last_val[x] = i

        # Right side: nearest index missing a bit of nums[i]
        ans = 0
        next_unset = [n] * B
        for i in range(n - 1, -1, -1):
            x = nums[i]
            r = n
            for b in range(B):
                if x >> b & 1:
                    r = min(r, next_unset[b])
            ans += (i - L[i]) * (r - i)
            for b in range(B):
                if not x >> b & 1:
                    next_unset[b] = i
        return ans