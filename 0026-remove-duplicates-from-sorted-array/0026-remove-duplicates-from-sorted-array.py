class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insertindex=0
        for i in range(1,len(nums)):
            if nums[i-1]!=nums[i]:
                nums[insertindex]=nums[i-1]
                insertindex+=1
        nums[insertindex]=nums[-1]
        insertindex+=1
        return insertindex
            
