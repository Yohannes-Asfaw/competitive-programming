class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        minsum=0
        maxsum=nums[0]
        prefix=0
        for i in nums:
            prefix+=i
            maxsum=max(maxsum,prefix-minsum)
            minsum=min(prefix,minsum)
            
        return maxsum




        