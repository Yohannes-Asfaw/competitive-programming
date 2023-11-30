class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans=0
        count=Counter(nums)
        for i in count.keys():
            if count[i]>1:
                ans+=(count[i]*(count[i]-1))//2
        return ans

        