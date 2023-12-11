class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dictionary={}
        for i in range(len(nums)):
            dictionary[nums[i]]=i
        for m in operations:
            nums[dictionary[m[0]]]=m[1]
            dictionary[m[1]]=dictionary[m[0]]
        return nums