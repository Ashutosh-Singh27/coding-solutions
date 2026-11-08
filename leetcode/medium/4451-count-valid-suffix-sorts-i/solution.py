class Solution:
    def countSuffix(self, nums: list[int], target: list[int]) -> int:
        n=len(nums)
        if Counter(nums)!=Counter(target):
            return 0
        p=0
        while p<n and nums[p]==target[p]:
            p+=1
        p=min(p,n-1)
        s=n-1
        while s>0 and target[s-1]>=target[s]:
            s-=1
        return max(0,p-s+1)