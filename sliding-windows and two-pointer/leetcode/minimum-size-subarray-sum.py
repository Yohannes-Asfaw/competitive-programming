class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        total=0
        ans=float("inf")
        for right in range(len(nums)):
            total+=nums[right]
            while total>=target:
                total-=nums[left]
                ans=min(ans,right-left+1)
                left+=1
        if ans==float("inf"):
            return 0
        return ans
                
            
        