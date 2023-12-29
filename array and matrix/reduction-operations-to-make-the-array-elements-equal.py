class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        count=Counter(nums)
        ans=[]
        for i,j in count.items():
            ans.append(j)
        res=0
        for i in range(1,len(ans)):
            ans[i]=ans[i]+ans[i-1]
        if len(ans)==0:
            return 0

        return sum(ans[:-1])
        