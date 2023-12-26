class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros=nums.count(0)
        ones=nums.count(1)
        for i in range(len(nums)):
            if zeros>0:
                nums[i]=0
                zeros-=1
            elif ones>0:
                nums[i]=1
                ones-=1
            else:
                nums[i]=2
        