class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count=0
        left=0
        maxsize=0
        for i in range(len(nums)):
            if nums[i]==0:
                count+=1
            while count>1:
                if nums[left]==0:
                    count-=1
                left+=1
            maxsize=max(maxsize,i-left)
        return maxsize

            

        