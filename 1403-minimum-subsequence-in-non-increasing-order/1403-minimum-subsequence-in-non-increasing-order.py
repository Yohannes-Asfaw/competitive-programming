class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        ans=[]
        nums.sort()
        total=sum(nums)
        subsum=0
        ans=[]
        index=len(nums)-1
        while total>=subsum:
            ans.append(nums[index])
            total-=nums[index]
            subsum+=nums[index]
            index-=1
        return sorted(ans, reverse=True)
