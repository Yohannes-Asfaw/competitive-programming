class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        count=defaultdict(int)
        left=0
        ans=0
        res=0
        for right in range(len(nums)):
            count[nums[right]]+=1
            ans+=nums[right]
            while count[nums[right]]>1:
                count[nums[left]]-=1
                ans-=nums[left]
                left+=1
            res=max(res,ans)
        return res
            
            
            
        