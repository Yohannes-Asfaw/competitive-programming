class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary={}
        for i in range(len(nums)):
            dictionary[nums[i]]=i
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in dictionary and dictionary[diff]!=i:
                return [i,dictionary[diff]]