def largestNumber(self, nums: List[int]) -> str:
        ans=[]
        for i in nums:
            ans.append(str(i))
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if ans[i]+ans[j]>ans[j]+ans[i]:
                    continue
                else:
                    ans[i],ans[j]=ans[j],ans[i]
        
        res="".join(ans)
        if int(res)==0:
            return "0"
        return res
