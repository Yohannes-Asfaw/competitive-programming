class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        negatives=[]
        positives=[]
        ans=1
        for i in nums:
            if i>0:
                positives.append(i)
            elif i<0:
                negatives.append(i)
        negatives.sort()
        if len(negatives)%2!=0:
            negatives.pop()
        if len(positives)!=0:
            for i in positives:
                ans*=i
        if len(negatives)!=0:
            for i in negatives:
                ans*=i
        if len(positives)==0 and len(negatives)==0:
            return 0
        return ans
