class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        ans=[]
        for i in list(set(nums)):
            if count[i]>len(nums)/3:
                ans.append(i)
        return ans
        