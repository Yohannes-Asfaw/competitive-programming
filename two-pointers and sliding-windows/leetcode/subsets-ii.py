class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def sub(i,path):
            if len(path)==len(nums):
                return 
            for j in range(i,len(nums)):
                path.append(nums[j])
                if sorted(path) not in ans:
                    ans.append(sorted(path.copy()))
                sub(j+1,path)
                path.pop()
        sub(0,[])
        ans.append([])
        return ans