class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        check=sorted(nums)
        ans=[]
        for i in nums:
            ans.append(check.index(i))
        return ans