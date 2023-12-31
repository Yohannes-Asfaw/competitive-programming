class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        ans=0
        nums.append(0)
        nums.sort()
        for a,b in zip(nums,nums[1:]):
            if a==b:
                continue
            l=a+1
            r=min(a+k,b-1)
            ans+=(r+l)*(r-l+1)//2
            k-=(r-l+1)
            if k==0:
                return(ans)
        if k>0:
            l=nums[-1]+1
            r=nums[-1]+k
            ans+=(r+l)*(r-l+1)//2
        return(ans)









    

