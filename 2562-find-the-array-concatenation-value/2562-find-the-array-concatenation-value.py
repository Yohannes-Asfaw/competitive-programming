class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        ans=0
        while(j>=i):
            if i!=j:
                temp=str(nums[i])+str(nums[j])
            elif i==j:
                temp=str(nums[i])
            ans+=int(temp)
            i+=1
            j-=1
        return ans


        
