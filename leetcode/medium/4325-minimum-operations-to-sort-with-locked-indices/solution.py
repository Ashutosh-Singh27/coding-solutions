class Solution:
    def minOperations(self, nums: list[int], locked: list[int], k: int) -> int:
        n= len(nums)
        inv=0
        for i in range(n):
            for j in range(i+1, n):
                if nums[i]>nums[j]:
                    inv+=1
        need=0
        start=0
        mx=0
        for i in range(n):
            mx=max(mx,nums[i])
            if mx ==i+1:
                if i-start+1>=2:
                    need+=sum(locked[start:i+1])
                start = i+1
        if need>k:
            return -1
        return inv + need