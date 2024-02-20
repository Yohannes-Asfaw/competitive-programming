class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans=0
        for K in range(2,len(nums)):
            i,j=0,K-1
            while i<j:
                if nums[i]+nums[j]>nums[K]:
                    ans+=j-i
                    j-=1
                else:
                    i+=1
        return ans
                

                    
                
                


