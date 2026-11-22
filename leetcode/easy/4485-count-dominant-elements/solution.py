class Solution:
    def countDominantElements(self, nums: list[int]) -> int:
        n=len(nums)
        count=0
        for i in range(n):
            if n==1:
                count+=1
            elif i==0:
                if nums[i]>=nums[i+1]:
                    count+=1
            elif i==n-1:
                if nums[i]>=nums[i-1]:
                    count+=1
            else:
                if 2*nums[i]>=nums[i-1]+nums[i+1]:
                    count+=1
        return count