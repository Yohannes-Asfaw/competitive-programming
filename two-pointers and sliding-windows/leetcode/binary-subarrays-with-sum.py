class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        mydict=defaultdict(int)
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        count=0
        for i in nums:
            if i==goal:
                count+=1
            if i-goal in mydict:
                count+=mydict[i-goal]
            if i in mydict:
                mydict[i]+=1
            else:
                mydict[i]=1
        return count
