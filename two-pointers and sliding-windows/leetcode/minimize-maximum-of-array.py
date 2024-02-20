class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res=nums[0]
        curr=nums[0]
        for i in range(1,len(nums)):
            curr+=nums[i]
            if ceil(curr/(i+1))>res:
                res=ceil(curr/(i+1))
        return res
        


        