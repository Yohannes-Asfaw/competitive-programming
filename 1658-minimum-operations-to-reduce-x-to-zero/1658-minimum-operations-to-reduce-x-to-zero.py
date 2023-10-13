class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target=sum(nums)-x
        cursum=0
        maxwindow=-1
        l=0
        for r in range(len(nums)):
            cursum+=nums[r]
            while l<=r and cursum>target:
                cursum-=nums[l]
                l+=1
            if cursum==target:
                maxwindow=max(maxwindow,r-l+1)
        if maxwindow==-1:
            return -1
        else:
            return len(nums)-maxwindow
