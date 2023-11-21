class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump=0
        if 0 not in nums:
            return True
        if len(nums)==1:
            return True
        else:
            for i in range(len(nums)-1):
                if nums[i]==0 and jump<=nums[i]+i:
                    return False
                jump = max(jump, i + nums[i])
                if jump>=len(nums)-1:
                    return True

