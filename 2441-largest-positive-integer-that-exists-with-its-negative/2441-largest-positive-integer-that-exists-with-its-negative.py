class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        count={}
        ans=0
        for i in nums:
            if i<0:
                count[i]=1
        for i in nums:
            if i >0 and (-1*i) in count:
                ans=max(ans,i)
        if ans:
            return ans
        else:
            return -1
