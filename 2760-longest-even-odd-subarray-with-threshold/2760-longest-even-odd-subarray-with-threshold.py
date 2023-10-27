class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans=0
        count=0
        for i in range(len(nums)):
            if nums[i]%2==0 and nums[i]<=(threshold):
                j=i+1
                while j<len(nums):
                    if nums[j-1]%2!=nums[j]%2 and nums[j]<=threshold:
                        j+=1
                    else:
                        break
                ans=max(ans,j-i)
        return ans


        
        