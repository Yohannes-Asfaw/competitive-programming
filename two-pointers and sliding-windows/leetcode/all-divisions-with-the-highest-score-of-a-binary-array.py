class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ones=nums.count(1)
        zeros=0
        dictionary={}
        dictionary[0]=ones
        for i in range(len(nums)):
            if nums[i]==0:
                zeros+=1
            elif nums[i]==1:
                ones-=1
            dictionary[i+1]=zeros+ones
        sortedlist=sorted(dictionary.items(), key=lambda x:x[1],reverse=True)
        ans=[]
        maxval=sortedlist[0][1]
        for i in sortedlist:
            if i[1]==maxval:
                ans.append(i[0])
        return ans
