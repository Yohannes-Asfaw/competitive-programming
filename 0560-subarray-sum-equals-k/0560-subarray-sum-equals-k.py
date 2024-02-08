class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mydict=defaultdict(int)
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        res=0
        for val in nums:
            
            if val==k:
                res+=1
            if val-k in mydict:
                res+=mydict[val-k]
            mydict[val]+=1
        return res
            