class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insertindex=0
        for i in range(len(nums)):
            if i==0 or nums[i-1]!=nums[i]:
                nums[insertindex]=nums[i]
                insertindex+=1
        return insertindex
