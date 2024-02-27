class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxjump=nums[0]
        if len(nums)==1:
            return True
        for i in range(len(nums)):
            maxjump=max(maxjump,i+nums[i])
            if nums[i]==0 and maxjump<=i:
                return False
            if maxjump>=len(nums)-1:
                return True
        return False

        