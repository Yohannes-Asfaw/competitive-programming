class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=float('-inf')
        maxending_here = 0
        for i in nums:
            if maxending_here>0:
                maxending_here+=i
            elif maxending_here<=0:
                maxending_here=i
            maxsum=max(maxsum,maxending_here)
        return maxsum