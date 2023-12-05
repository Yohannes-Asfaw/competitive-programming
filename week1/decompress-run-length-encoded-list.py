class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans=[]
        i=0
        j=1
        while j<len(nums):
            ans+=[nums[j]]*nums[i]
            i+=2
            j+=2
        return ans