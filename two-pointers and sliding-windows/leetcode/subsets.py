class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all=[]
        def sub(i,path):
            if len(path)==len(nums):
                return  
            for j in range(i,len(nums)):
                if nums[j] not in path:
                    path.append(nums[j])
                    all.append(path.copy())
                    sub(j,path)
                    path.pop()
        sub(0,[])
        all.append([])
        return all