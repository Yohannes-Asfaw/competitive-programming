class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        if len (nums)==1:
            return [0]
        sum1=sum(nums)
        ans=[0]*len(nums)
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        ans[0]=sum1-nums[0]
        ans[len(nums)-1]=nums[len(nums)-2]
        for i in range(1,len(nums)-1):
            ans[i]=abs(nums[i-1]-(sum1-nums[i]))
        
        return ans
        