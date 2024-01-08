class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum1=sum(nums[:k])
        maxs=sum1
        for i in range(k,len(nums)):
            sum1-=nums[i-k]
            sum1+=nums[i]
            maxs=max(sum1,maxs)
        return maxs/k
     

            
        