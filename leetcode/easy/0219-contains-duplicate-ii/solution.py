class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        last_seen = {}
        for i, n in enumerate(nums):
            if n in last_seen and i - last_seen[n] <= k:
                return True
            last_seen[n] = i
        return False