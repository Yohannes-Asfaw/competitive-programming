class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        j=len(nums)-1
        set1=set()
        while i<j:
            set1.add((nums[i]+nums[j])/2)
            i+=1
            j-=1
        return len(set1)
