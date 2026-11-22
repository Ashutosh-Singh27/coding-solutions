class Solution:
    def minCost(self, nums: list[int]) -> int:
        n = len(nums)
        best = float('inf')
        i = 0
        while i < n:
            j = i
            while j + 1 < n and nums[j + 1] == nums[i]:
                j += 1
            a, b, v = i, j, nums[i]  
            if a == 0 and b == n - 1:
                return 0             
            if a == 0:
                if b >= 1:            
                    best = min(best, v * (n - 1 - b))
            elif b == n - 1:
                if a <= n - 2:        
                    best = min(best, v * a)
            else:
                best = min(best, v * (a + n - 1 - b))
            i = j + 1
        return best