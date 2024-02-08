class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        total=sum(nums)
        nums=[0]+nums+[0]
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        for i in range(1,len(nums)):
            if total-nums[i-1]==nums[i]:
                if i-1<len(nums)-2:
                    return i-1
        return -1
        
        