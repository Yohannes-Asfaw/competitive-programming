class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if (target-nums[i] in nums):
                one=nums.index(target-nums[i])
                if (i!=one):
                    return [i,one]

        