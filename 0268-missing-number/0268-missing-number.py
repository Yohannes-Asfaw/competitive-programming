class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dictionary={nums[i]:i for i in range(len(nums))}
        for i in range(len(nums)+1):
            if i not in dictionary:
                return i