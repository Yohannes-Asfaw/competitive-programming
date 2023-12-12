class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count=0
        maxcount=0
        nums=set(nums)

        for i in nums:
            if i-1 in nums:
                continue
            while i in nums:
                count+=1
                i+=1
            maxcount = max(maxcount, count)
            count=0
        return(maxcount)