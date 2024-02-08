class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total=1
        count=nums.count(0)
        print(count)
        ans=[]
        if count<=1:
            for i in nums:
                if i!=0:
                    total*=i
            for i in nums:
                if i==0 and count==1:
                    ans.append(total)
                if count==1 and i!=0:
                    ans.append(0)
                if i!=0 and count==0:
                    ans.append(total//i)
            return ans
        
        return [0]*len(nums)
        