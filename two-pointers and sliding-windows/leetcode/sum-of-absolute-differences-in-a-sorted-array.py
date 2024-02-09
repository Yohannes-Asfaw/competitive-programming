class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        sum1=sum(nums)
        pref=nums.copy()
        for i in range(1,len(pref)):
            pref[i]+=pref[i-1]
        res=[]
        for i in range(len(nums)):
            if i==0:
                res.append(sum1-nums[i]*(len(nums)-i))
            else:
                res.append(((sum1-pref[i])-nums[i]*(len(nums)-i-1))+((i+1)*nums[i])-pref[i])
        return res
        