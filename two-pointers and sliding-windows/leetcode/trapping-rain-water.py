class Solution:
    def trap(self, nums: List[int]) -> int:
        nostack1=[]
        nostack2=[]
        curmax=nums[0]
        ans=0
        for i in range(len(nums)):
            curmax=max(nums[i],curmax)
            nostack1.append(curmax)
        curmax1=nums[-1] 
        for i in ((nums[::-1])):
            curmax1=max(i,curmax1)
            nostack2.append(curmax1)
        nostack2=nostack2[::-1]
        for i in range(len(nums)):
            ans+=min(nostack1[i],nostack2[i])-nums[i]
        
        return ans


        