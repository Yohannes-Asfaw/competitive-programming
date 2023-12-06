class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negatives=[]
        positives=[]
        ans=[]
        for i in nums:
            if i<0:
                negatives.append(i)
            else:
                positives.append(i)
        for i in range(len(positives)):
            ans.append(positives[i])
            ans.append(negatives[i])
        return ans
        