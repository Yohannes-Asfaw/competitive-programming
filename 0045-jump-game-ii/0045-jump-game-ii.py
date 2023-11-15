class Solution:
    def jump(self, nums: List[int]) -> int:
        l=0
        r=0
        jump=0
        while r<len(nums)-1:
            longest_jump=0
            for i in range(l,r+1):
                longest_jump=max(longest_jump,i+nums[i])
            l=l+1
            r=longest_jump
            jump+=1
        return(jump)